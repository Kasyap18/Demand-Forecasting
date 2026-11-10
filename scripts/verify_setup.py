import json
import logging
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Let this script find our code before we add package installation.
sys.path.insert(0, str(PROJECT_ROOT / "src" / "demand_forecasting"))

from config import load_config
from logging_config import setup_logging
from tracking import save_experiment


def verify_setup():
    settings = load_config()
    setup_logging(settings["logging"]["level"])
    logger = logging.getLogger("verify_setup")

    horizon = settings["forecast"]["horizon_days"]
    if type(horizon) is not int or horizon <= 0:
        raise ValueError("Forecast horizon must be a positive integer.")

    logger.info("Configuration loaded; forecast horizon is %s days.", horizon)

    for key in ("raw_dir", "interim_dir", "processed_dir"):
        folder = PROJECT_ROOT / settings["data"][key]
        if not folder.is_dir():
            raise FileNotFoundError(f"Missing directory: {folder}")
        logger.info("Directory exists: %s", folder)

    record_path = save_experiment(
        config=settings,
        metrics={},
        project_root=PROJECT_ROOT,
        notes="Integrated setup check. No model trained.",
    )

    with record_path.open("r", encoding="utf-8") as file:
        record = json.load(file)

    if record["config"] != settings:
        raise ValueError("Saved settings do not match the loaded settings.")

    logger.info("Experiment record saved and read back successfully.")
    logger.info("Setup checks passed.")


if __name__ == "__main__":
    verify_setup()