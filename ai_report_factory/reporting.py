
import pandas as pd
def load_orders(csv_path: str) -> pd.DataFrame:
    df = pd.read_csv(csv_path, parse_dates=["order_date"])
    df["profit"] = df["revenue"] - df["cost"]
    return df
