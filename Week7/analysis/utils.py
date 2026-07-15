import pandas as pd
import streamlit as st

from config import *

@st.cache_data
def load_dashboard():

    return pd.read_csv(DASHBOARD_DATA)


@st.cache_data
def load_recommendation():

    return pd.read_csv(STRATEGIC_RECOMMENDATIONS)


@st.cache_data
def load_opportunity():

    return pd.read_csv(OPPORTUNITY_SCORES)


@st.cache_data
def load_priority():

    return pd.read_csv(PRIORITY_PRODUCTS)


def get_kpis(df):

    kpi = {

        "Total Products": len(df),

        "Average Price": round(
            df["current_price"].mean(),2
        ),

        "Average Rating": round(
            df["rating"].mean(),2
        ),

        "Average Discount": round(
            df["discount_percent"].mean(),2
        ),

        "Average Opportunity": round(
            df["opportunity_score"].mean(),2
        ),

        "Highest Opportunity": round(
            df["opportunity_score"].max(),2
        ),

        "Highest Price": round(
            df["current_price"].max(),2
        ),

        "Lowest Price": round(
            df["current_price"].min(),2
        )

    }

    return kpi

def brand_summary(df):

    summary = (

        df.groupby("brand")

        .agg(

            Product_Count=("brand","count"),

            Average_Price=("current_price","mean"),

            Average_Rating=("rating","mean"),

            Opportunity=("opportunity_score","mean")

        )

        .reset_index()

    )

    return summary.round(2)


def platform_summary(df):

    summary = (

        df.groupby("platform")

        .agg(

            Products=("platform","count"),

            Average_Price=("current_price","mean"),

            Rating=("rating","mean"),

            Opportunity=("opportunity_score","mean")

        )

        .reset_index()

    )

    return summary.round(2)

def top_products(df,n=10):

    return (

        df.sort_values(

            "priority_score",

            ascending=False

        )

        .head(n)

    )

def opportunity_products(df,n=10):

    return (

        df.sort_values(

            "opportunity_score",

            ascending=False

        )

        .head(n)

    )

def recommendation_summary(df):

    return (

        df["final_recommendation"]

        .value_counts()

    )

def priority_summary(df):

    return (

        df["priority"]

        .value_counts()

    )

def filter_brand(df,brand):

    if brand=="All":

        return df

    return df[df["brand"]==brand]

def filter_platform(df,platform):

    if platform=="All":

        return df

    return df[df["platform"]==platform]

def search_product(df,text):

    if text=="":

        return df

    return df[

        df["product_name"]

        .str.contains(

            text,

            case=False,

            na=False

        )

    ]