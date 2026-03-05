
import matplotlib.pyplot as plt

def save_timeseries_chart(ts_df, path):
    plt.figure()
    plt.plot(ts_df["bucket"], ts_df["revenue"], label="Revenue")
    plt.plot(ts_df["bucket"], ts_df["profit"], label="Profit")
    plt.title("Revenue & Profit Over Time"); plt.xlabel("Period"); plt.ylabel("Amount")
    plt.legend(); plt.tight_layout(); plt.savefig(path, dpi=150); plt.close()

def save_category_chart(cat_df, path):
    plt.figure()
    plt.bar(cat_df["category"], cat_df["revenue"])
    plt.title("Revenue by Category"); plt.xlabel("Category"); plt.ylabel("Revenue")
    plt.xticks(rotation=30, ha="right"); plt.tight_layout(); plt.savefig(path, dpi=150); plt.close()

def save_channel_chart(ch_df, path):
    plt.figure()
    plt.pie(ch_df["revenue"], labels=ch_df["channel"], autopct="%1.1f%%")
    plt.title("Channel Revenue Share"); plt.tight_layout(); plt.savefig(path, dpi=150); plt.close()

def save_geo_chart(geo_df, path):
    top = geo_df.sort_values("revenue", ascending=False).head(15)
    plt.figure()
    plt.barh(top["city"], top["revenue"])
    plt.title("Top Cities by Revenue"); plt.xlabel("Revenue"); plt.ylabel("City")
    plt.tight_layout(); plt.savefig(path, dpi=150); plt.close()
