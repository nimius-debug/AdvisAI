import streamlit as st
import pandas as pd

def expenses_data_frame():
    return pd.DataFrame ([
            {"Category": "HOUSING", "Subcategory": "Mortgage/Rent", "Amount": 0.0},
            {"Category": "HOUSING", "Subcategory": "Homeowner's/Rental Insurance", "Amount": 0.0},
            {"Category": "HOUSING", "Subcategory": "Real Estate Taxes", "Amount": 0.0},
            {"Category": "HOUSING", "Subcategory": "Maintenance/Repairs", "Amount": 0.0},
            {"Category": "HOUSING", "Subcategory": "Electric", "Amount": 0.0},
            {"Category": "HOUSING", "Subcategory": "Gas", "Amount": 0.0},
            {"Category": "HOUSING", "Subcategory": "Water", "Amount": 0.0},
            {"Category": "HOUSING", "Subcategory": "Trash", "Amount": 0.0},
            {"Category": "HOUSING", "Subcategory": "Telephone/Internet/Cable", "Amount": 0.0},
            {"Category": "AUTO", "Subcategory": "Loan/Lease Payment", "Amount": 0.0},
            {"Category": "AUTO", "Subcategory": "Insurance (Auto)", "Amount": 0.0},
            {"Category": "AUTO", "Subcategory": "Registration/Inspection", "Amount": 0.0},
            {"Category": "AUTO", "Subcategory": "Gasoline/Maintenance", "Amount": 0.0},
            {"Category": "GROCERY", "Subcategory": "Food", "Amount": 0.0},
            {"Category": "GROCERY", "Subcategory": "Cleaning/Paper Supplies", "Amount": 0.0},
            {"Category": "GROCERY", "Subcategory": "Toiletries", "Amount": 0.0},
            {"Category": "GROCERY", "Subcategory": "Baby Care", "Amount": 0.0},
            {"Category": "GROCERY", "Subcategory": "Pet Care", "Amount": 0.0},
            {"Category": "GROCERY", "Subcategory": "Other Grocery Expenses", "Amount": 0.0},
            {"Category": "HEALTHCARE", "Subcategory": "Insurance (Healthcare)", "Amount": 0.0},
            {"Category": "HEALTHCARE", "Subcategory": "Doctor/Dentist", "Amount": 0.0},
            {"Category": "HEALTHCARE", "Subcategory": "RX/Medication", "Amount": 0.0},
            {"Category": "OTHER", "Subcategory": "Debts/Loans", "Amount": 0.0},
            {"Category": "OTHER", "Subcategory": "Savings", "Amount": 0.0},
            {"Category": "OTHER", "Subcategory": "Investments", "Amount": 0.0},
            {"Category": "OTHER", "Subcategory": "Life Insurance", "Amount": 0.0},
            {"Category": "OTHER", "Subcategory": "Child Care", "Amount": 0.0},
            {"Category": "OTHER", "Subcategory": "Clothing", "Amount": 0.0},
            {"Category": "OTHER", "Subcategory": "Dining Out", "Amount": 0.0},
            {"Category": "OTHER", "Subcategory": "Entertainment/Recreation", "Amount": 0.0},
            {"Category": "OTHER", "Subcategory": "Miscellaneous", "Amount": 0.0},
            {"Category": "GIVING", "Subcategory": "Tithe", "Amount": 0.0},
            {"Category": "GIVING", "Subcategory": "Charitable Contributions", "Amount": 0.0},
            {"Category": "INCOME TAXES", "Subcategory": "Federal Income Tax", "Amount": 0.0},
            {"Category": "INCOME TAXES", "Subcategory": "Federal Social Security Tax", "Amount": 0.0},
            {"Category": "INCOME TAXES", "Subcategory": "State Income Tax", "Amount": 0.0},
    ])

def expenses_data_editor():
    return st.data_editor(
            expenses_data_frame(),
            column_config = {
                "Category": st.column_config.SelectboxColumn(
                    "Expense Category",
                    help="Select the expense category",
                    width="medium",
                    options=["GIVING", "INCOME TAXES", "HOUSING", "AUTO", "GROCERY", "HEALTHCARE", "OTHER"],
                ),
                "Amount": st.column_config.NumberColumn(
                "Amount(USD)",
                help="The Amount of Income in USD",
                format="$%d",
                )
            },
            height=300,
            hide_index=True,
            num_rows="dynamic",
        )