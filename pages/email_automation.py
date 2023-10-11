import requests
import streamlit as st

def fetch_categories():
    """Fetch available book categories from Google Books API"""
    base_url = "https://www.googleapis.com/books/v1/volumes"
    params = {
        "q": "category:all",
        "maxResults": 1
    }
    response = requests.get(base_url, params=params)
    categories = response.json().get("items", [])
    if categories:
        return categories[0]["volumeInfo"]["categories"]
    return []

def fetch_books(category, order_by='relevance'):
    """Fetch books by category from Google Books API"""
    base_url = "https://www.googleapis.com/books/v1/volumes"
    books = []
    max_results = 40  # Maximum results per page

    while len(books) < 100:
        params = {
            "q": f"subject:{category}",
            "printType": "books",
            "maxResults": max_results,
            "startIndex": len(books),
            "orderBy": order_by
        }
        response = requests.get(base_url, params=params)
        response_data = response.json().get("items", [])
        # Filter out books with less than 100 ratings
        response_data = [book for book in response_data if book["volumeInfo"].get("ratingsCount", 0) >= 100]
        books.extend(response_data)

        if len(response_data) < max_results:
            break  # Reached the end of results

    # Sort the books by ratingsCount in descending order
    sorted_books = sorted(books, key=lambda x: (
        x["volumeInfo"].get("ratingsCount", 0),
    ), reverse=True)

    return sorted_books[:100]  # Return up to 100 books


def display_books(books):
    """Display books information"""
    for book in books:
        volume_info = book["volumeInfo"]
        st.subheader(volume_info.get("title", "Title Not Available"))
        st.write("Authors:", ", ".join(volume_info.get("authors", ["Author Not Available"])))
        st.write("Publisher:", volume_info.get("publisher", "Publisher Not Available"))
        st.write("Published Date:", volume_info.get("publishedDate", "Publish Date Not Available"))
        st.write("Description:", volume_info.get("description", "Description Not Available"))
        image_links = volume_info.get("imageLinks")
        if image_links is not None:
            st.image(image_links.get("thumbnail", ""))
        st.write("Average Rating:", volume_info.get("averageRating", "Not Available"))
        st.write("Ratings Count:", volume_info.get("ratingsCount", "Not Available"))


def main():
    st.title("Book Search")

    # Fetch available categories
    categories = fetch_categories()

    if categories:
        category = st.selectbox("Select a category", categories)
        order_by = st.selectbox("Order by", ["relevance", "newest"])

        if st.button("Search"):
            books = fetch_books(category, order_by=order_by)
            if books:
                display_books(books)
    else:
        st.write("No categories available.")


if __name__ == "__main__":
    main()
