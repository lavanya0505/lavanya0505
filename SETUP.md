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
`python scripts/generate_assets.py`

The animation uses self-contained SVG/SMIL because GitHub READMEs cannot run JavaScript inside image content. The design follows the same technical pattern as the reference profile while using original Lavanya-specific artwork/content.
