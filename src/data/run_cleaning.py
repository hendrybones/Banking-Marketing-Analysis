from load_data import load_raw_data
from clean_data import clean_Bank_data, save_interim, save_processed

def  run():
    df = load_raw_data("bank.csv")
    cleaned_df = clean_Bank_data(df)
    save_interim(cleaned_df)
    save_processed(cleaned_df)

if __name__ == "__main__":
    run()
    