import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

WEEK7_DIR = os.path.dirname(BASE_DIR)
DATA_FOLDER = os.path.join(WEEK7_DIR, "data")

DASHBOARD_DATA = os.path.join(
    DATA_FOLDER,
    "dashboard_dataset.csv"
)

STRATEGIC_RECOMMENDATIONS = os.path.join(
    DATA_FOLDER,
    "strategic_recommendations.csv"
)

OPPORTUNITY_SCORES = os.path.join(
    DATA_FOLDER,
    "opportunity_scores.csv"
)

PRIORITY_PRODUCTS = os.path.join(
    DATA_FOLDER,
    "priority_products.csv"
)
REPORT_FOLDER = os.path.join(
    WEEK7_DIR,
    "reports"
)

VISUAL_FOLDER = os.path.join(
    WEEK7_DIR,
    "visuals"
)

SCREENSHOT_FOLDER = os.path.join(
    WEEK7_DIR,
    "screenshots"
)
os.makedirs(REPORT_FOLDER, exist_ok=True)
os.makedirs(VISUAL_FOLDER, exist_ok=True)
os.makedirs(SCREENSHOT_FOLDER, exist_ok=True)
APP_TITLE = "Competitive Intelligence Dashboard"
PAGE_ICON = "📊"
LAYOUT = "wide"
PRIMARY_COLOR = "#1f77b4"
SUCCESS_COLOR = "#2ca02c"
WARNING_COLOR = "#ff7f0e"
DANGER_COLOR = "#d62728"