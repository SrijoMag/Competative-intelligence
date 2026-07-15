import streamlit as st
import plotly.express as px
from utils import *


def show_recommendation_dashboard():

    st.title("🎯 Strategic Recommendation Dashboard")

    df = load_dashboard()

    st.markdown(
        "Business recommendations generated using the Strategic Recommendation Engine."
    )

    st.markdown("---")

    # ----------------------------
    # Filters
    # ----------------------------

    col1, col2 = st.columns(2)

    priority = col1.selectbox(
        "Priority",
        ["All"] + sorted(df["priority"].unique().tolist())
    )

    brand = col2.selectbox(
        "Brand",
        ["All"] + sorted(df["brand"].unique().tolist())
    )

    filtered = df.copy()

    if priority != "All":
        filtered = filtered[
            filtered["priority"] == priority
        ]

    if brand != "All":
        filtered = filtered[
            filtered["brand"] == brand
        ]

    st.success(f"Products : {len(filtered)}")

    st.markdown("---")

    st.subheader("Strategic Recommendations")

    st.dataframe(
        filtered,
        use_container_width=True,
        height=450
    )

    st.markdown("---")

    # ----------------------------
    # Priority Distribution
    # ----------------------------

    fig = px.pie(

        filtered,

        names="priority",

        hole=0.5,

        title="Priority Distribution"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown("---")

    # ----------------------------
    # Opportunity Score
    # ----------------------------

    fig = px.bar(

        filtered.sort_values(
            "opportunity_score",
            ascending=False
        ),

        x="brand",

        y="opportunity_score",

        color="priority",

        hover_name="product_name",

        text_auto=".2f",

        title="Opportunity Score"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown("---")

    # ----------------------------
    # Top 10 Products
    # ----------------------------

    st.subheader("Top Priority Products")

    top = filtered.sort_values(

        "priority_score",

        ascending=False

    ).head(10)

    st.dataframe(
        top,
        use_container_width=True
    )

    st.markdown("---")

    # ----------------------------
    # Scatter Plot
    # ----------------------------

    fig = px.scatter(

        filtered,

        x="current_price",

        y="opportunity_score",

        color="priority",

        size="rating",

        hover_name="product_name",

        title="Price vs Opportunity"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown("---")

    # ----------------------------
    # Business Insights
    # ----------------------------

    st.success("Business Insights")

    highest = filtered.iloc[
        filtered["opportunity_score"].idxmax()
    ]

    st.info(f"""
Highest Opportunity Product

**{highest['product_name']}**

Brand : **{highest['brand']}**

Opportunity Score : **{highest['opportunity_score']:.2f}**

Priority : **{highest['priority']}**
""")

    csv = filtered.to_csv(index=False)

    st.download_button(

        "⬇ Download Recommendations",

        csv,

        "recommendations.csv",

        "text/csv"

    )