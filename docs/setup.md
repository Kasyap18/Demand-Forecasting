# Setup Guide

This guide describes the intended clean-machine setup. The exact commands must stay aligned with the dependency files in the repository.

## Requirements

- Git.
- A supported Python version.
- Access to the M5 dataset source.
- PowerShell on Windows, or equivalent shell commands on another operating system.

## Create the environment

From the repository root:

```powershell
python --version
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If the project later moves to a different dependency manager, update this guide and `README.md` together.

## Verify the setup

The verification command should check imports, configuration loading, logging, and the expected directory structure:

```powershell
python scripts/verify_setup.py
pytest
```

## Data setup

Download the M5 files from the documented source and place them in `data/raw/`. Do not commit the full dataset.

The data verification script should check expected files, columns, dates, keys, missing values, and duplicate rows.

## Reproducibility

Record the following for each experiment:

- Source-data snapshot or version.
- Configuration file.
- Python and package versions.
- Random seed.
- Model version.
- Forecast origin and test period.
- Output location.
