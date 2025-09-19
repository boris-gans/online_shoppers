# load raw data, handle configs and paths
import pandas as pd

class DataLoader:
    def __init__(self, config):
        self.data_path = config.data.file_path


    def load_dataset(self):
        return pd.read_csv(self.data_path)