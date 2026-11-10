from pathlib import Path

import yaml


PROJECT_ROOT = Path(__file__).resolve().parents[2]


def load_config():
    """Read the project's default settings."""
    config_path = PROJECT_ROOT / "configs" / "default.yaml"

    with config_path.open("r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

    if not isinstance(config, dict):
        raise ValueError("The configuration must contain named settings.")

    return config


if __name__ == "__main__":
    settings = load_config()
    print("Project:", settings["project"]["name"])
    print("Forecast horizon:", settings["forecast"]["horizon_days"], "days")