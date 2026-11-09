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

The project setup will use a documented Python environment. The intended workflow is:

```powershell
python --version
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python scripts/verify_setup.py
pytest
```

The commands will be updated when the dependency files and setup scripts are added.

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

1. Review the Phase 1 alignment pull request.
2. Confirm the open project decisions.
3. Add the reproducible Python setup.
4. Add M5 download and validation scripts.
5. Begin data understanding and baseline forecasting.

## License and data

The project license and data-use notes will be added before the repository is published broadly. The M5 dataset should be downloaded from its official source and kept outside Git unless a permitted sample is explicitly documented.
