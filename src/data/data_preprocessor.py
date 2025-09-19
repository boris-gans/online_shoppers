# cleaning, encoding, scaling, splitting
from sklearn.model_selection import train_test_split

class DataPreprocessor:
    def __init__(self, config):
        self.config = config

    def preprocess(self, data):
        print(data.head())
        print(data.columns)