import pandas as pd
import os
import matplotlib.pyplot as plt

BASE_dir=os.path.dirname(os.path.dirname(os.path.abspath("../week3/data/cleaned_dataset.csv")))
Visual_dir=os.path.join(BASE_dir,"visuals")
os.makedirs(Visual_dir,exist_ok=True)
df=pd.read_csv(os.path.join(BASE_dir,"..","week3","data","normalized_dataset.csv"))
summary=(df.groupby("platform").agg({"current_price":"mean","rating":"mean"}))
plt.figure(figsize=(8,6))

plt.scatter(
    summary["current_price"],
    summary["rating"]
)

for platform in summary.index:

    plt.annotate(
        platform,
        (
            summary.loc[
                platform,
                "current_price"
            ],
            summary.loc[
                platform,
                "rating"
            ]
        )
    )

plt.xlabel("Average Price")
plt.ylabel("Average Rating")

plt.title(
    "Competitor Perceptual Map"
)

plt.tight_layout()

plt.savefig(
        "visuals/perceptual_map.png"
    )


plt.show()
