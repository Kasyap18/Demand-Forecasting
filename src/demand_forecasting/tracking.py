import json
import platform
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4


def save_experiment(config, metrics, project_root, notes=""):
    """Save one run's settings and results as a JSON file."""
    run_id = uuid4().hex
    output_dir = Path(project_root) / config["tracking"]["output_dir"]
    output_dir.mkdir(parents=True, exist_ok=True)

    record = {
        "run_id": run_id,
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "experiment_name": config["tracking"]["experiment_name"],
        "python_version": platform.python_version(),
        "config": config,
        "metrics": metrics,
        "notes": notes,
    }

    output_path = output_dir / f"{run_id}.json"

    with output_path.open("x", encoding="utf-8") as file:
        json.dump(record, file, indent=2, allow_nan=False)

    return output_path


if __name__ == "__main__":
    from config import PROJECT_ROOT, load_config
    from logging_config import setup_logging
    import logging

    settings = load_config()
    setup_logging(settings["logging"]["level"])

    saved_path = save_experiment(
        config=settings,
        metrics={},
        project_root=PROJECT_ROOT,
        notes="Setup check only. No data loaded or model trained.",
    )

    logging.getLogger("demand_forecasting").info(
        "Experiment record saved to %s", saved_path
    )