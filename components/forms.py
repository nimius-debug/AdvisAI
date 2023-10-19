import streamlit as st

@st.cache_data
def styleform_css():
    contact_form_style = f"""
    <style>
        input[type=text], input[type=email] {{
            width: 100%; /* Full width */
            padding: 12px; /* Some padding */ 
            border: 1px solid #ccc; /* Gray border */
            border-radius: 4px; /* Rounded borders */
            box-sizing: border-box; /* Make sure that padding and width stays in place */
            margin-top: 10px; /* Add a top margin */
            margin-bottom: 16px; /* Bottom margin */
            
            font-family: serif; /* Match the font with your theme */
        }}

        button[type=submit] {{
            background-color: #1C4E80; /* Matched with your primaryColor */
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-family: serif; /* Match the font with your theme */
        }}

        /* When moving the mouse over the submit button, add a slightly darker shade of your primaryColor */
        button[type=submit]:hover {{
            background-color: #000000;
        }}
    </style>
    """
    st.markdown(contact_form_style, unsafe_allow_html=True)

@st.cache_data
def get_response_jscomponent():
    styleform_css()
    html_string = '''
    <form action="https://formsubmit.co/el/gayura" method="POST">
        <input type="email" name="email" placeholder="Email*" required>
        <button type="submit">Remind Me</button>
    </form>
    '''
    st.markdown(html_string, unsafe_allow_html=True) 
    