import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Load the data (replace 'Main_Data.csv' with your file path)
data = pd.read_csv('Main_Data.csv')

# Streamlit app title
st.title("Survey Data Analysis")
st.subheader('By Kabir, Jessica and Rudrakshi')

# Define survey columns
survey_columns = [
    '1. Are you free enough to do the things that you love?',
    '2. Do you think that you receive adequate social support and guidance when you need it the most? ',
    '3. Is your academic/professional life stressful?',
    '4. Do you feel financially secured on a daily basis?',
    '5. Do you readily express the feeling of gratitude?',
    '6.  Do you consider yourself to be generous?',
    '7. Do you feel that you were discriminated ever on the basis of your caste, creed, sex or race?',
    '8. Are you satisfied with the current political scenario of the country?',
    '9. Would you consider yourself to be mentally healthy?',
    '10. Are you happy right now?'
]

# Sidebar selection
st.sidebar.title("Select Visualization")
options = st.sidebar.radio("Choose one:", ["Survey Questions", "Gender Distribution", "Age Distribution"])

# Survey questions visualization
if options == "Survey Questions":
    st.header("Survey Question Visualizations")
    selected_question = st.selectbox("Select a question:", survey_columns)
    description = st.text_area("Description for the selected question:", placeholder="Enter a description here...")
    mean_value = data[selected_question].mean()
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.hist(data[selected_question], bins=5, edgecolor='black', alpha=0.7, color='coral')
    ax.set_title(f'Histogram for {selected_question} (Mean: {mean_value:.2f})')
    ax.set_xlabel('Response (1-5)')
    ax.set_ylabel('Frequency')
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    st.pyplot(fig)

# Gender distribution visualization
elif options == "Gender Distribution":
    st.header("Gender Distribution")
    description = st.text_area("Description for Gender Distribution:", placeholder="Enter a description here...")
    gender_counts = data['Gender'].value_counts()
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90, colors=['lightblue', 'pink', 'lightgreen'])
    ax.set_title('Gender Distribution')
    st.pyplot(fig)

# Age distribution visualization
elif options == "Age Distribution":
    st.header("Age Distribution")
    description = st.text_area("Description for Age Distribution:", placeholder="Enter a description here...")
    age_counts = data['Age'].value_counts().sort_index()
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(age_counts.index, age_counts.values, color='orange', edgecolor='black')
    ax.set_title('Age Distribution')
    ax.set_xlabel('Age')
    ax.set_ylabel('Frequency')
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    st.pyplot(fig)

# Display mean age
if options == "Age Distribution":
    mean_age = data['Age'].mean()
    st.subheader(f"Mean Age: {mean_age:.2f}")
