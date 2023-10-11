import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
def main():
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
    col1, col2 = st.columns(2,gap="large")
    with col1:
        with st.expander('TOTAL MONTHLY INCOME (GROSS)', expanded=True):
           
            salaries = st.number_input('Enter your Salaries/Wages', min_value=0.0, value=0.0, step=100.0, key='salaries')
            interest_dividends = st.number_input('Enter your Interest/Dividends', min_value=0.0, value=0.0, step=100.0, key='interest_dividends')
            other_income = st.number_input('Enter Other Income', min_value=0.0, value=0.0, step=100.0, key='other_income')
            total_income = salaries + interest_dividends + other_income
            
            
        st.header('Expenses')
        with st.expander('GIVING'):
            
            tithe = st.number_input('Enter Tithe', min_value=0.0, value=0.0, step=100.0, key='tithe')
            charitable_contributions = st.number_input('Enter Charitable Contributions', min_value=0.0, value=0.0, step=100.0, key='charitable_contributions')
        with st.expander('INCOME TAXES'):
            federal_income_tax = st.number_input('Enter Federal Income Tax', min_value=0.0, value=0.0, step=100.0, key='federal_income_tax')
            federal_social_security_tax = st.number_input('Enter Federal Social Security Tax', min_value=0.0, value=0.0, step=100.0, key='federal_social_security_tax')
            state_income_tax = st.number_input('Enter State Income Tax', min_value=0.0, value=0.0, step=100.0, key='state_income_tax')
        with st.expander('HOUSING'):
            mortgage_rent = st.number_input('Enter Mortgage/Rent', min_value=0.0, value=0.0, step=100.0, key='mortgage_rent')
            insurance_housing = st.number_input('Enter Homeowner\'s/Rental Insurance', min_value=0.0, value=0.0, step=100.0, key='insurance_housing')
            real_estate_taxes = st.number_input('Enter Real Estate Taxes', min_value=0.0, value=0.0, step=100.0, key='real_estate_taxes')
            maintenance_repairs = st.number_input('Enter Maintenance/Repairs', min_value=0.0, value=0.0, step=100.0, key='maintenance_repairs')
            electric = st.number_input('Enter Electric', min_value=0.0, value=0.0, step=100.0, key='electric')
            gas = st.number_input('Enter Gas', min_value=0.0, value=0.0, step=100.0, key='gas')
            water = st.number_input('Enter Water', min_value=0.0, value=0.0, step=100.0, key='water')
            trash = st.number_input('Enter Trash', min_value=0.0, value=0.0, step=100.0, key='trash')
            telephone_internet_cable = st.number_input('Enter Telephone/Internet/Cable', min_value=0.0, value=0.0, step=100.0, key='telephone_internet_cable')
        with st.expander('AUTO'):
            loan_lease_payment = st.number_input('Enter Loan/Lease Payment', min_value=0.0, value=0.0, step=100.0, key='loan_lease_payment')
            insurance_auto = st.number_input('Enter Insurance', min_value=0.0, value=0.0, step=100.0, key='insurance_auto')
            registration_inspection = st.number_input('Enter Registration/Inspection', min_value=0.0, value=0.0, step=100.0, key='registration_inspection')
            gasoline_maintenance = st.number_input('Enter Gasoline/Maintenance', min_value=0.0, value=0.0, step=100.0, key='gasoline_maintenance')
        with st.expander('GROCERY'):
            food = st.number_input('Enter Food', min_value=0.0, value=0.0, step=100.0, key='food')
            cleaning_paper_supplies = st.number_input('Enter Cleaning/Paper Supplies', min_value=0.0, value=0.0, step=100.0, key='cleaning_paper_supplies')
            toiletries = st.number_input('Enter Toiletries', min_value=0.0, value=0.0, step=100.0, key='toiletries')
            baby_care = st.number_input('Enter Baby Care', min_value=0.0, value=0.0, step=100.0, key='baby_care')
            pet_care = st.number_input('Enter Pet Care', min_value=0.0, value=0.0, step=100.0, key='pet_care')
            other_grocery = st.number_input('Enter Other Grocery Expenses', min_value=0.0, value=0.0, step=100.0, key='other_grocery')
        with st.expander('HEALTHCARE'):
            insurance_healthcare = st.number_input('Enter Insurance', min_value=0.0, value=0.0, step=100.0, key='insurance_healthcare')
            doctor_dentist = st.number_input('Enter Doctor/Dentist', min_value=0.0, value=0.0, step=100.0, key='doctor_dentist')
            rx_medication = st.number_input('Enter RX/Medication', min_value=0.0, value=0.0, step=100.0, key='rx_medication')
        with st.expander('OTHER'):
            debts_loans = st.number_input('Enter Debts/Loans', min_value=0.0, value=0.0, step=100.0, key='debts_loans')
            savings = st.number_input('Enter Savings', min_value=0.0, value=0.0, step=100.0, key='savings')
            investments = st.number_input('Enter Investments', min_value=0.0, value=0.0, step=100.0, key='investments')
            life_insurance = st.number_input('Enter Life Insurance', min_value=0.0, value=0.0, step=100.0, key='life_insurance')
            child_care = st.number_input('Enter Child Care', min_value=0.0, value=0.0, step=100.0, key='child_care')
            clothing = st.number_input('Enter Clothing', min_value=0.0, value=0.0, step=100.0, key='clothing')
            dining_out = st.number_input('Enter Dining Out', min_value=0.0, value=0.0, step=100.0, key='dining_out')
            entertainment_recreation = st.number_input('Enter Entertainment/Recreation', min_value=0.0, value=0.0, step=100.0, key='entertainment_recreation')
            miscellaneous = st.number_input('Enter Miscellaneous', min_value=0.0, value=0.0, step=100.0, key='miscellaneous')

        total_expenses = (
            tithe + charitable_contributions + federal_income_tax + federal_social_security_tax + state_income_tax +
            mortgage_rent + insurance_housing + real_estate_taxes + maintenance_repairs + electric + gas + water + trash +
            telephone_internet_cable + loan_lease_payment + insurance_auto + registration_inspection + gasoline_maintenance +
            food + cleaning_paper_supplies + toiletries + baby_care + pet_care + other_grocery + insurance_healthcare + doctor_dentist +
            rx_medication + debts_loans + savings + investments + life_insurance + child_care + clothing + dining_out +
            entertainment_recreation + miscellaneous
        )
        disposable_income = total_income - total_expenses
    with col2:
        st.header('TOTAL BREAKDOWN')
        st.write(f'Total Income: ${total_income:,.2f}')
        st.write(f'Total Expenses: ${total_expenses:,.2f}')
        st.write(f'Disposable Income: ${disposable_income:,.2f}')
        # Pie chart, where the slices will be ordered and plotted counter-clockwise:
        labels = 'Total Income', 'Total Expenses', 'Disposable Income'
        amount = [total_income, total_expenses, disposable_income]
        explode = (0, 0, 0.1) 

        fig1, ax1 = plt.subplots()
        ax1.pie(amount, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        st.pyplot(fig1)
        st.header('Monthly Marketing Budget')
        marketing_budget_percent = st.slider('Percent of Disposable Income for Marketing', min_value=0.0, max_value=1.0, value=0.10, step=0.01, key='marketing_budget_percent')
        monthly_marketing_budget = disposable_income * marketing_budget_percent
        daily_budget = monthly_marketing_budget / 30

        st.write(f'Monthly Marketing Budget: ${monthly_marketing_budget:,.2f}')
        st.write(f'Daily Budget: ${daily_budget:,.2f}')

        
        
if __name__ == "__main__":
    main()
