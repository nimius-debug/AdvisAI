import streamlit as st

@st.cache_data
def style_google_trends():
    st.markdown(
        """
        <style>
            /*#MainMenu {visibility: hidden;}
            footer {visibility: hidden;}*/
            .css-card {
                border-radius: 10px;
                padding: 10px;
                background-color: #1C4E80;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                margin-bottom: 10px;
                font-family: serif;
                color: white;
                font-size: 1.1rem;
                display: inline-block;
            }
            
        </style>
        """,
        unsafe_allow_html=True,
    )