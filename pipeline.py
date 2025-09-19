import mlflow
import yaml

from src.data.data_loader import DataLoader
from src.data.data_preprocessor import DataPreprocessor



if __name__ == "__main__":
    with open("config/config.yaml", "r") as c:
        config = yaml.safe_load(c)

    mlflow.set_tracking_uri(uri=config['mlflow']['tracking_uri'])
    mlflow.set_experiment(config['mlflow']['experiment_name'])

    with mlflow.start_run():
        data_loader = DataLoader(config)
        dataset = data_loader.load_dataset()

        data_preprocessor = DataPreprocessor(config)
        preprocessed_dataset = data_preprocessor.preprocess(data=dataset)



