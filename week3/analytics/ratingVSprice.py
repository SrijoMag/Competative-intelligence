import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("data/normalized_dataset.csv")
plt.figure(figsize=(8,6))
plt.scatter(df['current_price'],df['rating'])
plt.xlabel("Pricing")
plt.ylabel("Rating")
plt.title("Rating VS Price")
plt.savefig("visual/Rating_vs_Price.png")
plt.show()