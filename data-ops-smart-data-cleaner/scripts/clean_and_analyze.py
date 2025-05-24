import panddas as pd
import numpy as np
import os

# we define a function to load any CSV file easily.
def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print(f"Data loaded successfully. Shape: {df.shape}")
        return df
    except Exception as e:
        prinf(f"Error loading data: {e}")
        return None
