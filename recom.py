# Book Recommendation Website using Streamlit
# First import the necessary libraries
import requests
import streamlit as st

API_URL = "https://www.googleapis.com/books/v1/volumes"

# Function to fetch books from Google API
def fetch_book(query):
    param = {
        'q': query,
        'maxResults': 20
    }
    response = requests.get(API_URL, params=param)
    if response.status_code == 200:
        data = response.json()
        return data.get('items', [])
    else:
        st.error(f"Error fetching data of the book from Google API: {response.status_code}")
        return []

# Streamlit App
st.title("Book Recommendation Website")
st.write("Looking for a good book to read? Browse through some of our recommendations below!")

# User input for genre or keyword
search_query = st.text_input("Enter a genre or keyword to search for books", "Fiction")

# Fetch books based on the user input
if search_query:
    books = fetch_book(search_query)

if books:
    for book in books:
        volume_info = book.get('volumeInfo', {})
        title = volume_info.get('title', 'No title')
        authors = volume_info.get('authors', ['Unknown Author'])  # Corrected from 'Author' to 'authors'
        description = volume_info.get('description', 'No description available')
        rating = volume_info.get('averageRating', 'No Rating')
        
        # Fetch book image (thumbnail)
        image_links = volume_info.get('imageLinks', {})
        thumbnail = image_links.get('thumbnail', None)  # Use 'thumbnail' key to get the image link

        # Display book info
        st.subheader(title)
        st.write(f"**Author(s)**: {', '.join(authors)}")
        st.write(f"**Rating**: {rating}")
        st.write(f"**Description**: {description}")
        
        # Display image if available
        if thumbnail:
            st.image(thumbnail, width=150)  # Display thumbnail with a width of 150px
        
        st.write("---")
else:
    st.write(f"No books found for {search_query}. Try a different genre or keyword.")
