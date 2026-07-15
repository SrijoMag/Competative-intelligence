import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/normalized_dataset.csv")
top_brands = (df.groupby('brand')['current_price'].mean().sort_values(ascending=False)
    .head(10))
top_brands.plot(kind='bar')
plt.title("Top Brand Pricing")
plt.savefig("Visual/brand_comparison.png")
plt.show()