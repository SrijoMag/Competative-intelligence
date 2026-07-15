import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(os.path.abspath("week3/data/cleaned_dataset.csv"))))
OUTPUT_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(OUTPUT_DIR, exist_ok=True)
df = pd.read_csv(r"C:\Users\KIIT0001\Desktop\Project\Week3\data\normalized_dataset.csv")
market_avg = df["current_price"].mean()
recommendations = []
for _, row in df.iterrows():
    if row["current_price"] > market_avg:
        action = "Reduce Price"
    elif row["discount_percent"] < 10:
        action = "Increase Promotion"
    else:
        action = "Maintain Price"
    recommendations.append(action)

df["recommendation"] = recommendations
df.to_csv(os.path.join(OUTPUT_DIR,"pricing_recommendations.csv"),index=False)
print(df[
    [
        "product_name",
        "current_price",
        "recommendation"
    ]
].head())