import streamlit as st
import os


def load_css():

    base_dir = os.path.dirname(os.path.abspath(__file__))

    css_path = os.path.join(
        os.path.dirname(base_dir),
        "assets",
        "style.css"
    )

    if os.path.exists(css_path):

        with open(css_path) as f:

            st.markdown(

                f"<style>{f.read()}</style>",

                unsafe_allow_html=True

            )

    else:

        st.warning("style.css not found.")