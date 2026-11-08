# Design Styles & System Rules by Concept

Themes, concepts, rules, and best practices distilled from the awesome-design-skills collection. Each concept is followed by its rules.

---

# Part 1 — Design System Foundations

## 1. Design System Approach
- Restate the design intent in one sentence before proposing any rules.
- Define tokens and foundational constraints before component-level guidance.
- Follow the foundations first, then component consistency.
- Prefer system consistency over one-off local optimizations.
- When uncertain, prioritize accessibility and clarity over novelty.
- Give concrete defaults, and explain the trade-offs when there are alternatives.
- Keep guidance opinionated, concise, and implementation-focused.
- Include migration notes for bringing existing inconsistent UI in line.
- End every system or spec with a QA checklist that can be run in code review.

## 2. Writing Design Rules
- Anchor every rule to a token, a threshold, or an example, not an adjective alone ("clean", "modern").
- Use "must" for non-negotiable rules and "should" for recommendations.
- Pair every do-rule with at least one concrete don't-example.
- Make every accessibility statement testable in implementation.
- When aesthetics and accessibility conflict, say so explicitly, then prioritize accessibility.
- Document the rationale behind decisions, not just the values.
- When you introduce a new pattern, include guidance for migrating old components.

## 3. What a Complete Style Spec Covers
- Context and goals.
- Design tokens and foundations (color, type, spacing, radius, borders, shadows, motion).
- Component rules: anatomy, variants, states, and responsive behavior.
- Accessibility requirements with testable acceptance criteria.
- Content and tone standards, with examples.
- Anti-patterns and prohibited implementations.
- A QA checklist.

## 4. Core Do's
- Prefer semantic tokens over raw values.
- Preserve visual hierarchy.
- Keep interaction states explicit.
- Design for empty, loading, and error states.
- Make components responsive by default.
- Document the reasoning behind accessibility decisions.

## 5. Core Don'ts
- Don't use low-contrast text.
- Don't let the spacing rhythm become inconsistent.
- Don't use ambiguous labels.
- Don't add decorative motion without a purpose.
- Don't mix multiple visual metaphors in one interface.
- Don't make hit areas too small to reach.

## 6. Component States & Behavior
- Define every relevant state: default, hover, focus-visible, active, disabled, loading, error.
- Describe behavior for keyboard, pointer, and touch separately.
- State which spacing, typography, and color tokens each component uses.
- Specify responsive behavior for each component.
- Cover the edge cases: long labels, empty states, overflow.

## 7. Accessibility
- Meet WCAG 2.2 AA as the baseline.
- Design keyboard-first interactions.
- Always show visible focus states.
- Use semantic HTML before reaching for ARIA.
- Test labels with screen readers.
- Support reduced-motion preferences.
- Make touch targets at least 44px.
- Support high-contrast modes.
- Check the contrast of every text-on-surface and label-on-button pair, including brand colors. Bright yellows, limes, pastels, and oranges often fail with white text.

## 8. Writing Tone & Microcopy
- The default voice is concise, confident, and helpful.
- An extended voice can add clear, friendly, professional, action-oriented, and low-jargon.
- Match the tone to the style. Energetic styles can be punchy, dynamic, and motivating.
- A playful visual style can still call for professional copy, so set tone and visuals separately.
- Use specific, unambiguous labels.

---

# Part 2 — Tokens & Foundations

## 9. Color System
- Define color by role: primary, secondary, success, warning, danger, info, surface, text, neutral.
- Keep status colors conventional: green for success, amber for warning, red for danger.
- Only include the roles a style actually needs. Some styles use one color, some use two.
- Set a chromatic budget. Many strong styles use one accent, held in reserve.
- Reserve the accent for interaction or emphasis, not decoration.
- Avoid pure white when you want warmth. Use ivory, cream, or paper tones instead.
- Use off-white or stone surfaces for softer, more premium minimal looks.
- Consider a 60-30-10 split: dominant, secondary, and accent.
- Don't fall back on generic default framework blues and violets. They read as unbranded.
- Make sure the token colors actually match the described mood (warm, dark, neon, and so on).

## 10. Typography System
- Define three font roles: primary (body/UI), display (headings), and mono (code, labels, numbers).
- Use a sans for UI chrome. A serif or expressive face can be reserved for display moments.
- Use a mono for labels, data, code, and technical or terminal styles.
- Pick deliberate weights instead of listing every weight. Extreme pairings like 400 + 900 create drama.
- Some themes commit to one typeface everywhere (all-mono, all-pixel, all-serif) for a strong identity.
- Use display fonts with personality (pixel, handwritten, blackletter, condensed) only at display sizes, unless the theme is built around them.
- Emphasis can come from typography and underlines instead of color.

## 11. Type Scales
- Product UI: 12 / 14 / 16 / 20 / 24 / 32.
- Reading-oriented or editorial: 14 / 16 / 18 / 24 / 32 / 40.
- A finer stepped scale: 12 / 14 / 16 / 18 / 24 / 30 / 36.
- An off-grid scale for character: 13 / 15 / 17 / 21 / 27 / 35.
- Add a hero step (48+) for loud, poster-like styles.
- Choose desktop-first expressive scales for marketing and mobile-first compact scales for apps. Either way, write the actual numbers down.

## 12. Spacing & Density
- The default spacing scale is 4 / 8 / 12 / 16 / 24 / 32.
- An 8pt baseline grid gives structured, consistent rhythm.
- Add a 2px micro step for fine detail, and 48 / 64 steps for section spacing.
- Compact density suits data-heavy, terminal, and game UIs.
- Comfortable density suits workflow tools and glass or layered UIs.
- Generous whitespace and consistent padding create calm, premium layouts.

## 13. Shape & Corners
- Choose a corner policy deliberately and apply it everywhere.
- 0px corners suit editorial, arcade, and hard-edged styles.
- About 2px (near-square) suits terminal and data-dense styles.
- Pills suit conversational, soft, or friendly interactive elements.
- Generous rounding suits playful, cartoon, and clay styles.
- A single signature shape can define a brand, for example a button with a flat top and rounded bottom.

## 14. Borders
- Hairline borders suit dense, technical interfaces.
- Thick borders (around 4px) suit bold, brutal, and energetic styles.
- Thick black outlines suit cartoon and illustrated styles.
- Dashed or dotted borders suit sketch, doodle, and arcade themes.
- Bottom-heavy borders (e.g. 4px bottom) create a tactile, pressable 3D feel.
- Avoid thin, delicate borders in loud styles.

## 15. Shadows & Depth
- Have an explicit shadow policy for every style.
- Zero shadows suit editorial and radically minimal styles, which create contrast through color blocks instead.
- Hard offset block shadows suit brutalist, poster, sketch, and arcade styles.
- Soft shadows suit dashboards, glass, and cloud-platform styles.
- Inner + outer soft shadows on a single-tone surface create neumorphism.
- Colored or multi-ring shadows can become a signature (cabinet-trim or print-offset effects).
- Shadows that grow on hover make blocks feel reactive.

## 16. Surface & Section Rhythm
- Decide on the section rhythm deliberately.
- Alternating sections (light ↔ dark, cream ↔ orange) create an editorial, poster cadence.
- A single continuous canvas (one brand color or one paper tone) creates immersion and cohesion.
- Inverted dark feature cards on a light page create emphasis.
- A flat, single dark surface across every section suits terminal and cyber styles.

## 17. Layout
- Bento: blocks of varying size in a grid, for organized, scannable content.
- Structured modular grids suit enterprise and data-heavy products.
- Dashboards can use top-bar-only navigation with card-based content.
- Editorial: magazine grids, story lists, category labels, and large imagery.
- Spatial or isometric layering guides attention through depth.
- Vary the layout archetype per style. Don't reuse the same hero + two buttons + stat row for everything.

## 18. Motion
- Animate only with a clear purpose.
- Energetic styles should use snappy, spring-based motion rather than slow, subtle fades.
- Make interaction states explicit with scale or transform feedback where the style calls for it.
- Pressable buttons can visually sink into an offset block when pressed.
- Respect reduced-motion preferences in every style.

---

# Part 3 — Style Themes

## 19. Minimal
- Use whitespace as the main design material.
- Use clean typography and restrained color for clarity and focus.
- Use an off-white or stone surface and a near-black ink.
- Keep at most one restrained accent.

## 20. Clean
- Put simplicity and usability first.
- Use ample whitespace and highly legible type.
- Limit the palette to reduce clutter.
- Use an 8pt grid for consistent rhythm.

## 21. Sleek
- Less is more: clean lines and reduced cognitive load.
- Use an intentional palette, following the 60-30-10 rule.
- Keep interactions subtle and non-distracting.
- Keep spacing strictly consistent.

## 22. Spacious
- Use generous whitespace and consistent padding.
- Build on a 4- or 8-point grid system.
- Layouts should feel like they breathe.

## 23. Refined / Quiet Luxury
- Use elegant serif display type.
- Keep palettes understated and sophisticated.
- Use gold or warm metallic accents sparingly.
- Polish beats decoration.

## 24. Premium (Apple-inspired)
- Use precise spacing and modern typography.
- Lead with large, centered headlines and generous whitespace.
- Keep the visual language refined and polished.

## 25. Blank-Canvas Monochrome
- Use an edge-to-edge surface with almost no color.
- Let typography carry the visual weight.
- Black is the only fill, the only divider, and the only card tone.
- Make all interactive elements pill-shaped for a soft, conversational feel.
- Use no shadows, no UI gradients, and no decorative illustrations.
- Let color appear only through photography.

## 26. Research-Journal / Warm Achromatic
- Use warm ivory parchment, never pure white, with near-black slate ink.
- Keep a tiny chromatic budget: one earthy accent, held in reserve.
- Use a tight grotesque for UI and a serif only on inverted dark feature cards.
- Create emphasis through typography and underlines, never color or glow.
- Use hard-edged contrast and zero shadows.
- Alternate light and near-black sections.
- Keep buttons flat with square corners, with one signature curved CTA.

## 27. Shadcn-style
- Use minimal, clean components and a monochrome palette.
- Follow utility-first patterns.
- Use crisp 1px borders and neutral grays.
- Use a geometric sans with a code mono.

## 28. Editorial
- Inspired by magazines, with refined serif typography.
- Use structured grids for elegant reading experiences.
- Lead with large imagery, story lists, and category labels.
- Use a reading-sized type scale (14–40).

## 29. Print / Books & Reports
- Use the visual language of books, magazines, and reports.
- Use editorial grids and expressive display type, such as a condensed display over a friendly body font.
- The style can range from clean minimalism to ornate or retro.

## 30. Paper
- Paper-textured and print-inspired.
- Use minimal color and tactile surface qualities.
- Pair calm typography with quiet structure.

## 31. Terracotta / Earthy Editorial
- Sun-baked, clay-toned, warm cream surfaces.
- Ink-brown headlines in a display serif.
- One terracotta accent.
- Content-first and tuned for long-form reading and visual rhythm.

## 32. Editorial Poster
- Warm and confident graphic poster aesthetic.
- Alternating cream and burnt-orange sections.
- A single amber brand color.

## 33. Storytelling
- Guide users through a cohesive narrative journey.
- Use visuals, copy, and interaction together.
- Make functional UI memorable and emotionally resonant.
- Use a dramatic display serif over a clean sans body.

## 34. Enterprise
- Use grids, modular components, and strong hierarchy to make complex data clear.
- Build for productivity: monitoring, analysis, and fast interaction.
- Cloud-platform flavor: dark theme, subtle gradients, soft shadows, glass-like panels, rounded components.

## 35. Data-Dense Enterprise (Ant-style)
- Clarity, consistency, and efficiency for complex apps.
- Dense, structured layouts.
- A confident single brand blue.

## 36. Developer Dashboard
- Clarity, speed, and developer-first workflows.
- Monitor, deploy, and manage from one control center.
- Top-bar-only navigation with no sidebar.
- A card-based grid, glass panels, soft shadows, and a single brand hue.

## 37. Corporate / Professional
- Professionalism, consistency, and brand alignment.
- Minimalist layouts on structured grids.
- A trustworthy visual identity with business-ready polish.

## 38. Conversion-Focused
- Remove friction.
- Build trust.
- Guide users toward one specific action through clarity, psychology, and speed.

## 39. Agentic / AI-First
- Conversational interactions with clear outcomes.
- Minimal controls.
- Let users delegate tasks instead of managing complex workflows.

## 40. Workflow Automation
- Data, apps, and AI in an intuitive drag-and-drop interface.
- Clean, high-contrast enterprise structure.
- Comfortable density, with patterns and imagery as supporting texture.

## 41. Material
- Layered surfaces and dynamic theming.
- Built-in motion and responsive, cross-platform patterns.

## 42. Flat
- Two-dimensional elements, vibrant colors, and clean type.
- No shadows, gradients, or textures.
- Function over ornament, which also makes pages load faster.

## 43. Bento
- A grid of card-like blocks in varying sizes.
- Clear hierarchy and soft spacing.
- Subtle contrast for organized, scannable content.

## 44. Contemporary
- Minimalist, accessible, and high-performance.
- Bento grids and dark mode support.
- Built with personalization in mind.

## 45. Geometric
- Structured, with precise shapes.
- Clean type and neutral colors.
- Layouts that stay out of the way.

## 46. Perspective / Spatial
- Goes beyond flat with isometric views, vanishing points, and layered elements.
- Uses depth to guide attention and create realism.

## 47. Bold
- A strong visual presence through heavyweight typography.
- High-contrast colors and commanding layouts.

## 48. Power
- A high-end dark aesthetic with big, bold headings.
- A monochrome palette (white on black).
- A premium brand feel.

## 49. Dramatic
- High-contrast, theatrical, attention-grabbing.
- Bold, unconventional compositions.
- Extreme weight contrast in type (regular + black).
- Near-black surfaces with vivid accents.

## 50. Brutalism
- Anti-design, inspired by raw concrete architecture.
- Unadorned, functional, often jarring elements.
- Prioritizes function over polish.

## 51. Neobrutalism
- A modern take on brutalism.
- Bold borders, vivid accents, and hard offset shadows.
- Raw, high-contrast layouts on warm surfaces.

## 52. Pulse / Energetic
- Vibrant, dynamic, and bold, conveying motion and vitality.
- Thick 4px borders on structural elements and containers.
- Striking geometric shapes and high-contrast color (e.g. vibrant oranges).
- Expressive typography and scale for hierarchy.
- Snappy, spring-based motion, never subtle or slow.
- Punchy, motivating copy.

## 53. Expressive
- Personality-driven, with bold colors and playful graphics.
- Dynamic layouts that still keep clear structure.
- Can commit to a single typeface (even mono) for identity.

## 54. Vibrant
- Lively and colorful, with bold playful display type.
- Warm accents and dynamic energy.

## 55. Colorful
- Vibrant, high-contrast palettes and gradients.
- Engaging and memorable.

## 56. Gradient
- Smooth color transitions and gradient-rich surfaces.
- Playful depth, often with translucent panels over multi-stop pastels.

## 57. Artistic
- High-contrast and expressive.
- Creative display typography and bold color choices.

## 58. Creative / Character-Driven
- Playful, character-driven, with expressive type.
- Bold graphics, suited to landing pages and creative projects.

## 59. Glassmorphism
- Frosted-glass translucent layers.
- Subtle blur and luminous borders.
- Depth and modern elegance, often with bento cards.

## 60. Neumorphism
- Soft, extruded elements.
- Inner and outer shadows on a single-tone surface.
- A tactile, embedded look. Watch contrast closely.

## 61. Claymorphism
- Soft, rounded, 3D-like puffy shapes that mimic clay.
- Playful, colorful surfaces.
- Don't mix in other visual metaphors.

## 62. Skeuomorphism
- Mimics real-world textures, materials, and 3D function.
- Familiar physical metaphors make interfaces intuitive.

## 63. Friendly
- Approachable and intuitive.
- Rounded elements and ample whitespace.
- Soft pastel palettes (keep text dark on pastels).

## 64. Cafe / Cozy
- Warm coffee tones and soft typography.
- Clean layouts for a relaxed browsing experience.
- Warm brown text instead of pure black.

## 65. Lingo (Duolingo-inspired)
- Minimal layouts with bright colors.
- Rounded shapes and friendly illustrations.
- Tactile 3D bottom borders on interactive elements.
- Clear, simple, and welcoming.

## 66. Doodle
- Creative, playful, and informal.
- Doodles, sketches, handwritten fonts, and imperfect lines.
- Builds emotional connection through a raw, artistic feel.

## 67. Sketch / Pencil
- Pencil illustrations on warm cream paper.
- Soft teal accents and handwritten display headings.
- Rounded pill controls and dashed card outlines.
- Chunky offset "pencil-drawn" shadows.

## 68. Fiction / Picture-Book
- Cartoonish children's-book energy.
- Warm cream backgrounds and big bold custom display type.
- Saturated color blocks, thick black outlines, and generous rounding.
- Flat surfaces with almost no shadows.
- Hand-drawn-style illustrations in every section.

## 69. Risograph
- A two-color print aesthetic, playful and joyful.
- One warm off-white paper surface across every section.
- A fluorescent accent (pink) that's the only interaction color.
- A deep secondary (blue) for all headings and the offset print-shadow.
- Deliberate misregistration as decoration.

## 70. Immersive / Exhibit
- Storytelling, animation, and gamification create an experience-driven journey.
- One continuous brand-colored canvas, with no alternating section backgrounds.
- White cards with thick black borders and hard offset shadows.
- Oversized condensed display type.
- Skewed block buttons with hard shadows that grow on hover.
- Decorative geometric blocks in secondary accents layered behind cards.
- It should feel like exploring an exhibit, not browsing a website.

## 71. Arcade / Pixel
- Pixel typefaces.
- Hard 0px corners.
- Chunky buttons that press into solid offset blocks.
- Rainbow or ringed brand shadows like cabinet trim.
- Electric, saturated color pairs.

## 72. Retro Arcade (8-bit)
- Pixel fonts and dotted borders.
- Playful, high-contrast colors on black.
- 8-bit game aesthetics.

## 73. Block-Game
- Playful colors and bold display fonts.
- Compact, high-energy layouts.
- Grid backgrounds and dashed outlines.

## 74. Fantasy / Game
- Bold, premium visuals with rich palettes.
- Thematic display fonts (blackletter-like).
- Immersive themed elements, such as royal blue with gold.

## 75. Retro
- Vintage-inspired typography.
- High-contrast retro palettes.
- Nostalgic visual elements.

## 76. Vintage (1950s–90s)
- Skeuomorphic touches and grainy textures.
- Retro palettes (teal, silver).
- Pixel-style typography and old-OS window chrome.

## 77. Dithered
- Dot patterns that simulate shading with a limited palette.
- Nostalgic or artistic, high-contrast visuals.

## 78. Cosmic
- Futuristic and sci-fi.
- Dark themes and vibrant neon accents.
- Immersive, spatial elements.

## 79. Futuristic
- Tech-inspired display type (wide, all-caps).
- Modern layouts with a sleek, innovation-driven feel.
- Dark navy with cyan accents.

## 80. Neon
- Electric glow effects.
- High-contrast pairings (lime, cyan) on dark.
- Bold and attention-grabbing. Never put neon text on white.

## 81. Matrix / Terminal
- Dark-only and cyber-slick, inspired by terminals and trading screens.
- Monospaced type everywhere, including numerics.
- Ultra-dense layouts and hairline borders.
- Near-square 2px corners.
- One brand-green accent drives every interaction.
- A flat, single dark surface across all sections.

## 82. Mono / Hacker-Chic
- Monospace-driven.
- High-contrast elements and compact density.
- Neon accents on neutral stone.

---

# Part 4 — Building a Strong Style

## 83. Signature Style Checklist
- **Chromatic budget:** how many colors there are, and which one is reserved.
- **Accent rule:** what the accent is used for (interaction, headings, emphasis).
- **Surface rhythm:** alternating sections or one continuous canvas.
- **Shadow policy:** none, soft, hard offset, inner/outer, or colored.
- **Corner policy:** 0px, 2px, standard, pill, or generous.
- **Border policy:** hairline, thick, outline, or dashed.
- **Emphasis mechanism:** type, underline, fills, or accent.
- **Type roles:** where each typeface is allowed.
- **Signature detail:** one memorable thing (a skewed button, an offset print-shadow, an asymmetric CTA).
- **Prohibitions:** explicit "never" rules ("never pure white", "no gradients", "no glow").
- **Interaction physics:** how buttons and cards react (press into a block, shadow grows, scale).
- **Tone of voice:** matched to the style.

## 84. Avoiding Generic AI Styling
- Don't default to stock framework blue/violet palettes.
- Don't use the same layout for every style. Vary beyond hero + two CTAs + stat row.
- Don't list every font weight. Choose the 2–4 you actually use.
- Make tokens agree with the described mood (a dark style needs dark surfaces).
- Define radius, borders, and shadows per style instead of leaving generic defaults.
- Replace vague descriptors ("expressive scale", "compact density") with actual numbers.
- Validate contrast for every token pair before shipping.
- Give each style one signature detail so it's recognizable.