import streamlit as st
import pandas as pd
import os

# File to store book data
BOOKS_FILE = "books.csv"

# Ensure the CSV file exists
if not os.path.exists(BOOKS_FILE):
    df = pd.DataFrame(columns=["Title", "Author", "Genre", "Year"])
    df.to_csv(BOOKS_FILE, index=False)
    
st.set_page_config(page_title="📚library mangement",page_icon="📚",layout="centered")

st.title("📚 Personal Library Manager")

options = ["Add a Book", "Explore Books", "Find a Book"]
selected_option = st.radio("What do you want to do?", options)


def add_books():
    """Function to add a book to the library."""
    st.subheader("📖 Add a New Book")
    
    title = st.text_input("Enter Book Title")
    author = st.text_input("Enter Author Name")
    genre = st.text_input("Enter Book Genre")
    year = st.number_input("Enter Publication Year", min_value=1000, max_value=2025, step=1)

    if st.button("Add Book"):
        if title and author and genre and year:
            # Load existing data
            df = pd.read_csv(BOOKS_FILE)
            #create a new dataframe of book
            new_book = pd.DataFrame([[title, author, genre, year]], columns=["Title", "Author", "Genre", "Year"])
        #concat to the old dataframe and ignore= true ignore index that it easily conact as a row 
            df = pd.concat([df, new_book], ignore_index=True)
            # Save back to CSV
            df.to_csv(BOOKS_FILE, index=False)
            st.success(f"✅ '{title}' by {author} added successfully!")
        else:
            st.warning("⚠️ Please fill in all fields.")


def explore_books():
    """Function to display all books in the library."""
    st.subheader("📚 Your Library Collection")
    
    df = pd.read_csv(BOOKS_FILE)
    
    if df.empty:
        st.info("📂 No books added yet.")
    else:
        st.dataframe(df)


def find_books():
    """Function to search books by title or author."""
    st.subheader("🔎 Find a Book")

    search_query = st.text_input("Enter Book Title or Author Name")
    
    if st.button("Search"):
        df = pd.read_csv(BOOKS_FILE)
        
        if df.empty:
            st.info("📂 No books in the library yet.")
        else:
            results = df[
                df["Title"].str.contains(search_query, case=False, na=False) | #case false ensure that ignore minor spelling error like small h to capital H
                df["Author"].str.contains(search_query, case=False, na=False)
            ]
            
            if results.empty:
                st.warning("❌ No books found matching your search.")
            else:
                st.dataframe(results)


# Route based on selection
if selected_option == "Add a Book":
    add_books()
elif selected_option == "Explore Books":
    explore_books()
elif selected_option == "Find a Book":
    find_books()

