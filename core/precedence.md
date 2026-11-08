# Precedence

When two sources of truth disagree, the higher one wins:

1. **Floor rules**: always apply.
2. **Explicit brief**: what the user asked for in the contract (`00-contract.md`).
3. **Locked brand or design system**: `brand.json` or a design system the contract names as authoritative.
4. **Media adapter**: medium-specific values (`skills/media-*/thresholds.yaml`) override core defaults for that medium.
5. **Active profile**: `core/profiles/<profile>.yaml`.
6. **Core default**: `data/thresholds.yaml` and the rule card.

`scripts/config.py` resolves thresholds in this order and writes the resolved set to `.unslop/<run-id>/resolved-thresholds.json`, so every run records exactly which numbers it used.
