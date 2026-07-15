import streamlit as st
import plotly.express as px

from utils import *
from kpi_card import kpi_card


def show_dashboard():

    st.title("📊 Executive Dashboard")
    st.markdown("### Competitive Intelligence & Pricing Strategy Engine")

    df = load_dashboard()

    kpi = get_kpis(df)

    st.markdown("## 📌 Business KPIs")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        kpi_card(
            "Products",
            kpi["Total Products"],
            "#2563EB",
            "📦"
        )

    with c2:
        kpi_card(
            "Average Price",
            f"₹ {round(kpi['Average Price'],2)}",
            "#10B981",
            "💰"
        )

    with c3:
        kpi_card(
            "Average Rating",
            round(kpi["Average Rating"],2),
            "#F59E0B",
            "⭐"
        )

    with c4:
        kpi_card(
            "Average Discount",
            f"{round(kpi['Average Discount'],2)}%",
            "#EF4444",
            "🏷️"
        )

    st.write("")

    c5, c6, c7, c8 = st.columns(4)

    with c5:
        kpi_card(
            "Opportunity",
            round(kpi["Average Opportunity"],2),
            "#7C3AED",
            "🎯"
        )

    with c6:
        kpi_card(
            "Highest Score",
            round(kpi["Highest Opportunity"],2),
            "#0EA5E9",
            "📈"
        )

    with c7:
        kpi_card(
            "Highest Price",
            f"₹ {round(kpi['Highest Price'],2)}",
            "#F97316",
            "💵"
        )

    with c8:
        kpi_card(
            "Lowest Price",
            f"₹ {round(kpi['Lowest Price'],2)}",
            "#14B8A6",
            "💸"
        )

    st.markdown("---")

    st.markdown("## 🏷 Brand Performance")

    brand = brand_summary(df)

    st.dataframe(
        brand,
        use_container_width=True
    )

    fig = px.bar(
        brand,
        x="brand",
        y="Opportunity",
        color="Opportunity",
        text_auto=".2f",
        title="Average Opportunity Score by Brand"
    )

    fig.update_layout(
        height=450,
        xaxis_title="Brand",
        yaxis_title="Opportunity Score"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown("---")

    st.markdown("## 🏪 Platform Analysis")

    platform = platform_summary(df)

    st.dataframe(
        platform,
        use_container_width=True
    )

    fig = px.bar(
        platform,
        x="platform",
        y="Average_Price",
        color="Average_Price",
        text_auto=".2f",
        title="Average Product Price by Platform"
    )

    fig.update_layout(height=450)

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("### Recommendation Distribution")

        rec = recommendation_summary(df)

        fig = px.pie(
            names=rec.index,
            values=rec.values,
            hole=0.55,
            title="Recommendations"
        )

        fig.update_traces(textposition="inside")

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with col2:

        st.markdown("### Priority Distribution")

        pri = priority_summary(df)

        fig = px.pie(
            names=pri.index,
            values=pri.values,
            hole=0.55,
            title="Priority"
        )

        fig.update_traces(textposition="inside")

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.markdown("---")

    st.markdown("## 💰 Price vs Rating")

    fig = px.scatter(

        df,

        x="current_price",

        y="rating",

        color="brand",

        size="opportunity_score",

        hover_name="product_name",

        title="Price vs Rating Analysis"

    )

    fig.update_layout(height=550)

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown("---")

    st.markdown("## 🎯 Opportunity Score Distribution")

    fig = px.histogram(

        df,

        x="opportunity_score",

        color="brand",

        marginal="box",

        nbins=15,

        title="Opportunity Score Distribution"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown("---")
    col1, col2 = st.columns(2)

    with col1:

        st.markdown("### ⭐ Top Priority Products")

        top = top_products(df)

        st.dataframe(
            top.style.highlight_max(
                subset=["priority_score"],
                color="lightgreen"
            ),
            use_container_width=True
        )

    with col2:

        st.markdown("### 🚀 Top Opportunity Products")

        opp = opportunity_products(df)

        st.dataframe(
            opp.style.highlight_max(
                subset=["opportunity_score"],
                color="orange"
            ),
            use_container_width=True
        )

    st.markdown("---")

    st.success("### 📈 Executive Insights")

    st.info(f"""
- Total Products Analysed : **{kpi['Total Products']}**
- Average Market Price : **₹ {round(kpi['Average Price'],2)}**
- Highest Opportunity Score : **{round(kpi['Highest Opportunity'],2)}**
- Average Customer Rating : **{round(kpi['Average Rating'],2)}**
- Products with higher opportunity scores should be prioritised for pricing strategy revisions.
- Platforms with lower average prices may require aggressive pricing strategies.
- High-priority products should be monitored continuously for competitor price changes.
""")