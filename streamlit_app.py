#Statistical Calculator
#First we will include all the libraries we need
#We will be using Streamlit to develop the web app with full functionality

import streamlit as st
import pandas as pd
import numpy as np
from scipy import stats
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

st.title('Statistical Calculator')
st.header('By Kabir Kashyap')

#Processing Input Function

def process_input(input_str):
    try:
        return list(map(float, input_str.split(',')))
    except ValueError:
        st.error("Please ensure all the entries are valid numbers")
        return []
    
#Input Section
st.subheader("Data Input")
x_input = st.text_area("Enter data for variable x (Comma Seperated Values)", value = "1,2,3,4,5")
y_input = st.text_area("Enter a list of number for Y (Comma Seperated Values, optional for regression)", value = "2,4,6,8,10")

x = process_input(x_input)
y = process_input(y_input)

if x:
    st.subheader("Measures of Central Tendency")
    st.write(f"Mean: {np.mean(x): .2f}")
    st.write(f"Median: {np.median(x): .2f}")

    try:
        mode = stats.mode(x)(x)
        st.write(f"Mode: {mode: .2f}")
    except:
        st.write("Mode: No mode found (no repeating values)")

    st.subheader("Measures of Dispersion")
    st.write(f"Range: {np.ptp(x): .2f}")
    st.write(f"Variance: {np.var(x): .2f}")
    st.write(f"Standard Deviaton: {np.std(x, ddof=1):.2f}")

    #Plot Histogram for X
    st.subheader("Histogram of X")
    fig, ax = plt.subplots()
    ax.hist(x, bins=10, color ='skyblue', edgecolor = 'black')
    ax.set_title("Histogram of X")
    ax.set_xlabel("values of X")
    ax.set_ylabel('Values of Y')
    st.pyplot(fig)

    if y and len(x) == len(y):
        #Converting to a 2D array for regression
        x = np.array(x).reshape(-1,1)
        y = np.array(y)

        model = LinearRegression().fit(x,y)
        slope = model.coef_[0]
        intercept = model.intercept_

        st.subheader("Linear Regression Analysis")
        st.write(f"Equation: Y = {slope:.2f} * X + {intercept:.2f}")
        st.write(f"Slope: {slope:.2f}")
        st.write(f"Intercept: {intercept:.2f}")


        #Predict Values
        y_pred = model.predict(x)
        st.write("Predicted Values of Y:", y_pred)

        #Scatter plot with Regression
        st.subheader("Scatter Plot of X and Y with regresion line")
        fig, ax = plt.subplots()
        ax.scatter(x,y, color = 'blue', label='Data Points')
        ax.plot(x, y_pred, color='red', label = 'Regression Line')
        ax.set_title("X vs Y with Reression Line")
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.legend()
        st.pyplot(fig)

    elif y and len(x) != len(y):
        st.warning("X and Y must have the same lenght for Regression Analysis")
