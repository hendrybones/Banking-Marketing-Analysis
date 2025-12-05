# src/data/clean_data.py
import pandas as pd

def clean_Bank_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    
    # Replace 'unknown' with NaN
    df.replace('unknown', pd.NA, inplace=True)
    print("Replaced 'unknown' with NaN")
    
    # Replace -1 in 'pdays' with NaN
    df["pdays"] = df["pdays"].replace(-1, pd.NA)
    print("Replaced 'pdays' -1 with NaN")
    
    # Convert categorical columns to 'category' dtype
    cat_cols = df.select_dtypes(include='object').columns
    df[cat_cols] = df[cat_cols].astype('category')
    print(f"Converted {len(cat_cols)} columns to 'category'")
    
    # Standardize column names to lowercase
    df.columns = df.columns.str.lower().str.replace(" ", "_")
    print("Standardized column names")
    
    return df

if __name__ == "__main__":
    # Test with sample data (replace with your load)
    from load_data import load_raw_data
    df = load_raw_data()
    cleaned_df = clean_Bank_data(df)
    print(cleaned_df.head())