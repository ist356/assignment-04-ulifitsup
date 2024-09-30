'''
Solution unibrow.py
'''
import pandas as pd
import streamlit as st
import pandaslib as pl

st.title("UniBrow")
st.caption("The Universal data browser")

# TODO Write code here to complete the unibrow.py

file = st.file_uploader("Upload a file:", type=["csv", "xlsx", "json"])
if file:
    file_ext = pl.get_file_extension(file.name)
    df = pl.load_file(file, file_ext)
    columns = pl.get_column_names(df)
    selected_columns = st.multiselect("Select columns to display", columns, default=columns)
    if st.checkbox("Filter data"):
        stcols = st.columns(3)
        text_columns = pl.get_columns_of_type(df, 'object')
        filter_column = stcols[0].selectbox("Select column to filter", text_columns)
        if filter_column:
            values = pl.get_unique_values(df, filter_column)
            value = stcols[1].selectbox("Select value to filter On", values)
            df_show = df[df[filter_column] == value][selected_columns]
    else:
        df_show = df[selected_columns]