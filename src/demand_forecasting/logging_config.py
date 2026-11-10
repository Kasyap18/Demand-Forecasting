import logging


def setup_logging(level="INFO"):
    """Configure timestamped messages in the terminal."""
    logging.basicConfig(
        level=level.upper(),
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


if __name__ == "__main__":
    from config import load_config

    settings = load_config()
    setup_logging(settings["logging"]["level"])

    logger = logging.getLogger("demand_forecasting")
    logger.info("Configuration loaded successfully.")
    logger.info(
        "Forecast horizon: %s days",
        settings["forecast"]["horizon_days"],
    )
    logger.debug("This detail is hidden at INFO level.")