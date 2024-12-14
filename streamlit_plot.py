import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Load the data (replace 'Main_Data.csv' with your file path)
data = pd.read_csv('Main_Data.csv')

# Streamlit app title
st.title("Survey Data Analysis")

# Plot histograms for survey answers (assuming survey answers are in specific columns)
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

# Calculate and display the mean for each survey question
means = {}
st.header("Survey Question Histograms")
for column in survey_columns:
    means[column] = data[column].mean()
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.hist(data[column], bins=5, edgecolor='black', alpha=0.7, color='coral')
    ax.set_title(f'Histogram for {column} (Mean: {means[column]:.2f})')
    ax.set_xlabel('Response (1-5)')
    ax.set_ylabel('Frequency')
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    st.pyplot(fig)

# Gender distribution (pie chart)
st.header("Gender Distribution")
gender_counts = data['Gender'].value_counts()
fig, ax = plt.subplots(figsize=(8, 6))
ax.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90, colors=['lightblue', 'pink', 'lightgreen'])
ax.set_title('Gender Distribution')
st.pyplot(fig)

# Age distribution (bar chart)
st.header("Age Distribution")
age_counts = data['Age'].value_counts().sort_index()
fig, ax = plt.subplots(figsize=(8, 6))
ax.bar(age_counts.index, age_counts.values, color='orange', edgecolor='black')
ax.set_title('Age Distribution')
ax.set_xlabel('Age')
ax.set_ylabel('Frequency')
ax.grid(axis='y', linestyle='--', alpha=0.7)
st.pyplot(fig)

# Calculate and display the mean age
mean_age = data['Age'].mean()
st.subheader(f"Mean Age: {mean_age:.2f}")

# Plot means of survey questions and age
st.header("Mean Values of Survey Questions and Age")
all_means = list(means.values()) + [mean_age]
labels = survey_columns + ['Mean Age']
fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(labels, all_means, color='teal', edgecolor='black')
ax.set_title('Mean Values of Survey Questions and Age')
ax.set_xlabel('Mean')
ax.set_ylabel('Questions')
ax.grid(axis='x', linestyle='--', alpha=0.7)
st.pyplot(fig)
