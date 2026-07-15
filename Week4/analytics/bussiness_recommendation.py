import pandas as pd
import os

BASE_dir=os.path.dirname(os.path.dirname(os.path.abspath("../week3/data/cleaned_dataset.csv")))
df = pd.read_csv(
    os.path.join(
        BASE_dir,"..","week3","data","normalized_dataset.csv"))
print("\n===== STRATEGIC INSIGHTS =====\n")

avg_price = (df.groupby("platform")["current_price"].mean())

print("Cheapest Platform:",avg_price.idxmin())
print("Most Expensive Platform:",avg_price.idxmax())

avg_rating = (df.groupby("platform")["rating"].mean())

print("Highest Rated Platform:",avg_rating.idxmax())

avg_discount = (df.groupby("platform")["discount_percent"].mean())

print("Highest Discount Platform:",avg_discount.idxmax())