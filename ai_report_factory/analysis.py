
import pandas as pd

def compute_kpis(df: pd.DataFrame) -> dict:
    revenue = float(df["revenue"].sum())
    profit = float((df["revenue"] - df["cost"]).sum())
    orders = int(df["order_id"].nunique())
    customers = int(df["customer_id"].nunique())
    aov = float(df.groupby("order_id")["revenue"].sum().mean())
    margin = float(profit / revenue) if revenue else 0.0
    return {"revenue": revenue, "profit": profit, "orders": orders, "customers": customers, "aov": aov, "margin": margin}

def timeseries(df: pd.DataFrame, period: str = "M") -> pd.DataFrame:
    if period.upper() == "W":
        df["bucket"] = df["order_date"].dt.to_period("W").apply(lambda p: p.start_time)
    elif period.upper() == "D":
        df["bucket"] = df["order_date"].dt.date
    elif period.upper() == "Q":
        df["bucket"] = df["order_date"].dt.to_period("Q").apply(lambda p: p.start_time)
    else:
        df["bucket"] = df["order_date"].dt.to_period("M").apply(lambda p: p.start_time)
    return df.groupby("bucket").agg(revenue=("revenue","sum"), profit=("profit","sum")).reset_index()

def by_category(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby("category")["revenue"].sum().sort_values(ascending=False).reset_index()

def by_channel(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby("channel")["revenue"].sum().sort_values(ascending=False).reset_index()

def by_geo(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby(["country","city"])["revenue"].sum().reset_index()
