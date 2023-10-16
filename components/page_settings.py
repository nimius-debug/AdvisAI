import streamlit as st
import base64
from PIL import Image
from streamlit_option_menu import option_menu

    
#########################horizontal bar#########################
def horizontal_menu():
    # Configuration for static values
    MENU_OPTIONS = ["Ads Budget", "Automation Agent", 'Settings']
    MENU_ICONS = ['speedometer2', "filetype-ai", 'gear']
    MENU_STYLES = {
        "container": {
            "padding": "10px!important",
            "background-color": "#F1F1F1",  # Background color matches your theme
            "border": "2px solid #1C4E80",  # Border color matches your theme
        },
        "icon": {
            "color": "#1C4E80",  # Primary color matches your theme
            "font-size": "16px",
            "margin-right": "5px",
        },
        "nav-link": {
            "font-size": "16px",
            "text-align": "left",
            "margin": "5px 0",
            "padding": "5px 10px",
            "--hover-color": "#FFFFFF",  # Hover color matches your theme
        },
        "nav-link-selected": {
            "background-color": "#FFFFFF",  # Selected background color matches your theme
            "color": "#000000",  # Text color matches your theme
            "border-left": "4px solid #1C4E80",  # Border color matches your theme
        }
    }

    
    return option_menu(None, MENU_OPTIONS, icons=MENU_ICONS, menu_icon="cast", default_index=0, styles=MENU_STYLES)
#########################BACKGROUND  #########################

#########################image to base64 background #########################
@st.cache_data
def get_img_as_base64(file_pic):
    with open(file_pic, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

@st.cache_data
def set_backgound_img():
    img = get_img_as_base64("img/bg.png")
    print('background image')
    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
        background-image: url("data:image/png;base64,{img}");
        background-size: cover;
        background-position: top left;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    [data-testid="stSidebar"] > div:first-child {{
        background-color: #EDEDED;");
        background-position: center; 
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
.css-1y4p8pa
    [data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
    }}

    [data-testid="stToolbar"] {{
    right: 2rem;
    }}
    
    .css-1y4p8pa {{
        padding: 1rem 1rem 10rem
    }}
    data
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)
#########################logo#########################
@st.cache_data
def footer():
    ft = """
    <style>
        a:link , a:visited{
            color: #BFBFBF;  /* theme's text color hex code at 75 percent brightness*/
            background-color: transparent;
            text-decoration: none;
        }

        a:hover,  a:active {
            color: #383b3a; /* theme's primary color*/
            background-color: transparent;
            text-decoration: underline;
        }

        #page-container {
            position: relative;
            min-height: 10vh;
        }

        footer{
            visibility:hidden;
        }

        .footer {
            font-size: 1rem; /* equals 14px */
            position: relative;
            left: 0;
            top:300px;
            bottom: 0;
            width: 100%;
            background-color: transparent;
            color: #808080; /* theme's text color hex code at 50 percent brightness*/
            text-align: center; /* you can replace 'left' with 'center' or 'right' if you want*/
        }
    </style>

    <div id="page-container">
        <div class="footer">
            <p style='font-size: 0.875em;'>Made with <img src="https://em-content.zobj.net/source/skype/289/red-heart_2764-fe0f.png" alt="heart" height= "10"/><a style='display: inline; text-align: left;' href="https://github.com/nimius-debug" target="_blank"> by Jorge A Gil</a></p>
        </div>
    </div>
    """
    st.markdown(ft,unsafe_allow_html=True)
#########################logo#########################

def display_logo():
    """
    Displays the logo in the streamlit app.
    """
    col1, col2, col3 = st.columns([1,2,1])

    with col1:
        st.write(' ')

    with col2:
        logo = Image.open('img/logo.png')
        st.image(logo, use_column_width= "auto")

    with col3:
        st.write(' ')
        
        