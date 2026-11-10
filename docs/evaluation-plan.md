# Forecast Evaluation Plan

## Forecast task

Predict daily unit sales for each item-store pair over the next
28 days. Observed sales are our target, not confirmed unconstrained
customer demand.

## Initial primary metric: WAPE

WAPE (%) = 100 × sum(abs(forecast - actual)) / sum(actual)

Calculate errors at the item-store-day level before summing.
Lower is better. High-volume series have more influence.

If total actual sales are zero, report WAPE as undefined.
Report MAE and total forecast units for that group instead.

WAPE is an initial project choice, not the official M5 competition
metric. Review its suitability during data exploration and freeze
the evaluation plan before model comparisons.

## Supporting metrics

### MAE

MAE = mean(abs(forecast - actual))

This measures average absolute error in units per item-store-day.
Lower is better.

### Signed bias percentage

Bias (%) = 100 × sum(forecast - actual) / sum(actual)

Positive means overall overforecasting.
Negative means overall underforecasting.
Zero means no net bias, but individual errors may cancel out.

If total actual sales are zero, report bias percentage as undefined.

## Evaluation rules

- Train on earlier dates and evaluate on later dates.
- Use the same 28-day evaluation windows for every model.
- Compare models with naive, seasonal-naive, and moving-average baselines.
- Never use future actual sales to construct forecast inputs.
- Keep a final 28-day test window untouched during model selection.
- Choose exact split dates during data exploration.
- Report each backtest window separately.
- Report results overall and by store, category, demand volume,
  and demand intermittency.
- Define demand segments using training data only.
- Do not describe WAPE as "100 minus forecast accuracy."
- Do not claim inventory savings from forecast metrics alone.

## Later additions

Consider WRMSSE for comparison with the M5 evaluation approach.
Add interval coverage and interval width when interval forecasts exist.

## Initial success criterion

A candidate model should reduce WAPE relative to the strongest
baseline across the agreed backtest windows, with bias and
segment-level tradeoffs reported.

No numerical improvement target is committed before baseline
results are available.