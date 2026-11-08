// Network shim for sandboxed capture. Some sandboxes block every host except package registries.
// Google Fonts and npm CDNs (jsDelivr /npm/, unpkg) can be rebuilt from the npm registry, so pages
// render with their real fonts and scripts. Everything else that fails is recorded, never hidden.
import { execFileSync } from "node:child_process";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";

const CACHE = process.env.UNSLOP_NPM_CACHE || path.join(os.homedir(), ".cache/unslop/npm");
const FONT_HOST = "https://unslop-fonts.invalid/";
fs.mkdirSync(CACHE, { recursive: true });

function npmPackage(spec) {
  // returns the extracted package dir for "name@version" (version optional), or null
  const safe = spec.replace(/[\/@]/g, "_");
  const dir = path.join(CACHE, safe);
  if (fs.existsSync(path.join(dir, "package.json"))) return dir;
  if (fs.existsSync(dir + ".missing")) return null;
  try {
    const out = execFileSync("npm", ["pack", spec, "--silent", "--pack-destination", CACHE], { cwd: CACHE, timeout: 90000, stdio: ["ignore", "pipe", "ignore"] }).toString().trim().split("\n").pop();
    fs.mkdirSync(dir, { recursive: true });
    execFileSync("tar", ["-xzf", path.join(CACHE, out), "-C", dir, "--strip-components=1"]);
    return dir;
  } catch { fs.writeFileSync(dir + ".missing", ""); return null; }
}

function googleFamilies(url) {
  const u = new URL(url);
  const fams = [];
  for (const f of u.searchParams.getAll("family")) {
    for (const part of f.split("|")) {
      const [name, axes = ""] = part.split(":");
      const weights = (axes.match(/\d{3}/g) || ["400"]).map(Number);
      fams.push({ name: name.replace(/\+/g, " ").trim(), weights: [...new Set(weights)], italic: /ital|italic|i\b/.test(axes) });
    }
  }
  return fams;
}

function fontCss(fam) {
  const id = fam.name.toLowerCase().replace(/\s+/g, "-");
  const dir = npmPackage(`@fontsource/${id}`);
  if (!dir) return null;
  const css = [];
  const files = fs.readdirSync(dir).filter((f) => /^\d{3}(-italic)?\.css$/.test(f));
  for (const f of files) {
    const w = +f.slice(0, 3);
    const lo = Math.min(...fam.weights), hi = Math.max(...fam.weights);
    if (w < lo - 1 || w > hi + 1) continue;      // keep the requested weight range
    css.push(fs.readFileSync(path.join(dir, f), "utf8").replace(/url\(\.\/files\//g, `url(${FONT_HOST}${encodeURIComponent(id)}/files/`));
  }
  return css.length ? css.join("\n") : null;
}

export async function installShim(ctx, log) {
  const net = { shimmed: [], blocked: [], fontsMissing: [] };
  await ctx.route(/^https:\/\/fonts\.googleapis\.com\/css/, async (route) => {
    const fams = googleFamilies(route.request().url());
    let body = "";
    for (const fam of fams) {
      const css = fontCss(fam);
      if (css) { body += css + "\n"; net.shimmed.push(`font ${fam.name}`); }
      else net.fontsMissing.push(fam.name);
    }
    await route.fulfill({ status: 200, contentType: "text/css", body });
  });
  await ctx.route(FONT_HOST + "**", async (route) => {
    const rel = decodeURIComponent(route.request().url().slice(FONT_HOST.length));
    const [id, ...rest] = rel.split("/");
    const file = path.join(CACHE, `_fontsource_${id}`, ...rest);
    if (fs.existsSync(file)) await route.fulfill({ status: 200, contentType: "font/woff2", body: fs.readFileSync(file) });
    else await route.abort();
  });
  await ctx.route(/^https:\/\/(cdn\.jsdelivr\.net\/npm|unpkg\.com)\//, async (route) => {
    const url = new URL(route.request().url());
    const p = url.pathname.replace(/^\/npm\//, "/").slice(1);           // name@ver/path or @scope/name@ver/path
    const m = p.match(/^((?:@[^/]+\/)?[^/@]+)(?:@([^/]+))?(\/.*)?$/);
    if (!m) return route.abort();
    const dir = npmPackage(m[2] ? `${m[1]}@${m[2]}` : m[1]);
    if (!dir) { net.blocked.push(url.href); return route.abort(); }
    let file = m[3] && m[3] !== "/" ? path.join(dir, m[3]) : null;
    if (!file || !fs.existsSync(file)) {
      const pj = JSON.parse(fs.readFileSync(path.join(dir, "package.json"), "utf8"));
      file = path.join(dir, pj.unpkg || pj.jsdelivr || pj.browser || pj.main || "index.js");
    }
    if (!fs.existsSync(file)) { net.blocked.push(url.href); return route.abort(); }
    const ext = path.extname(file);
    const type = { ".css": "text/css", ".js": "application/javascript", ".mjs": "application/javascript", ".json": "application/json", ".woff2": "font/woff2", ".svg": "image/svg+xml" }[ext] || "application/octet-stream";
    net.shimmed.push(`npm ${m[1]}${m[2] ? "@" + m[2] : ""}`);
    await route.fulfill({ status: 200, contentType: type, body: fs.readFileSync(file) });
  });
  for (const pair of (process.env.UNSLOP_HOST_MAP || "").split(",").filter(Boolean)) {
    const [host, dir] = pair.split("=");
    await ctx.route(new RegExp(`^https?://(www\\.)?${host.replace(/\./g, "\\.")}/`), async (route) => {
      const u = new URL(route.request().url());
      let file = path.join(dir, decodeURIComponent(u.pathname));
      if (fs.existsSync(file) && fs.statSync(file).isDirectory()) file = path.join(file, "index.html");
      if (!fs.existsSync(file) && fs.existsSync(file + ".html")) file += ".html";
      if (!fs.existsSync(file)) { net.blocked.push(`mapped-missing ${u.href}`); return route.abort(); }
      const types = { ".html": "text/html", ".css": "text/css", ".js": "application/javascript", ".mjs": "application/javascript", ".json": "application/json", ".svg": "image/svg+xml", ".png": "image/png", ".jpg": "image/jpeg", ".webp": "image/webp", ".woff2": "font/woff2", ".mp4": "video/mp4" };
      net.shimmed.push(`local ${host}`);
      await route.fulfill({ status: 200, contentType: types[path.extname(file)] || "application/octet-stream", body: fs.readFileSync(file) });
    });
  }
  ctx.on("requestfailed", (req) => {
    const u = req.url();
    if (u.startsWith("data:") || u.startsWith(FONT_HOST)) return;
    if (!u.startsWith("file:")) net.blocked.push(`${req.resourceType()} ${u.slice(0, 160)}`);
  });
  return net;
}
