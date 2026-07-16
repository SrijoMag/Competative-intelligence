
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from utils import *


def show_geo_dashboard():

    st.title(" Geo Analytics Dashboard")

    st.markdown(
        "Geographical visualization of competitor activity."
    )

    df = load_dashboard()

    location_data = {

        "Amazon": {
            "city": "Bengaluru",
            "lat": 12.9716,
            "lon": 77.5946
        },

        "Flipkart": {
            "city": "Bengaluru",
            "lat": 12.9716,
            "lon": 77.5946
        },

        "Croma": {
            "city": "Mumbai",
            "lat": 19.0760,
            "lon": 72.8777
        }

    }

    geo = []

    for _, row in df.iterrows():

        platform = row["platform"]

        if platform in location_data:

            geo.append({

                "brand": row["brand"],

                "platform": platform,

                "price": row["current_price"],

                "rating": row["rating"],

                "opportunity": row["opportunity_score"],

                "city": location_data[platform]["city"],

                "lat": location_data[platform]["lat"],

                "lon": location_data[platform]["lon"]

            })

    geo = pd.DataFrame(geo)

    st.success(f"Mapped Products : {len(geo)}")

    st.markdown("---")


    m = folium.Map(

        location=[20.5937,78.9629],

        zoom_start=5

    )

    for _, row in geo.iterrows():

        popup = f"""
<b>{row['brand']}</b><br>

Platform : {row['platform']}<br>

City : {row['city']}<br>

Price : ₹ {row['price']}<br>

Rating : {round(row['rating'],2)}<br>

Opportunity : {round(row['opportunity'],2)}
"""

        folium.CircleMarker(

            location=[row["lat"], row["lon"]],

            radius=8,

            popup=popup,

            tooltip=row["brand"],

            color="blue",

            fill=True,

            fill_opacity=0.7

        ).add_to(m)

    st_folium(

        m,

        width=1000,

        height=600

    )

    st.markdown("---")

    summary = geo.groupby("city").agg(

        Products=("brand","count"),

        Average_Price=("price","mean"),

        Average_Rating=("rating","mean"),

        Opportunity=("opportunity","mean")

    ).reset_index()

    st.subheader("City Summary")

    st.dataframe(

        summary,

        use_container_width=True

    )

    st.markdown("---")

    st.subheader("Business Insights")

    st.info("""

• Bengaluru contains major e-commerce competitors.

• Mumbai represents organized retail presence.

• Opportunity score can be monitored geographically.

• Future versions can integrate live warehouse locations.

• Delivery coverage can also be mapped.

""")