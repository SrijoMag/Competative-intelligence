import streamlit as st

from style import load_css
from home import show_home
from executive_Dashboard import show_dashboard
from competitor_monitor import show_competitor_monitor
from pricing_stimulator import show_pricing_simulator
from recommendatio_dashboard import show_recommendation_dashboard
from alerts import show_alert_dashboard
from export_report import show_export_center
from geo_dashboard import show_geo_dashboard


st.set_page_config(
    page_title="Competitive Intelligence Platform",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_css()

st.sidebar.image(
    "https://img.icons8.com/color/96/combo-chart.png",
    width=80
)

st.sidebar.title("Pricing Intelligence")

st.sidebar.markdown(
"""
### Week 7 Dashboard

Strategic Recommendation Engine
"""
)

page = st.sidebar.radio(

    "Navigation",

    [

        "🏠 Home",

        "📊 Executive Dashboard",

        "🏢 Competitor Monitor",

        "💰 Pricing Simulator",

        "🎯 Recommendation Dashboard",

        "🚨 Competitor Alerts",

        "📤 Export Reports",

        "🌍 Geo Dashboard"

    ]

)

st.sidebar.markdown("---")

st.sidebar.info(
"""
**Intern**

Srijoswin Mazumder

Competitive Intelligence & Pricing Strategy Engine

Week 7
"""
)

if page == "🏠 Home":

    show_home()

elif page == "📊 Executive Dashboard":

    show_dashboard()

elif page == "🏢 Competitor Monitor":

    show_competitor_monitor()

elif page == "💰 Pricing Simulator":

    show_pricing_simulator()

elif page == "🎯 Recommendation Dashboard":

    show_recommendation_dashboard()

elif page == "🚨 Competitor Alerts":

    show_alert_dashboard()

elif page == "📤 Export Reports":

    show_export_center()

elif page == "🌍 Geo Dashboard":

    show_geo_dashboard()