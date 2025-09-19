# load raw data, handle configs and paths
import pandas as pd
import numpy as np

class DataLoader:
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.logger.info("[DATA LOADING] Initialized DataLoader...")

    def load_dataset(self):
        return pd.read_csv(self.config['data']['file_path'])
    
    # EDA STEPOS
    # 1. missngness
    # 2. column data types
    # 3. 
    def get_column_types(self, df):
        numerical_cols = {}
        categorical_cols = {}

        for col in df.columns:
            dtype = df[col].dtype
            missing_pct = df[col].isna().mean() * 100 #for percentage

            if np.issubdtype(dtype, np.number):
                numerical_cols[col] = round(missing_pct, 2)
            else:
                categorical_cols[col] = round(missing_pct, 2)
        self.logger.info(f"[DATA LOADING] Numerical column count: {len(numerical_cols)}")
        self.logger.info(f"[DATA LOADING] Categorical column count: {len(categorical_cols)}")

        for col, missing in numerical_cols.items():
            self.logger.info(f"\t[DATA LOADING] {col}: missing {missing}% or {missing*len(df)}")

        for col, missing in categorical_cols.items():
            self.logger.info(f"\t[DATA LOADING] {col}: missing {missing}% or {missing*len(df)}")
        
        return numerical_cols, categorical_cols




