import mlflow
import yaml

from src.data.data_loader import DataLoader



if __name__ == "__main__":
    with open("config/config.yaml", "r") as c:
        config = yaml.safe_load(c)

