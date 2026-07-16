
import streamlit as st
import pandas as pd
from utils import *


def show_export_center():

    st.title(" Export Reports")

    st.markdown(
        "Download datasets, recommendations and analytical reports."
    )

    df = load_dashboard()

    st.markdown("---")

    st.subheader("Dataset Preview")

    st.dataframe(
        df,
        use_container_width=True,
        height=450
    )

    st.markdown("---")

    # ------------------------------------------
    # Filter Section
    # ------------------------------------------

    col1, col2 = st.columns(2)

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

    filtered = df.copy()

    if brand != "All":
        filtered = filtered[
            filtered["brand"] == brand
        ]

    if platform != "All":
        filtered = filtered[
            filtered["platform"] == platform
        ]

    st.success(f"{len(filtered)} Products Selected")

    st.markdown("---")

    st.subheader("Filtered Dataset")

    st.dataframe(
        filtered,
        use_container_width=True
    )

    st.markdown("---")

    # ------------------------------------------
    # CSV Export
    # ------------------------------------------

    csv = filtered.to_csv(index=False)

    st.download_button(
        "⬇ Download CSV",
        csv,
        "dashboard_dataset.csv",
        "text/csv"
    )

    # ------------------------------------------
    # Excel Export
    # ------------------------------------------

    excel = filtered.to_excel(
        "export.xlsx",
        index=False
    )

    with open("export.xlsx", "rb") as file:

        st.download_button(
            "⬇ Download Excel",
            file,
            "dashboard_dataset.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

    st.markdown("---")

    # ------------------------------------------
    # Summary
    # ------------------------------------------

    st.subheader("Export Summary")

    st.info(f"""

Products : **{len(filtered)}**

Average Price : **₹ {round(filtered['current_price'].mean(),2)}**

Average Rating : **{round(filtered['rating'].mean(),2)}**

Average Opportunity Score : **{round(filtered['opportunity_score'].mean(),2)}**

""")