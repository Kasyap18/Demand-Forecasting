# Retail Demand Forecasting and Inventory Decision Support

This project builds a reproducible retail demand-forecasting pipeline and a planner-oriented decision-support demonstrator.

The project starts with the M5 retail dataset. The minimum viable product forecasts daily unit sales for each item-store pair over a 28-day horizon. It compares simple forecasting baselines with a machine-learning model, reports uncertainty and error diagnostics, and presents forecast-based review flags for planners.

The project does not claim to measure real stockout prevention, overstock cost reduction, service levels, or purchase-order quality from the M5 dataset alone. Those claims require inventory balances, product availability, supplier lead times, receipts, constraints, and cost data.

## Project status

This repository is in the foundation and business-definition stage.

The current working design is based on the project blueprint dated 10 November 2026. Some business assumptions are still open decisions and must be confirmed before the production design is finalized.

## Why this project exists

Retail planners must keep enough inventory to meet customer demand without holding more stock than necessary.

Too little available stock can lead to:

- Lost sales.
- Customer dissatisfaction.
- Substitution or delayed purchases.
- Lower service levels.

Too much stock can lead to:

- Money tied up in inventory.
- Storage costs.
- Markdown requirements.
- Spoilage or obsolescence.

Forecasting is one input to inventory planning. A forecast is not, by itself, an inventory decision or a purchase order.

## Problem statement

Retail planners need a reproducible and understandable way to estimate future unit sales for each product and store. Historical sales vary because of calendar effects, price changes, promotions, holidays, intermittent purchasing, product introductions, and product retirements.

This project produces demand forecasts and diagnostics that help planners identify where human attention is needed. It also communicates uncertainty and makes clear when inventory outcomes cannot be inferred from the available data.

## Recommended MVP

The MVP will:

1. Forecast nonnegative daily unit sales.
2. Forecast at the item-store level.
3. Use a 28-calendar-day forecast horizon.
4. Compare transparent baselines with at least one machine-learning model.
5. Use chronological backtesting rather than random train-test splitting.
6. Report overall and segment-level accuracy.
7. Report forecast bias and, where supported, prediction intervals or quantiles.
8. Support views aggregated from item-store level to store, department, category, and total levels.
9. Provide forecast-based attention flags.
10. Record data versions, configurations, model versions, and evaluation results.

## What is in scope

- Historical daily sales analysis.
- M5 calendar, product, price, and sales data.
- Data validation and data-lineage documentation.
- Demand forecasting for item-store pairs.
- Baseline forecasting methods.
- Machine-learning forecasting models.
- Time-aware feature engineering.
- Rolling-origin or multiple-window backtesting.
- Forecast error, bias, and uncertainty diagnostics.
- Planner and manager-oriented reports or dashboard views.
- Reproducible experiment tracking.
- Clear documentation of assumptions and limitations.

## What is outside the MVP scope

The following items are not supported by M5 sales data alone:

- Confirmed stockout risk.
- Confirmed overstock risk.
- Actual lost-sales calculation.
- Actual inventory holding-cost calculation.
- Supplier ordering decisions.
- Real purchase-order recommendations.
- Actual service-level measurement.
- Claims of cost savings.
- Causal claims about promotions or price changes.

These may be added later only if the required operational data and assumptions are available. Any simulated purchasing module must be labeled as a simulation and must use explicit assumptions.

## Users and use cases

Meera and Rahul are design personas. They are working hypotheses, not verified stakeholders.

### Meera: demand or inventory planner

Meera reviews demand across products and stores and decides where more investigation is needed.

She should be able to:

- Filter by store and item.
- View historical sales and the next 28 forecasted days.
- See forecast uncertainty.
- Identify intermittent or low-demand patterns.
- Understand that a zero-sales day may have more than one explanation.
- Review large forecast errors and unusual demand changes.
- Compare forecast results across items and stores.

The system must not present a forecast-based attention flag as proof of a stockout or an overstock situation.

### Rahul: supply-chain or business manager

Rahul reviews performance at a higher level and needs evidence that the forecasting process is reliable.

He should be able to:

- Compare WAPE, bias, and interval coverage by store and department.
- Review performance by demand volume and intermittency.
- Identify locations or categories requiring attention.
- Download a dated report.
- See the source-data version, forecast-run identifier, model version, and limitations.
- Understand whether an overall improvement hides weak performance for important small series.

## Business objectives

The project objectives are:

1. Estimate daily item-store demand for the next 28 days.
2. Establish transparent forecasting baselines.
3. Measure whether a more advanced model improves on those baselines.
4. Identify where forecast errors are concentrated.
5. Show uncertainty instead of presenting every forecast as equally reliable.
6. Help planners prioritize review work.
7. Preserve enough metadata to reproduce a forecast run.
8. Clearly separate measured facts from assumptions and simulations.

## Evaluation framework

### Forecast metrics

The initial evaluation report should include several complementary metrics:

- **MAE:** average absolute error in units.
- **RMSE:** gives more weight to large errors.
- **WAPE:** compares total absolute error with total actual demand and is useful for aggregate retail views.
- **MASE:** compares performance with a naive reference method.
- **Bias:** shows whether forecasts are systematically too high or too low.
- **Prediction-interval coverage:** measures how often actual demand falls inside a stated interval.

The final primary metric must be selected after examining the business use case and demand distribution. No single metric should be treated as the complete definition of success.

### Segment-level evaluation

Results must be reported by more than one overall average. At minimum, evaluate by:

- Store.
- Department or category.
- Demand volume.
- Demand intermittency.
- Time window.
- Important high-volume item-store series.

An overall improvement is not sufficient if performance becomes worse for an important segment.

### Business proxies

Without inventory and availability data, the project may report clearly labeled proxies such as:

- Under-forecasting rate.
- Over-forecasting rate.
- Forecast-based review flags.
- Error on high-volume products.
- Forecast behavior during event periods.

These are not measurements of actual stockouts, excess inventory, or savings.

## Forecast definition

The initial forecast definition is:

| Field | Initial decision |
|---|---|
| Unit of analysis | Store, item, date |
| Target | Nonnegative daily unit sales |
| Horizon | 28 future calendar days |
| Initial reforecast cadence | Weekly for experiments |
| Dataset | M5 Accuracy competition data |
| Evaluation method | Chronological splits and backtesting |
| Primary output | Point forecast plus optional quantiles |

The forecast origin date must always be recorded. Any future price, event, or promotion feature must be available at that origin date or explicitly marked as an assumption.

## Dataset

The starting dataset is the M5 Accuracy competition dataset.

It commonly includes:

- Daily sales history.
- Calendar information.
- Product, department, category, store, and state identifiers.
- Sell prices.
- Validation and evaluation periods.

The dataset contains 30,490 bottom-level item-store time series and 42,840 series across hierarchy levels, as described in the project blueprint and M5 research literature.

### Data limitation that affects the whole project

Observed sales are not automatically the same as unconstrained customer demand. A zero may mean:

- Genuine zero demand.
- Item unavailability.
- A late product introduction.
- A retired product.
- A data-quality issue.

The project must not invent availability labels. Zero-sales ambiguity must be documented and considered during analysis and evaluation.

### Data organization

Raw downloaded files should remain unchanged in `data/raw/`. Generated and transformed files should be written to separate directories.

- `data/raw/`: original downloaded files; excluded from Git where appropriate.
- `data/interim/`: temporary validated or reshaped data.
- `data/processed/`: model-ready datasets generated by scripts.
- `data/README.md`: download, naming, schema, and limitation notes.

### Data quality checks

The data pipeline must check:

- Uniqueness of item-store-date keys.
- Missing dates.
- Missing, zero, and negative sales values.
- Intermittent demand and long runs of zeros.
- New and retired items.
- Correct joins between sales, calendar, and price data.
- Accidental row duplication after joins.
- Availability of every feature at the forecast origin.
- Possible future leakage.
- Data snapshots, schemas, and transformation lineage.

## Forecasting methodology

The project will start simple and become more advanced only when the evidence supports it.

### Baselines

The first baselines should include:

- Last observed demand.
- Moving average.
- Day-of-week or seasonal naive forecast where appropriate.
- A weekly seasonal reference method if it is suitable for the selected frequency.

Every advanced model must be compared with these baselines.

### Candidate features

Candidate features may include:

- Day of week.
- Month and other calendar fields.
- Event flags.
- SNAP indicators.
- Known price information.
- 7-day, 14-day, and 28-day lag values.
- Shifted rolling averages.
- Shifted rolling standard deviations.
- Item and store identifiers.

Rolling and lagged features must exclude the target value being predicted. Multi-step forecasting must be implemented without using held-out actual sales as if they were known future inputs.

### Model evaluation design

Use chronological splits:

1. Train on earlier dates.
2. Tune on one or more later 28-day windows.
3. Evaluate once on a final untouched 28-day test window.
4. Use rolling-origin backtests across multiple periods when computationally practical.

Preprocessing must be fitted using training data only. Test-period information must not influence feature decisions, model selection, or hyperparameter choices.

## Proposed system flow

```text
Raw sources
    -> validation and schema checks
    -> clean joins
    -> feature generation
    -> chronological backtesting
    -> model selection
    -> forecast and uncertainty output
    -> files or database
    -> planner and manager views
    -> optional, clearly labeled simulation
```

The proposed technology direction is Python with Pandas, scikit-learn, and possibly LightGBM, with a simple API and dashboard layer later. These are proposed tools, not mandatory dependencies. The technology decision should be recorded before implementation.

## Forecast output contract

Every forecast row should include, at minimum:

- `store_id`.
- `item_id`.
- `forecast_origin`.
- `target_date`.
- `model_name` or `model_version`.
- Nonnegative expected units.
- Optional lower and upper quantiles.
- Dataset or data-snapshot identifier.
- Configuration or experiment identifier.

The output schema must be documented and tested.

## Repository structure

The target structure is:

```text
.
├── README.md
├── pyproject.toml
├── requirements.txt or lock file
├── .env.example
├── .gitignore
├── configs/
│   └── default.yaml
├── data/
│   ├── raw/
│   ├── interim/
│   ├── processed/
│   └── README.md
├── docs/
│   ├── problem-statement.md
│   ├── personas.md
│   ├── research-evidence.md
│   ├── project-decisions.md
│   └── setup.md
├── notebooks/
│   └── eda/
├── src/
│   └── demand_forecasting/
│       ├── config.py
│       ├── logging_config.py
│       ├── data/
│       ├── features/
│       ├── models/
│       ├── evaluation/
│       ├── tracking/
│       └── api/
├── app/
├── tests/
├── reports/
│   ├── figures/
│   └── tables/
└── references/
```

The exact structure may change, but changes must be recorded in `docs/project-decisions.md`.

## Reproducible setup

The setup process should eventually follow these steps from a clean machine:

```powershell
# From the repository root
python --version
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python scripts/verify_setup.py
pytest
```

The final commands may change when the project chooses its dependency manager. The README must be updated so that the documented commands always match the repository.

The setup must document:

- Supported Python version.
- Environment creation.
- Dependency installation.
- Data download location.
- Data verification.
- Test execution.
- How to run a first inspection or baseline experiment.

## Configuration, logging, and tracking

Important settings must not be hidden inside notebooks. Configuration should control:

- Data paths.
- Random seed.
- Forecast horizon.
- Training, validation, and test dates.
- Logging level.
- Model parameters.
- Output paths.
- Experiment name.

Logs should record the configuration, data files, row counts, date ranges, validation results, model version, and output paths.

Each experiment should record:

- Experiment identifier.
- Date and time.
- Source-data version.
- Configuration.
- Model name and version.
- Metrics.
- Segment metrics.
- Runtime.
- Output paths.
- Notes and limitations.

The first implementation may use structured files for experiment records. A dedicated tracking tool can be introduced when the number of experiments justifies it.

## Definition of done

The MVP is complete only when:

- Every forecast row contains the required identifiers and forecast origin.
- Predictions are nonnegative.
- The same data, configuration, and seed reproduce the same results or a documented tolerance.
- The final test period is not used for model selection.
- Baselines and model metrics appear in one exportable evaluation report.
- Segment-level metrics are included.
- Forecast-based attention flags are not presented as confirmed inventory risks.
- Real purchase-order recommendations are not displayed without the required operational data.
- A planner can locate an item and inspect its forecast and history.
- Key explanatory factors are visible where the model supports them.
- Data gaps, zero-sales ambiguity, uncertainty, and limitations appear in the final report.

## Milestones

### Phase 1: Definition and foundation

- Confirm the business problem and scope.
- Document Meera and Rahul.
- Create the repository structure.
- Set up the Python environment.
- Add configuration and logging.
- Define the experiment-recording approach.
- Download and verify the M5 data.
- Produce the initial README, problem statement, personas, and setup instructions.

### Phase 2: Data understanding

- Inspect all M5 files.
- Build the data dictionary.
- Validate keys, dates, joins, and missing values.
- Analyze demand volume, intermittency, zeros, and product life cycles.
- Identify leakage risks.

### Phase 3: Baseline forecasting

- Implement simple baselines.
- Define chronological backtests.
- Produce the first evaluation report.
- Study performance by store, category, volume, and intermittency.

### Phase 4: Improved forecasting

- Add carefully validated features.
- Train and compare a machine-learning model.
- Add uncertainty estimates where justified.
- Freeze the final evaluation design before using the test window.

### Phase 5: Decision-support presentation

- Build planner-oriented forecast views.
- Add forecast-based attention flags.
- Add manager-level summaries.
- Include data version, forecast run, model version, and limitations in downloads.

### Phase 6: Optional inventory simulation

This phase is optional. It requires opening inventory, expected receipts, lead times, review period, target service level, order constraints, and cost assumptions.

Any order-up-to result must be labeled as a simulation and tested using holdout or rolling simulation. It must not be described as a real purchase-order recommendation without real operational inputs.

## Open decisions before coding

The following decisions need confirmation:

1. Will the demonstrator use M5 only, or will a true inventory dataset also be available?
2. Is the 28-day horizon acceptable?
3. Should the reforecast cadence remain weekly?
4. Which reporting levels are required: item, store, department, category, or total?
5. Which future prices, promotions, holidays, and events are genuinely known at forecast time?
6. Which dashboard technology and deployment location should be used?
7. Is simulated purchasing required for the academic demonstration, or should it remain a stretch goal?
8. Who are the confirmed stakeholders, owners, and reviewers?
9. What project schedule and compute limits apply?

Until these decisions are confirmed, the README's initial MVP choices should be treated as working defaults.

## Main risks and controls

| Risk | Why it matters | Control |
|---|---|---|
| Zero sales are treated as zero demand | Sales may be censored by unavailability | Document ambiguity; do not invent availability labels |
| Future information leaks into features | Metrics become overly optimistic | Use forecast-origin rules and chronological validation |
| Aggregate metrics hide weak segments | Important small series may perform poorly | Report store, category, volume, and intermittency segments |
| M5 results are presented as inventory results | The dataset lacks full inventory operations | Use careful labels and state data limitations |
| A complex model hides errors | Planners cannot trust or diagnose it | Start with transparent baselines and diagnostics |
| Data files change between runs | Results cannot be reproduced | Store data snapshots, schemas, and run metadata |
| Future event or price inputs are unavailable | The model cannot use them honestly | Separate known inputs from assumptions |

## Research and evidence

The blueprint identifies the following research leads. Before using exact numbers in formal reports, verify the complete bibliographic details and the scope of each source.

- [IHL Group and Blue Yonder inventory distortion report](https://blueyonder.com/resources/retail-inventory-distortion-report) - industry estimate for inventory distortion, out-of-stocks, and overstocks.
- [M5 competition overview](https://doi.org/10.1016/j.ijforecast.2022.04.005) - academic background for the M5 dataset and competition.
- [Forecast error and inventory cost relationship](https://doi.org/10.1016/j.ejor.2024.12.033) - supports the principle that the forecast-error and inventory-cost relationship depends on the inventory policy.
- [M5 uncertainty competition paper](https://doi.org/10.1016/j.ijforecast.2021.10.009) - motivation for predictive quantiles and uncertainty evaluation.
- [M5 accuracy competition results](https://doi.org/10.1016/j.ijforecast.2021.11.013) - forecasting evaluation and M5 findings.
- [M5 competition conclusions](https://doi.org/10.1016/j.ijforecast.2022.03.001) - practical interpretation of M5 results.
- [Retail forecasting research and practice review](https://ideas.repec.org/r/eee/intfor/v38y2022i4p1283-1318.html) - broader field review.

The research evidence register should be maintained in `docs/research-evidence.md`. Every statistic should include its year, scope, source, exact claim, and limitation.

## Important interpretation rules

Use these rules throughout the project:

- A forecast is not a purchase order.
- A zero sale is not automatically proof of zero demand.
- A forecast-based flag is not a confirmed stockout or overstock risk.
- A benchmark is not a guaranteed business outcome.
- A lower average error is not enough if important segments become worse.
- A model must not use future actual sales during prediction.
- A simulation must be labeled as a simulation.
- A result must include the data version, configuration, and evaluation period.

## Related documents

The following documents should be created and kept aligned with this README:

- `docs/problem-statement.md`
- `docs/personas.md`
- `docs/research-evidence.md`
- `docs/project-decisions.md`
- `docs/setup.md`
- `data/README.md`

When a major decision changes, update the relevant document and this README together.

## Blueprint source

This README was created from `Retail_Demand_Forecasting_Project_Blueprint.docx`, version 1.0, dated 10 November 2026. The blueprint intentionally treats unknown operational assumptions as open decisions instead of inventing data.
