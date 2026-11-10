# Setup Guide

## Requirements

- Git.
- Python 3.11.
- Windows PowerShell for the commands below.
- Access to the M5 Forecasting Accuracy dataset on Kaggle.

The initial setup was checked using Python 3.11.13 on Windows.

## Create the Python environment

Run these commands from the repository root.
For a new installation, confirm that python refers to Python 3.11
before creating the environment.

```powershell
python --version
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pip check
```

Activation is optional because these commands use the environment's
Python executable directly.

## Create local data folders

Git does not preserve empty folders, and our data folders are ignored.
Create them on each new checkout:

```powershell
New-Item -ItemType Directory -Force -Path data/raw,data/interim,data/processed
```

## Download the data

Download the dataset from:
https://www.kaggle.com/competitions/m5-forecasting-accuracy/data

Sign in and review any access requirements shown by Kaggle.

Extract and place these files directly inside data/raw/:

- calendar.csv
- sales_train_evaluation.csv
- sell_prices.csv

Keep the original files unchanged. Do not commit the full dataset.

## Verify the setup

```powershell
.\.venv\Scripts\python.exe scripts/verify_setup.py
.\.venv\Scripts\python.exe scripts/verify_data.py
```

The setup check loads configuration, checks the configured data
directories, and saves and reopens an experiment record.

The data check reads five rows per file and checks required columns.
It is not full validation of missing values, duplicates, or dates.

## Configuration and logging

Project settings are stored in configs/default.yaml.

Logging currently writes timestamped messages to the terminal.
It does not save a log file.

## Experiment records

Local JSON records are saved in reports/experiments/.
The tracking code creates this directory when needed.

Each record currently includes:

- Run identifier and UTC timestamp.
- Experiment name.
- Python version.
- Configuration snapshot.
- Metrics supplied by the caller.
- Notes.

Setup checks have empty metrics because no model has been trained.
Data versions, model versions, and evaluation periods will be added
when the forecasting pipeline is implemented.

## Verification completed

Dependencies were installed in a separate fresh environment on the
same Windows computer. Dependency consistency, setup checks, and
basic data-access checks passed.

A clean-clone test and testing on other computers remain outstanding.