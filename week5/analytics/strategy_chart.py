import pandas as pd
import matplotlib.pyplot as plt
import os

BASE_dir=os.path.dirname(os.path.dirname(os.path.abspath("week3/data/cleaned_dataset.csv")))
Visual_file=os.path.join(BASE_dir,"visuals")
os.makedirs(Visual_file,exist_ok=True)

df = pd.read_csv(os.path.join(BASE_dir,"data","strategy_results.csv"))

plt.figure(figsize=(6,5))

plt.bar(
    df["Strategy"],
    df["Average Price"]
)

plt.title("Pricing Strategy Comparison")
plt.ylabel("Average Price")
plt.tight_layout()

plt.savefig(
    os.path.join(
        Visual_file,
        "strategy_comparison.png"
    )
)

plt.show()