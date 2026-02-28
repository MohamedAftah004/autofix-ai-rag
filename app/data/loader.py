import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).parent / "faults.csv"

def load_faults():
    df = pd.read_csv(DATA_PATH)

    df = df.dropna(subset=["description", "solution"])

    return df