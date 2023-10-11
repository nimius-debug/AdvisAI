import pandas as pd
import streamlit as st
def income_data_frame():
    return pd.DataFrame ([
            {"Category": "Salaries/Wages", "Amount": 0.0},
            {"Category": "Interest/Dividends", "Amount": 0.0},
            {"Category": "Other Income", "Amount": 0.0},
            ])

def income_data_editor():
    return st.data_editor(
            income_data_frame(),
            column_config={
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