import pandas as pd
import os

BASE_dir=os.path.dirname(os.path.dirname(os.path.abspath("week3/data/cleaned_dataset.csv")))
Data_file=os.path.join(BASE_dir,"..","week3","data","normalized_dataset.csv")
Output_file=os.path.join(BASE_dir,"data","competitor_segments.csv")
df=pd.read_csv(r"C:\Users\KIIT0001\Desktop\Project\week3\data\normalized_dataset.csv")
summary=(df.groupby("platform").agg({"current_price": "mean","rating": "mean","review_count": "mean"}).reset_index())

def classify(row):
    
        if row["rating"] >= 4 and row["review_count"] >= 100:
            return "Leader"
    
        elif row["rating"] >= 3.5:
            return "Challenger"
    
        else:
            return "Niche Player"
    
summary["segment"] = summary.apply(
        classify,
        axis=1
    )

os.makedirs(
    os.path.dirname(Output_file),
    exist_ok=True
)
    
summary.to_csv(
        "data/competitor_segments.csv",
        index=False
    )
    
print(summary)