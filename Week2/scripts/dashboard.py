import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "../data/cleaned_master_dataset.csv"
)

avg_price = df.groupby(
    "platform"
)["current_price"].mean()

avg_price.plot(
    kind="bar"
)

plt.title(
    "Average Price by Platform"
)

plt.ylabel(
    "Price"
)

plt.show()
