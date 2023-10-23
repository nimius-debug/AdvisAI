from tavily import Client
import streamlit as st

@st.cache_data
def research_query(query):
    tavily = Client(api_key=st.secrets['TAVILY_API_KEY'])
    research_data = tavily.search(query=query, search_depth="basic")
    
    query_of_res = research_data["query"]
    response_time = research_data["response_time"]  
    st.markdown(f"### :mag: Search results for: **{query_of_res}** in {response_time} seconds")
    for result in research_data["results"]:
        title = result["title"]
        content = result["content"]
        url = result["url"]
        score = result["score"]
                
        st.markdown(
    f"""
        <style>
            .css-card {{
                border-radius: 10px;
                padding: 10px;
                background-color: #FFFFFF;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                margin-bottom: 10px;
                font-family: serif;
                color: #000000;
                font-size: 1.1rem;
                display: inline-block;
            }}
            .css-card h3 {{
                color: #1C4E80;
            }}
            .css-card a {{
                color: #1C4E80;
                text-decoration: none;
            }}
            .css-card a:hover {{
                text-decoration: underline;
            }}
        </style>
        <div class="css-card">
            <h3>{title}</h3>
            <p>{content}</p>
            <a href="{url}" target="_blank">Read more</a>
            <br>
            <small>Score: {score}</small>
        </div>
    """,
    unsafe_allow_html=True,
)


def research_topic():
    colums = st.columns((1,4,1))
    with colums[1]:
        st.header(":desktop_computer: :red[Research] Agent")
        st.markdown("##### It scans a variety of trusted sources to ensure that it gathers the most relevant and accurate information tailored to your specific query")
    
        query = st.text_input("",placeholder="What would you like to research:",label_visibility = "hidden")
        if st.button("Search"):
        # For basic search:
            with st.spinner('Searching...'):
               research_query(query)
            
            # For advanced search:
        st.divider()
        st.subheader("Advanced Search Coming Soon")