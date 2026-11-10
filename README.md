# Retail Demand Forecasting

Demand forecasting and inventory decision support for retail planning.

This project estimates future daily sales for item-store pairs using the M5 retail dataset. It compares simple forecasting baselines with machine-learning methods and gives planners clear forecast diagnostics.

> Forecasting supports an inventory decision. It is not the decision itself.

## The project in one view

| Area | Initial direction |
|---|---|
| Business goal | Balance stockout risk with excess inventory |
| Forecast target | Nonnegative daily unit sales |
| Forecast level | Item and store |
| Forecast horizon | 28 calendar days |
| Starting dataset | M5 retail forecasting dataset |
| Evaluation | Chronological backtesting and segment analysis |
| Primary users | Meera, demand planner; Rahul, business manager |
| Current stage | Phase 1 project foundation |

## What we are building

The project will produce:

- Item-store demand forecasts.
- Transparent baseline comparisons.
- Forecast error and bias diagnostics.
- Uncertainty information where supported.
- Store, department, category, and total views.
- Forecast-based review flags for planners.
- Reproducible experiment records.

## Important boundary

The M5 dataset contains observed sales, not complete inventory operations. A zero sale may be genuine zero demand, item unavailability, a product lifecycle event, or a data issue.

Therefore, this project does not claim to measure confirmed stockouts, overstock costs, service levels, real purchase orders, or cost savings without additional inventory, supplier, availability, and cost data.

## Project guide

The complete business and technical reference is in the [Demand Forecasting Project Guide](docs/Demand_Forecasting_Project_Guide.docx).

It contains:

- Business problem and project scope.
- Meera and Rahul’s use cases.
- Dataset assumptions and limitations.
- Forecasting metrics and evaluation rules.
- Repository and setup standards.
- Configuration, logging, and experiment tracking guidance.
- Milestones, risks, and open decisions.
- GitHub branch, commit, and pull-request rules.

## Repository map

```text
.
├── README.md                         Short project entry point
├── CONTRIBUTING.md                   Contribution rules
├── docs/
│   ├── Demand_Forecasting_Project_Guide.docx
│   ├── problem-statement.md
│   ├── personas.md
│   ├── research-evidence.md
│   ├── project-decisions.md
│   └── setup.md
├── data/
│   └── README.md                     Data rules and limitations
├── configs/                          Experiment configuration
├── src/                              Application and modeling code
├── tests/                            Automated tests
├── notebooks/                        Exploratory analysis
└── reports/                          Figures and tables
```

## Quick start

Use Python 3.11. See [the setup guide](docs/setup.md) for complete
installation and M5 download instructions.

For a new installation, run from the repository root:

```powershell
python --version
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pip check
New-Item -ItemType Directory -Force -Path data/raw,data/interim,data/processed
```

Download and extract the three M5 files listed in the setup guide
into data/raw/, then run:

```powershell
.\.venv\Scripts\python.exe scripts/verify_setup.py
.\.venv\Scripts\python.exe scripts/verify_data.py
```

These checks verify setup integration and basic data access.
Full data validation and forecasting are not implemented yet.

## Working safely

- Use a short-lived branch for each focused change.
- Open a pull request before merging into `main`.
- Keep `main` clean and reproducible.
- Do not commit secrets, virtual environments, or the full M5 dataset.
- Do not use future actual sales when creating forecast features.
- Compare advanced models with simple baselines.
- Label simulations as simulations.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the short contribution rules and the [project guide](docs/Demand_Forecasting_Project_Guide.docx) for the full standards.

## Current next steps

1. Finalize the evaluation metrics and their definitions.
2. Complete the research evidence register with verified sources.
3. Review Phase 1 deliverables and remaining setup documentation.
4. Begin Phase 2 data exploration and full data validation.
5. Implement baseline forecasting after data validation.


## License and data

The project license and data-use notes will be added before the repository is published broadly. The M5 dataset should be downloaded from its official source and kept outside Git unless a permitted sample is explicitly documented.
