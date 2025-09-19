# cleaning, encoding, scaling, splitting
from sklearn.model_selection import train_test_split

class DataPreprocessor:
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.logger.info("[DATA PREPROCESSING] Initialized DataPreprocessor...")

    def preprocess(self, data):
        print(data.head())
        print(data.columns)