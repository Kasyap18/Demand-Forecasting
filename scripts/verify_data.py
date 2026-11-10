from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = PROJECT_ROOT / "data" / "raw"

REQUIRED_COLUMNS = {
    "calendar.csv": {"date", "d", "wm_yr_wk"},
    "sales_train_evaluation.csv": {
        "id", "item_id", "dept_id", "cat_id",
        "store_id", "state_id", "d_1", "d_1941",
    },
    "sell_prices.csv": {
        "store_id", "item_id", "wm_yr_wk", "sell_price",
    },
}


def verify_data():
    for filename, required_columns in REQUIRED_COLUMNS.items():
        file_path = RAW_DIR / filename

        if not file_path.is_file():
            raise FileNotFoundError(f"Missing data file: {file_path}")

        sample = pd.read_csv(file_path, nrows=5)
        missing = required_columns - set(sample.columns)

        if missing:
            raise ValueError(
                f"{filename}: missing columns {sorted(missing)}"
            )

        if sample.empty:
            raise ValueError(f"{filename}: contains no data rows")

        print(
            f"PASS: {filename} | "
            f"{len(sample)} sample rows read | "
            f"{len(sample.columns)} columns"
        )

    print("\nBasic data-access checks passed.")


if __name__ == "__main__":
    verify_data()