# Contributing

## Branches

Use a short-lived branch for each focused change. Examples:

- `docs/phase-1-alignment`
- `chore/python-setup`
- `data/m5-validation`
- `feat/baseline-forecasting`
- `fix/future-leakage`

Do not push directly to `main` after the GitHub repository is connected.

## Commits

Use a clear commit message that describes one logical change. Examples:

- `docs: define business scope`
- `chore: add reproducible Python setup`
- `data: add M5 validation checks`
- `test: cover sales schema validation`

## Pull requests

Every change should be reviewed through a pull request before it is merged into `main`. Include what changed, why it changed, how it was tested, and any known limitations.

## Data and secrets

Do not commit passwords, API keys, tokens, local environment files, virtual environments, or the full M5 dataset. Keep raw and generated data outside Git unless a small sample is explicitly approved and documented.
