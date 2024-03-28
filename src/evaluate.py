import streamlit as st
import pandas as pd
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Functions for performance evaluation - from Predict House Prices notebook


def regression_performance(X_train, y_train, x_test, y_test, pipeline):
    st.write("#### **Model Evaluation** \n")
    st.write("**Train Set**")
    regression_evaluation(X_train, y_train, pipeline)
    st.write("**Test Set**")
    regression_evaluation(x_test, y_test, pipeline)


def regression_evaluation(X, y, pipeline):
	@@ -25,22 +25,3 @@ def regression_evaluation(X, y, pipeline):
    st.write('Root Mean Squared Error:', np.sqrt(
        mean_squared_error(y, prediction)).round(3))
    st.write("\n")