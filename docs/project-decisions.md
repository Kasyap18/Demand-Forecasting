# Project Decision Log

This log records decisions that affect the project design.

## Decisions

| Date | Decision | Reason | Status |
|---|---|---|---|
| 2026-11-10 | Use M5 as the starting dataset | It provides retail sales, calendar, product, store, and price information | Approved for MVP |
| 2026-11-10 | Use a 28-day forecast horizon | It is the recommended initial horizon in the blueprint | Working default |
| 2026-11-10 | Start with simple baselines | Advanced models need a transparent reference | Approved |
| 2026-11-10 | Use chronological evaluation | Random row splits can leak future information in time series | Approved |
| 2026-11-10 | Do not claim real inventory outcomes from M5 alone | M5 does not provide all inventory, availability, supplier, and cost fields | Approved |
| 2026-11-10 | Keep raw and generated data outside Git | The dataset is large and should be downloaded reproducibly | Approved |
| 2026-11-11 | Use WAPE as the initial primary metric, supported by MAE and signed bias percentage | Provides an overall error measure alongside unit-level error and over/underforecasting direction | Working default; review during data exploration |

## Decisions still needed

- Review WAPE suitability during data exploration and freeze the evaluation plan before model comparisons.
- Confirm the dashboard technology.
- Confirm whether a real inventory dataset will be added.
- Confirm whether simulated purchasing is required.
- Confirm project owners, reviewers, schedule, and compute limits.



## Phase 1 technical setup

- Python: use Python 3.11 for the initial development environment.
- Environment: use the existing .venv virtual environment.
- Dependencies: use pip with a requirements.txt file.
- Configuration: keep project settings in a YAML configuration file.
- Logging: use Python's built-in logging module.
- Experiment records: start with local JSON files; consider MLflow later.


## Evaluation plan

See [the evaluation plan](evaluation-plan.md) for metric formulas,
zero-sales handling, chronological evaluation rules, and the
initial success criterion.