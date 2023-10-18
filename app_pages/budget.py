import streamlit as st
import matplotlib.pyplot as plt
# import base64
# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas
# import dataframe_image as dfi
from components.income_df import income_data_editor 
from components.expenses_df import expenses_data_editor


def budget():
    st.header('Ads Budget')
    st.write('Add your monthly income and expenses to calculate your marketing ads budget.')
    st.caption('(credits Ray Kakuda -> Fullstaq Marketer Monthly Marketing Budget Sheet)')
    st.markdown("""---""")
    #****************************income ********************************************************************************
    col1, col2 = st.columns([1, 1], gap="large")
    with col1:
        st.subheader('Monthly Income')
        df_in_editor = income_data_editor()
        print(df_in_editor)
    #****************************expenses ********************************************************************************
    
    with col2:
        st.subheader('Monthly Expenses')
        df_exp = expenses_data_editor()
        
    #****************************budget ********************************************************************************
    st.header('Ads Budget - Breakdown')
    st.divider()
    
    #****************************pie chart ********************************************************************************
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
        # plt.savefig('piechart.png')
        pie_col, breakdown_col = st.columns([1, 1],gap="large")
       
    #****************************display pie ********************************************************************************
        with pie_col:
            st.pyplot(fig1,use_container_width=True)
            marketing_budget_percent = st.slider('Percent of Disposable Income for Marketing',format="%d%%", min_value=0, max_value=1, value=100, step=1, key='marketing_budget_percent')
            monthly_marketing_budget = disposable_income * marketing_budget_percent/100
            daily_budget = monthly_marketing_budget / 30
    
    #****************************display breakdown ********************************************************************************
        with breakdown_col:
            st.subheader(f'Total Income: ----> :blue[ ${total_income:,.2f}]')
            st.subheader(f'Total Expenses:----> :orange[ ${total_expenses:,.2f}]')
            st.subheader(f'Disposable Income:----> :green[${disposable_income:,.2f}]')
            st.divider()
            
            st.subheader(f'Monthly Marketing Budget: ${monthly_marketing_budget:,.2f}')
            st.subheader(f'Daily Ads Budget: ${daily_budget:,.2f}')
           
    else:
        st.warning('You have no money too spend on ads, consider getting a job!')
    # combine the income and expenses dataframes into one for the report
 