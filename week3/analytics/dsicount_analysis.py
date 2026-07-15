import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("data/normalized_dataset.csv")
discount= (df.groupby('platform')['discount_percent'].mean())
discount.plot(kind='bar')
plt.title("Average Discount By Platform")
plt.savefig("visual/discount_analysis.png")
plt.show()