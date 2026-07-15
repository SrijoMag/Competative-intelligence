import pandas as pd
import os

BASE_dir=os.path.dirname(os.path.dirname(os.path.abspath("../week3/data/cleaned_dataset.csv")))

df = pd.read_csv(
    os.path.join(
        BASE_dir,"..","week3","data","normalized_dataset.csv"))

avg_price = (
    df["current_price"]
    .mean()
)

opportunities = df[
    (
        df["rating"] >= 4
    )
    &
    (
        df["current_price"]
        < avg_price
    )
]

opportunities.to_csv(
    "data/opportunity_proxy.csv",index=False)

print(
    opportunities[
        [
            "platform",
            "product_name",
            "current_price",
            "rating"
        ]
    ]
)