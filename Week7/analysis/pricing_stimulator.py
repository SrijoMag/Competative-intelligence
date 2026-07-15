import streamlit as st
import pandas as pd
import plotly.express as px
from utils import *


def show_pricing_simulator():

    st.title("💰 Dynamic Pricing Simulator")

    df = load_dashboard()

    products = df["product_name"].tolist()

    product = st.selectbox(
        "Select Product",
        products
    )

    product_df = df[df["product_name"] == product].iloc[0]

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Current Price",
            f"₹ {round(product_df['current_price'],2)}"
        )

        st.metric(
            "Rating",
            round(product_df["rating"],2)
        )

        st.metric(
            "Opportunity Score",
            round(product_df["opportunity_score"],2)
        )

    with col2:

        st.metric(
            "Priority",
            product_df["priority"]
        )

        st.metric(
            "Platform",
            product_df["platform"]
        )

        st.metric(
            "Brand",
            product_df["brand"]
        )

    st.markdown("---")

    st.subheader("Pricing Simulation")

    new_price = st.slider(

        "Select New Price",

        min_value=int(df["current_price"].min()),

        max_value=int(df["current_price"].max() * 1.5),

        value=int(product_df["current_price"])

    )

    current_price = product_df["current_price"]

    difference = new_price - current_price

    percentage = (difference / current_price) * 100

    st.write(f"Price Change : **{percentage:.2f}%**")

    if percentage < -10:

        strategy = "Aggressive Pricing"

        color = "green"

    elif percentage > 10:

        strategy = "Premium Pricing"

        color = "red"

    else:

        strategy = "Balanced Pricing"

        color = "blue"

    st.markdown(

        f"<h3 style='color:{color}'>{strategy}</h3>",

        unsafe_allow_html=True

    )

    demand = max(20, 100 - percentage)

    revenue = new_price * demand

    profit = revenue * 0.18

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Estimated Demand",
        round(demand)
    )

    col2.metric(
        "Estimated Revenue",
        f"₹ {round(revenue,2)}"
    )

    col3.metric(
        "Estimated Profit",
        f"₹ {round(profit,2)}"
    )

    st.markdown("---")

    scenario = pd.DataFrame({

        "Scenario": [

            "Current",

            "Simulated"

        ],

        "Price": [

            current_price,

            new_price

        ],

        "Revenue": [

            current_price * 100,

            revenue

        ]

    })

    fig = px.bar(

        scenario,

        x="Scenario",

        y="Revenue",

        color="Scenario",

        text_auto=".2f",

        title="Revenue Comparison"

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    st.markdown("---")

    st.subheader("Business Recommendation")

    if percentage < -10:

        st.success("""

Recommended Strategy

• Increase sales volume

• Gain market share

• Suitable during competitor discounts

""")

    elif percentage > 10:

        st.warning("""

Recommended Strategy

• Premium pricing

• Increase profit margin

• Suitable for high-demand products

""")

    else:

        st.info("""

Recommended Strategy

• Maintain current pricing

• Monitor competitors

• Continue periodic reviews

""")

    export = pd.DataFrame({

        "Product": [product],

        "Current Price": [current_price],

        "Simulated Price": [new_price],

        "Demand": [round(demand)],

        "Revenue": [round(revenue,2)],

        "Profit": [round(profit,2)],

        "Strategy": [strategy]

    })

    csv = export.to_csv(index=False)

    st.download_button(

        "⬇ Download Simulation",

        csv,

        "pricing_simulation.csv",

        "text/csv"

    )