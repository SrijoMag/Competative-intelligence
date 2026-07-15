import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(os.path.abspath("week3/data/cleaned_dataset.csv"))))
Normalized_DIR = os.path.join(BASE_DIR,"..","Week3","data","normalized_dataset.csv")
Pricing_Recommendation=os.path.join(BASE_DIR,"..","Week5","data","pricing_recommendations.csv")
COMPETITOR_SEGMENT = os.path.join(BASE_DIR,"..","Week4","data","competitor_segments.csv")
PRICING_GAP = os.path.join(BASE_DIR,"..","Week4","data", "pricing_gap_report.csv")

OUTPUT_FOLDER = os.path.join(BASE_DIR, "outputs")
VISUAL_FOLDER = os.path.join(BASE_DIR, "visuals")
REPORT_FOLDER = os.path.join(BASE_DIR, "report")

os.makedirs(OUTPUT_FOLDER, exist_ok=True)
os.makedirs(VISUAL_FOLDER, exist_ok=True)
os.makedirs(REPORT_FOLDER, exist_ok=True)

STRATEGIC_RECOMMENDATION = os.path.join(
    OUTPUT_FOLDER,
    "strategic_recommendations.csv"
)

OPPORTUNITY_SCORE = os.path.join(
    OUTPUT_FOLDER,
    "opportunity_scores.csv"
)

PRIORITY_PRODUCTS = os.path.join(
    OUTPUT_FOLDER,
    "priority_products.csv"
)

DASHBOARD_DATASET = os.path.join(
    OUTPUT_FOLDER,
    "dashboard_dataset.csv"
)

EXECUTIVE_SUMMARY = os.path.join(
    OUTPUT_FOLDER,
    "executive_summary.txt"
)

HIGH_PRICE = 7000

MID_PRICE = 3000

LOW_PRICE = 1500

HIGH_DISCOUNT = 60

GOOD_RATING = 4.2

AVERAGE_RATING = 3.8

HIGH_REVIEWS = 5000

PRICE_WEIGHT = 0.35

RATING_WEIGHT = 0.25

DISCOUNT_WEIGHT = 0.20

REVIEW_WEIGHT = 0.20

MAX_SCORE = 100