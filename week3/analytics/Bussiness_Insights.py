import pandas as pd

df = pd.read_csv("data/normalized_dataset.csv")
print("\n===== BUSINESS INSIGHTS =====\n")
avg_price = (df.groupby('platform')['current_price'].mean())
print("Cheapest Platform:",avg_price.idxmin())
avg_discount = (df.groupby('platform')['discount_percent'].mean())
print("Highest Discount Platform:",avg_discount.idxmax())
avg_rating = (df.groupby('platform')['rating'].mean())

print("Best Rated Platform:",avg_rating.idxmax())

reviews = (df.groupby('platform')['review_count'].mean())
print("Highest Customer Engagement:",reviews.idxmax())