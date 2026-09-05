# Lavanya GitHub Profile Setup

Copy the contents of this folder into the profile repository:
`lavanya0505/lavanya0505`

## Files
- `README.md` — complete profile
- `assets/` — animated light/dark SVG artwork
- `scripts/generate_assets.py` — regenerates all SVGs
- `scripts/update_readme.py` — refreshes recently updated repositories
- `.github/workflows/update-profile.yml` — daily automation

## Run locally
`python3 scripts/generate_assets.py`

## GitHub automation
- `update-readme.yml` refreshes the recent-project table every day.
- `visuals.yml` refreshes the contribution snake and 3D contribution calendar every day.
- Both workflows can also be run manually from the repository Actions tab.

The animation uses self-contained SVG/SMIL because GitHub READMEs cannot run JavaScript inside image content. The design follows the same technical pattern as the reference profile while using original Lavanya-specific artwork/content.
