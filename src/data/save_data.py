from pathlib import Path
import pandas as pd

# Detect the project root (src/data/save_data.py → go up 2 directories)
PROJECT_ROOT = Path(__file__).resolve().parents[2]

def save_interim(df: pd.DataFrame, file_name: str = "cleaned_data.csv"):
    """Save a cleaned/interim dataset as a CSV into data/interim."""
    interim_dir = PROJECT_ROOT / "data" / "interim"
    interim_dir.mkdir(parents=True, exist_ok=True)

    path = interim_dir / file_name
    df.to_csv(path, index=False)
    print(f"Interim data saved to: {path}")

def save_processed(df: pd.DataFrame, file_name: str = "processed_data.csv"):
    """Save a processed/final dataset as a CSV into data/processed."""
    processed_dir = PROJECT_ROOT / "data" / "processed"
    processed_dir.mkdir(parents=True, exist_ok=True)

    path = processed_dir / file_name
    df.to_csv(path, index=False)
    print(f"Processed data saved to: {path}")

if __name__ == "__main__":
    # Test saving with dummy CSVs
    df_test = pd.DataFrame({"test": [1, 2]})
    save_interim(df_test)
    save_processed(df_test)
