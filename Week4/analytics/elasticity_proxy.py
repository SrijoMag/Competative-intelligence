import pandas as pd
import os

BASE_dir=os.path.dirname(os.path.dirname(os.path.abspath("../week3/data/cleaned_dataset.csv")))
df = pd.read_csv(
    os.path.join(
        BASE_dir,"..","week3","data","normalized_dataset.csv"))

correlation = (
    df["discount_percent"]
    .corr(
        df["review_count"]
    )
)

print(
    "Elasticity Proxy:",
    round(correlation,3)
)