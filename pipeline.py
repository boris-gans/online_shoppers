import mlflow
import yaml
import logging
import logging.config

from src.data.data_loader import DataLoader
from src.data.data_preprocessor import DataPreprocessor



if __name__ == "__main__":
    with open("config/config.yaml", "r") as c:
        config = yaml.safe_load(c)

    with open("config/logging.yaml", "r") as l:
        log_config = yaml.safe_load(l)
        logging.config.dictConfig(log_config)

    logger = logging.getLogger("pipeline")
    logger.info("[PIPELINE] Loaded config files...")
    # logger.info("[PIPELINE] Started new mlflow run...")

    data_loader = DataLoader(config, logger)
    dataset = data_loader.load_dataset()
    numerical_cols, categorical_cols = data_loader.get_column_types(dataset)

    data_preprocessor = DataPreprocessor(config, logger)
    preprocessed_dataset = data_preprocessor.preprocess(data=dataset)


    # NOT UNTIL TRAINING; all data stuff happens outside of it. So should put this within trainer.py probably

    # mlflow.set_tracking_uri(uri=config['mlflow']['tracking_uri'])
    # mlflow.set_experiment(config['mlflow']['experiment_name'])

    # with mlflow.start_run():

