import streamlit as st


def kpi_card(title, value, color="#2563EB", icon="📊"):

    st.markdown(

        f"""

<div style="

background:{color};

padding:20px;

border-radius:15px;

box-shadow:0px 5px 15px rgba(0,0,0,.25);

text-align:center;

color:white;

height:150px;

">

<h2>{icon}</h2>

<h4>{title}</h4>

<h1>{value}</h1>

</div>

""",

        unsafe_allow_html=True

    )