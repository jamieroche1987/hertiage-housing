import streamlit as st
from src.data_management import load_property_data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")

## Streamlit warning appears despite using the st.cache_data command

def page_sale_price_study():
    st.write("#### 🏡 Property Sale Price Study")

     #load the data
    df = load_property_data()

    # copies from sales price study notebook
    vars_to_study = ['OverallQual','TotalBsmtSF','1stFlrSF',
                    'YearBuilt', 'GarageArea','GrLivArea']

    st.info(
        f"**House Price Study**"
        f"*Business Requirement 1*:\n"
        f"* 1 - The client is interested in discovering how the house attributes\n"
        f"correlate with the sale price.\n"
        f"Therefore, the client expects data visualisations of\n"
        f"the correlated variables against the sale price to show that.\n\n"
        f"**This business requirement were satisfied and met.**"
    )
    if st.checkbox("Inspect Property Attributes"):


        st.write(
            f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns,\n"
            f"see below for the first 25 rows.\n\n"
            f"*Note: All NaN variables have been cleaned*")
        st.write(df.head(25))

    st.write("---")

    st.info(
        f"As per the clients request, a correlatiom study was\n"
        f"performed to better understand how the attributes\n"
        f"are correlated to sale prices.\n\n"
        f"The study concluded that the most correlated\n"
        f"variables were: **{vars_to_study}**"
        )

    # code copied from sales price study notebook
    df_eda = df.filter(vars_to_study + ['SalePrice'])

    if st.checkbox("Sale Price Study Visulations"):
        sale_price_per_var(df_eda, vars_to_study)

# cache decoder
@st.cache_data 
def sale_price_per_var(df_eda, vars_to_study):
    # function based on sale price study notebook
    target_var = 'SalePrice'
    for col in vars_to_study:
        plot_numerical(df_eda, col, target_var)
        st.write("\n\n")

# cache decoder
@st.cache_data 
def plot_numerical(df, col, target_var):
    # function based on sale price study notebook
    fig, axes = plt.subplots(figsize=(15, 8))
    sns.regplot(data=df, x=col, y=target_var)
    plt.title(f"{col}", fontsize=20)
    st.pyplot(fig)