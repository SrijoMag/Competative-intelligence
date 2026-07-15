import pandas as pd

df = pd.read_csv(
    "../data/cleaned_master_dataset.csv"
)

best_prices = df.loc[
    df.groupby(
        "product_name"
    )["current_price"].idxmin()
]

print(
    best_prices[
        [
            "product_name",
            "platform",
            "current_price"
        ]
    ]
)