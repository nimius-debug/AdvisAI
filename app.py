import streamlit as st
from components.page_settings import horizontal_menu,display_logo,footer
from app_pages.budget import budget
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
        footer()
        
    if selected == "Ads Budget":
        budget()
        
        
    
if __name__ == "__main__":
    main()

    

