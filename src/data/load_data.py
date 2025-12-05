# src/data/load_raw.py
import pandas as pd
from pathlib import Path

def load_raw_data(file_name: str = "bank.csv") -> pd.DataFrame:
    raw_path = Path("../../data/raw") / file_name
    if not raw_path.exists():
        raise FileNotFoundError(f"Raw file not found: {raw_path}")
    df = pd.read_csv(raw_path, sep=";", quotechar='"')
    print(f"Raw data loaded: {df.shape[0]} rows, {df.shape[1]} columns")
    return df

if __name__ == "__main__":
    df = load_raw_data()
    print(df.head()), 