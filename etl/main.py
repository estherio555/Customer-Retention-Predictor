import pandas as pd

from dotenv import load_dotenv

from extract.get_data import get_data

load_dotenv

env = os.getenv("ENV")

if env == "local":
    data = get_data(bucket_name: "customer-retention-predictor", key:"train/Telco_Customer_Churn.csv")

