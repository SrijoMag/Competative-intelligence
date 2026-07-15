import streamlit as st
import plotly.express as px
from utils import *


def show_competitor_monitor():

    st.title("🏢 Competitor Monitoring Center")

    df = load_dashboard()

    st.markdown("Monitor competitor pricing, ratings and opportunities.")

    st.markdown("---")

    col1,col2,col3 = st.columns(3)

    brands = ["All"] + sorted(df["brand"].unique().tolist())

    platforms = ["All"] + sorted(df["platform"].unique().tolist())

    brand = col1.selectbox(
        "Brand",
        brands
    )

    platform = col2.selectbox(
        "Platform",
        platforms
    )

    rating = col3.slider(
        "Minimum Rating",
        0.0,
        5.0,
        0.0,
        0.1
    )

    filtered = df.copy()

    if brand != "All":
        filtered = filtered[
            filtered["brand"] == brand
        ]

    if platform != "All":
        filtered = filtered[
            filtered["platform"] == platform
        ]

    filtered = filtered[
        filtered["rating"] >= rating
    ]

    st.success(f"Products Found : {len(filtered)}")

    st.markdown("---")

    st.subheader("Competitor Products")

    st.dataframe(
        filtered,
        use_container_width=True,
        height=500
    )

    st.markdown("---")

    st.subheader("Average Price by Platform")

    platform_price = (

        filtered

        .groupby("platform")["current_price"]

        .mean()

        .reset_index()

    )

    fig = px.bar(

        platform_price,

        x="platform",

        y="current_price",

        color="platform",

        text_auto=".2f"

    )

    fig.update_layout(height=450)

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown("---")

    st.subheader("Average Rating by Brand")

    brand_rating = (

        filtered

        .groupby("brand")["rating"]

        .mean()

        .reset_index()

    )

    fig = px.bar(

        brand_rating,

        x="brand",

        y="rating",

        color="brand",

        text_auto=".2f"

    )

    fig.update_layout(height=450)

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown("---")

    st.subheader("Opportunity Score")

    fig = px.scatter(

        filtered,

        x="current_price",

        y="opportunity_score",

        color="brand",

        size="rating",

        hover_name="product_name"

    )

    fig.update_layout(height=550)

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown("---")

    st.subheader("Top Opportunity Products")

    top = (

        filtered

        .sort_values(

            "opportunity_score",

            ascending=False

        )

        .head(10)

    )

    st.dataframe(

        top,

        use_container_width=True

    )

    csv = top.to_csv(index=False)

    st.download_button(

        "⬇ Download Top Products",

        csv,

        "top_competitors.csv",

        "text/csv"

    )