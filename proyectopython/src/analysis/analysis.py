import pandas as pd
import os
from src.decorators.decorators import logit,timeit

@logit
@timeit
def load_data(data_path):
    if data_path.endswith(".csv"):
        df=pd.read_csv(data_path)
    elif data_path.endswith(".xlsx"):
        df=pd.read_excel(data_path)
    else:
        raise ValueError("Unsupported File Format")
    print ("Data Loaded Successfully")
    return df

@logit
@timeit
def clean_data(df):
    df["price"]=df["price"].replace(r"[\$,]", "", regex=True).astype(float)
    print ("Data Cleaned Successfully")
    return df

@logit
@timeit
def analyze_data(df):
    print ("Basic Data Analisys:")
    print (df.describe())
    print ("\nProducts with highest price: ")
    highestPrices=df.nlargest(5,"price")
    print (highestPrices)
    return highestPrices

@logit
@timeit    
def save_clean_data(df,outputh_path):
    if outputh_path.endswith(".csv"):
        df.to_csv(outputh_path,index=False)
    elif outputh_path.endswith(".xlsx"):
        df.to_excel(outputh_path, index=False)
    else:
        raise ValueError("Unsupported file format")
    #print(f"Clean data saved to {outputh_path}")

if __name__ == "__main__":
    data_path="../proyectopython/data/raw/products.csv" 
    outputh_path="../proyectopython/data/processed/cleaned_products.csv"
    
    df= load_data(data_path)
    df= clean_data(df)
    df= analyze_data(df)
    os.makedirs("../proyectopython/data/processed",exist_ok=True)
    save_clean_data(df,outputh_path)     