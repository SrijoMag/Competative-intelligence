import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("data/normalized_dataset.csv")
plt.figure(figsize=(10,6))
df.boxplot(column='current_price',by='platform')
plt.title("Paltform Price Distribution")
plt.suptitle("")
plt.savefig("visual/platfor_price.png")
plt.show()
plt.savefig()