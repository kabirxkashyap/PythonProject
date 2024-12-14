import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

data = pd.read_csv('Main_Data.csv')

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

means = {}
for column in survey_columns:
    means[column] = data[column].mean()
    plt.figure(figsize=(8, 6))
    plt.hist(data[column], bins=5, edgecolor='black', alpha=0.7, color='coral')
    plt.title(f'Histogram for {column} (Mean: {means[column]:.2f})')
    plt.xlabel('Response (1-5)')
    plt.ylabel('Frequency')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

gender_counts = data['Gender'].value_counts()
plt.figure(figsize=(8, 6))
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90, colors=['lightblue', 'pink', 'lightgreen'])
plt.title('Gender Distribution')
plt.axis('equal') 
plt.show()

age_counts = data['Age'].value_counts().sort_index()
plt.figure(figsize=(8, 6))
plt.bar(age_counts.index, age_counts.values, color='orange', edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

mean_age = data['Age'].mean()
print(f"Mean Age: {mean_age:.2f}")

all_means = list(means.values()) + [mean_age]
labels = survey_columns + ['Mean Age']
plt.figure(figsize=(10, 6))
plt.barh(labels, all_means, color='teal', edgecolor='black')
plt.title('Mean Values of Survey Questions and Age')
plt.xlabel('Mean')
plt.ylabel('Questions')
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
