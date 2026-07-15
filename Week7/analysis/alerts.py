
import streamlit as st
import pandas as pd
import plotly.express as px

from utils import *


def show_alert_dashboard():

    st.title("🚨 Competitor Alert Center")

    df = load_dashboard()

    alerts = []

    avg_price = df["current_price"].mean()
    avg_rating = df["rating"].mean()

    # ------------------------------------
    # High Price
    # ------------------------------------

    for _, row in df.iterrows():

        if row["current_price"] > avg_price * 1.20:

            alerts.append({

                "Type":"High Price",

                "Severity":"High",

                "Brand":row["brand"],

                "Platform":row["platform"],

                "Product":row["product_name"],

                "Message":"Price is significantly above market average."

            })

    # ------------------------------------
    # Low Rating
    # ------------------------------------

    for _, row in df.iterrows():

        if row["rating"] < avg_rating:

            alerts.append({

                "Type":"Low Rating",

                "Severity":"Medium",

                "Brand":row["brand"],

                "Platform":row["platform"],

                "Product":row["product_name"],

                "Message":"Customer rating below average."

            })

    # ------------------------------------
    # High Opportunity
    # ------------------------------------

    for _, row in df.iterrows():

        if row["opportunity_score"] >= 85:

            alerts.append({

                "Type":"Opportunity",

                "Severity":"High",

                "Brand":row["brand"],

                "Platform":row["platform"],

                "Product":row["product_name"],

                "Message":"Immediate pricing opportunity."

            })

    # ------------------------------------
    # Critical Priority
    # ------------------------------------

    for _, row in df.iterrows():

        if row["priority"]=="Critical":

            alerts.append({

                "Type":"Critical",

                "Severity":"Critical",

                "Brand":row["brand"],

                "Platform":row["platform"],

                "Product":row["product_name"],

                "Message":"Immediate business action required."

            })

    alerts = pd.DataFrame(alerts)

    if alerts.empty:

        st.success("No alerts generated.")

        return

    st.success(f"Total Alerts : {len(alerts)}")

    st.markdown("---")

    # ===========================================
    # KPIs
    # ===========================================

    c1,c2,c3,c4 = st.columns(4)

    c1.metric(
        "Critical",
        len(alerts[alerts["Severity"]=="Critical"])
    )

    c2.metric(
        "High",
        len(alerts[alerts["Severity"]=="High"])
    )

    c3.metric(
        "Medium",
        len(alerts[alerts["Severity"]=="Medium"])
    )

    c4.metric(
        "Total",
        len(alerts)
    )

    st.markdown("---")

    st.subheader("Generated Alerts")

    st.dataframe(

        alerts,

        use_container_width=True,

        height=450

    )

    st.markdown("---")

    # ===========================================
    # Charts
    # ===========================================

    fig = px.pie(

        alerts,

        names="Severity",

        hole=.55,

        title="Alert Severity"

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    fig = px.bar(

        alerts,

        x="Brand",

        color="Severity",

        title="Alerts by Brand",

        text_auto=True

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    fig = px.bar(

        alerts,

        x="Platform",

        color="Severity",

        title="Alerts by Platform",

        text_auto=True

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    st.markdown("---")

    csv = alerts.to_csv(index=False)

    st.download_button(

        "⬇ Download Alerts",

        csv,

        "competitor_alerts.csv",

        "text/csv"

    )