import streamlit as st
import openai
from pytrends.request import TrendReq
from components.trends import get_realtime_trends, get_x_trends, AI_analyze_trends
from styles.style_components import style_google_trends

@st.cache_data(show_spinner=False)
def split_cards(trends: list, start_idx: int, end_idx: int)-> None:

    for i, trend in enumerate(trends[start_idx:end_idx], start=start_idx + 1):
        st.markdown(
            f"""
            <div class="css-card">
                <span >{i}. {trend}</span>
            </div>
            """,
            unsafe_allow_html=True,
        )
    

def email_automation():
    style_google_trends()
    st.header(":chart_with_upwards_trend: Trendy :red[ Zone] ")
    
    # Display trends for the current page
    trends = get_realtime_trends()
    xtrends = get_x_trends()
    
    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.markdown("##### Top real-time searches on X(Twitter))")
        st.dataframe(xtrends, use_container_width=True, height=600)

    # Display trends for the current page
    with col2:
        st.markdown("##### Top real-time searches on Google Trends (US)")
        cards_per_page = 8
        total_pages = (
            int(len(trends) / cards_per_page) if int(len(trends) / cards_per_page) > 0 else 1
        )

        current_page = st.number_input(
            "Page", min_value=1, max_value=total_pages, step=1
        )
            
        start_idx = (current_page - 1) * cards_per_page
        end_idx = start_idx + cards_per_page
        
        split_cards(trends, start_idx, end_idx)
        # Set up pagination outside the if btn_trends block
        st.markdown(f"Page **{current_page}** of **{total_pages}** ")
        
    st.write('power by Google Trends & X(Twitter)')
    st.divider()
    st.markdown("### :robot_face: Let :red[AI Analyze] the trends for you!")
    st.markdown("The AI analyzes trends from GoogleTrends and Twitter, providing top topics to keep your audience engaged.")
    ai_analize = st.button("Analyze")
    list_xtrends = xtrends.values.tolist()
   
    if ai_analize:
        list_xtrends = xtrends.values.tolist()
        AI_analyze_trends(list_xtrends, trends)
    
    st.divider()
    
    st.header("Integration")
    coln1, coln2 = st.columns(2)
    with coln1:
        with st.expander(":email: GetResponse"):
            GET_RESPONSE = st.text_input("Enter your GETRESPONSE API KEY here: ", value="Coming Soon")
            # GR_key_message = "GetResponse key was accepted!"
            # st.write(GR_key_message)
    with coln2:
        with st.expander(":brain: OpenAI"):
            OPEN_AI = st.text_input("Enter your OPENAI API KEY here: ", value="Coming Soon")
            openai.api_key = OPEN_AI
        model_id = 'gpt-3.5-turbo'
        #AI_key_message = "Open AI key was accepted!"