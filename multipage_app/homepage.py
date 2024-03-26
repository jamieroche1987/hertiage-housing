import streamlit as st

st.set_page_config(
            page_title="Heritage Housing",
            page_icon="🏘️"
        )

st.title("Homepage")

st.info(
    f"Welcome to the Heritage Housing!\n"
    f"\nThe purpose of this app is to Heritage Housing (currently) only\n"
    f"avaliable in the Ames area.\n\n"
    f"The following pages can be found here:\n\n"
    f"* Project Summary\n\n"
    f"* Hypothesis and Validation\n\n"
    f"* Propery Sale Price Study\n\n"
    f"* Sales Predictor\n\n"
    f"* ML Model\n\n")

st.sidebar.write("Select page above to view")