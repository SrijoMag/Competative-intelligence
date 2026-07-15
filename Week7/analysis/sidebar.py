import streamlit as st
from datetime import datetime


def show_sidebar():

    st.sidebar.image(
        "https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
        width=100
    )

    st.sidebar.title("📊 CI Dashboard")

    st.sidebar.markdown("---")

    page = st.sidebar.radio(

        "Navigation",

        [

            "🏠 Home",

            "📈 Executive Dashboard",

            "🏢 Competitor Monitor",

            "💰 Pricing Simulator",

            "🎯 Recommendation Dashboard",

            "🚨 Competitor Alerts",

            "📄 Export Reports",

            "🌍 Market Analysis",

            "ℹ About"

        ]

    )

    st.sidebar.markdown("---")

    st.sidebar.subheader("Project Details")

    st.sidebar.info(
        """
**Intern**

Srijoswin Mazumder

**Project**

Competitive Intelligence &
Pricing Strategy Engine

**Week**

7

**Version**

1.0
"""
    )

    st.sidebar.markdown("---")

    st.sidebar.subheader("Dashboard Statistics")

    st.sidebar.metric(
        "Modules",
        8
    )

    st.sidebar.metric(
        "Datasets",
        4
    )

    st.sidebar.metric(
        "Charts",
        15
    )

    st.sidebar.metric(
        "Products",
        22
    )

    st.sidebar.markdown("---")

    st.sidebar.caption(
        "Last Updated"
    )

    st.sidebar.write(
        datetime.now().strftime("%d-%m-%Y")
    )

    st.sidebar.markdown("---")

    st.sidebar.success(
        "Dashboard Ready"
    )

    return page