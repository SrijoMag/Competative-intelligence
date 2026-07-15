import pandas as pd
import os

BASE_dir=os.path.dirname(os.path.dirname(os.path.abspath("week3/data/cleaned_dataset.csv")))
Output_file=os.path.join(BASE_dir,"data")
os.makedirs(Output_file,exist_ok=True)
df=pd.read_csv(r"C:\Users\KIIT0001\Desktop\Project\week5\week3\data\pricing_recommendations.csv")

results = pd.DataFrame()
results["Strategy"] = ["Aggressive","Conservative"]
results["Average Price"] = [
    (df["current_price"] * 0.95).mean(),
    (df["current_price"] * 0.98).mean()
]

results.to_csv(os.path.join(Output_file,"strategy_results.csv"),index=False)
print(results)