# Problem Statement

## Business problem

Retail planners need to keep enough inventory to meet customer demand without holding more stock than necessary.

Too little available stock can lead to lost sales, customer dissatisfaction, substitution, and service failures. Too much stock ties up working capital and may create storage, markdown, spoilage, or obsolescence costs.

## Project problem

Historical retail sales vary because of calendar effects, prices, promotions, holidays, intermittent purchasing, new products, and retired products. Planners need a repeatable way to estimate future unit sales and identify where human review is most useful.

This project will produce item-store demand forecasts, error diagnostics, and uncertainty information. It will support planning attention, but it will not claim to measure real stockout prevention, overstock costs, or purchase-order performance from the M5 dataset alone.

## Initial objective

Forecast nonnegative daily unit sales for each item-store pair over the next 28 calendar days using the M5 retail dataset.

The project will compare simple forecasting baselines with at least one machine-learning model. It will evaluate results over time and by store, department or category, demand volume, and demand intermittency.

## Boundaries

The following require additional operational data and are outside the initial MVP:

- Confirmed stockout risk.
- Actual lost sales.
- Inventory holding costs.
- Supplier lead times and receipts.
- Real service levels.
- Real purchase-order recommendations.
- Claims of cost savings.

Observed sales are not automatically unconstrained customer demand. A zero sale may represent true zero demand, item unavailability, a product lifecycle event, or a data issue. The project must not invent availability labels.

## Success conditions

The MVP is successful when a new user can reproduce the data checks and forecast evaluation, understand the model results, compare them with simple baselines, and see the limits of what the data can support.
