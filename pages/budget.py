import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# import base64
# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas
# import dataframe_image as dfi
from components.income_df import income_data_editor 
from components.expenses_df import expenses_data_editor

# def get_table_download_link(df, filename):
#     """Generates a link allowing the data in a given pandas dataframe to be downloaded
#     in:  dataframe
#     out: download link
#     """
#     csv = df.to_csv(index=False)
#     b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
#     href = f'<a href="data:file/csv;base64,{b64}" download="{filename}.csv">Download {filename} as CSV</a>'
#     return href

# def create_pdf():
#     c = canvas.Canvas("BudgetReport.pdf", pagesize=letter)
#     width, height = letter

#     # Add images
#     c.drawImage('piechart.png', 0, height - 400, 400, 400)  # pie chart
#     c.drawImage('df_income.png', 0, height - 800, 400, 400)  # income data
#     c.drawImage('df_expenses.png', 0, height - 1200, 400, 400)  # expenses data

#     # Add some text data
#     c.drawString(0, height - 1220, "Total Income: $" + str(total_income))
#     c.drawString(0, height - 1240, "Total Expenses: $" + str(total_expenses))
#     c.drawString(0, height - 1260, "Disposable Income: $" + str(disposable_income))
#     c.drawString(0, height - 1280, "Monthly Marketing Budget: $" + str(monthly_marketing_budget))
#     c.drawString(0, height - 1300, "Daily Budget: $" + str(daily_budget))

#     c.save()
def budget():
    # st.markdown('<style> .css-ue6h4q { color: green; }.css-16idsys p </style>', unsafe_allow_html=True)
    st.set_page_config(
        page_title="JAG ToolBox",
        page_icon=':rocket:',
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            'Get Help': 'mailto:jag.solutionshub@gmail.com',
            'Report a bug': "mailto:jag.solutionshub@gmail.com",
            'About': "Welcome to your Marketer ToolBox!. \
                The Marketer Toolbox is a comprehensive suite of tools designed to assist marketers in managing and\
                optimizing their marketing efforts. It provides a range of functionalities and features to streamline \
                marketing tasks, track performance, and make data-driven decisions. Whether you're a digital marketer,\
                brand manager, or marketing strategist, the Marketer Toolbox offers a set of essential tools to enhance\
                your marketing campaigns and drive better results."
        }
    )
    with st.sidebar:
        st.write('## JAG ToolBox')
    
    st.title('Monthly Marketing Budget Calculator')
    # col1, col2 = st.columns(2,gap="large")
    # with col1:
    st.header('Monthly Income and Expenses')
    
    #****************************income ********************************************************************************
    col1, col2 = st.columns(2,gap="small")
    with col1:
        st.subheader('Income')
        df_in_editor = income_data_editor()
        print(df_in_editor)
    #****************************expenses ********************************************************************************
    
    with col2:
        st.subheader('Expenses')
        df_exp = expenses_data_editor()
        
    st.markdown("""---""")
    total_income = df_in_editor["Amount"].sum()
    total_expenses = df_exp["Amount"].sum()
    
    disposable_income = total_income - total_expenses
    
    if disposable_income > 0:
        labels = 'Total Income', 'Total Expenses', 'Disposable Income'
        amount = [total_income, total_expenses, disposable_income]
        explode = (0, 0, 0.1) 
        fig1, ax1 = plt.subplots()
        ax1.pie(amount, explode=explode, labels=labels, autopct=lambda p: '{:.0f}'.format(p * sum(amount) / 100),
                shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.savefig('piechart.png')
        pie_col, breakdown_col = st.columns([1, 1],gap="large")
        with pie_col:
            st.pyplot(fig1)
            marketing_budget_percent = st.slider('Percent of Disposable Income for Marketing',format="%d%%", min_value=0, max_value=1, value=100, step=1, key='marketing_budget_percent')
            monthly_marketing_budget = disposable_income * marketing_budget_percent/100
            daily_budget = monthly_marketing_budget / 30
        with breakdown_col:
            st.header('TOTAL BREAKDOWN')
            st.write(f'Total Income: ${total_income:,.2f}')
            st.write(f'Total Expenses: ${total_expenses:,.2f}')
            st.write(f'Disposable Income: ${disposable_income:,.2f}')
            st.header('Monthly Marketing Budget')
            st.write(f'Monthly Marketing Budget: ${monthly_marketing_budget:,.2f}')
            st.write(f'Daily Budget: ${daily_budget:,.2f}')
            if st.button('Generate Report'):
                create_pdf()

    else:
        st.error('You have no money too spend on ads, get a job!')
    # combine the income and expenses dataframes into one for the report
   
if __name__ == '__main__':
    budget()