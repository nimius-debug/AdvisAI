import streamlit as st
from components.page_settings import horizontal_menu,display_logo,footer
from components.forms import get_response_jscomponent

from app_pages.budget import budget
from app_pages.email_automation import email_automation
from app_pages.research_agent import research_topic
###################################################page config###############################################

st.set_page_config(
    page_title="NexaStack",
    page_icon=':rocket:',
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'mailto:jag.solutionshub@gmail.com',
        'Report a bug': "mailto:jag.solutionshub@gmail.com",
        'About': "Welcome to your NexaStack!. \
            The NexaStack is a comprehensive suite of tools designed to assist marketers in managing and\
            optimizing their marketing efforts. It provides a range of functionalities and features to streamline \
            marketing tasks, track performance, and make data-driven decisions. Whether you're a digital marketer,\
            brand manager, or marketing strategist, the Marketer Toolbox offers a set of essential tools to enhance\
            your marketing campaigns and drive better results."
    }
)

################################################ main app ################################################
def main():
    with st.sidebar:
        st.write("(beta)")
        display_logo()
        selected = horizontal_menu()
        st.divider()
        st.caption(':mailbox: Upcoming features will be available to a limited number of users. Get a reminder when these exclusive features become available. ')
        get_response_jscomponent()
        st.divider()
        footer()
        

        
    if selected == "Ads Budget":
        budget()
    elif selected == "Trendy Agent":
        email_automation()
    elif selected == "Research Agent":
        research_topic()    
    
    elif selected =="Settings":
        st.header("Integration (Coming Soon))")
        coln1, coln2 = st.columns(2)
        with coln1:
            with st.expander(":email: GetResponse"):
                GET_RESPONSE = st.text_input("Enter your GETRESPONSE API KEY here: ", value="Coming Soon")
                # GR_key_message = "GetResponse key was accepted!"
                # st.write(GR_key_message)
        with coln2:
            with st.expander(":brain: OpenAI"):
                OPEN_AI = st.text_input("Enter your OPENAI API KEY here: ", value="Coming Soon")
                # openai.api_key = OPEN_AI
            # model_id = 'gpt-3.5-turbo'
            #AI_key_message = "Open AI key was accepted!"
if __name__ == "__main__":
    main()

    

