import pandas as pd
import os

BASE_dir=os.path.dirname(os.path.dirname(os.path.abspath("week3/data/cleaned_dataset.csv")))
Output_file=os.path.join(BASE_dir,"data")
os.makedirs(Output_file,exist_ok=True)
df=pd.read_csv(r"c:\Users\KIIT0001\Desktop\Project\Week3\data\normalized_dataset.csv")

market_avg=df["current_price"].mean()
alerts=df[df["current_price"]>market_avg]

alerts.to_csv(os.path.join(Output_file,"competitor_alerts.csv"),index=False)

print(alerts.head())