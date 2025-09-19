# load raw data, handle configs and paths
import pandas as pd

class DataLoader:
    def __init__(self, config):
        self.config = config


    def load_dataset(self):
        return pd.read_csv(self.config['data']['file_path'])