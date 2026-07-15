import pandas as pd
import os

BASE_dir=os.path.dirname(os.path.dirname(os.path.abspath("../week3/data/cleaned_dataset.csv")))
df=pd.read_csv(os.path.join(BASE_dir,"..","week3","data","normalized_dataset.csv"))
platform_price=(df.groupby("platform")["current_price"].mean())
market_avg=(df["current_price"].mean())
gap_df=pd.DataFrame()
gap_df["average_price"]=platform_price
gap_df["pricing_gap"]=(platform_price-market_avg)

gap_df.to_csv("data/pricing_gap_report.csv",index=False)

print(gap_df)