import streamlit as st
state = st.session_state
import pandas as pd

from scripts import tools
tools.page_config()


bbip_demo = 'https://docs.google.com/spreadsheets/d/1Rwosz1-ZvQlIJX1YBph9IAcHNQ5S0oXeMoKY7RZBxsM/edit#gid=0'

df = tools.get_google_sheet(bbip_demo)

st.write('# HBW metadata demo')
st.write('**Full database**')
st.write(df.head())


with st.expander('Filter the database to include specific columns'):
    with st.form(key=f'md_elements_form'):

        st.write("""*These are all of the columns in the database. Select ones to
        include in a filtered sheet.*""")

        cols_to_include = []

        md_els_cols = st.columns(3)
        for i,c in enumerate(df.columns):

            n = i % 3
            with md_els_cols[n]:
                btn = st.checkbox(c)
            if btn:
                cols_to_include.append(c)

        md_elements_button = st.form_submit_button(label='Update sheet')

if md_elements_button:

    if cols_to_include == []:
        cols_to_include = df.columns
    df_filtered = df[cols_to_include]
    st.write(df_filtered.head())
    st.download_button(label="Download filtered data as CSV",
                    data=df_filtered.to_csv(index=None).encode('utf-8'),
                    file_name='bbip_demo.csv',mime='text/csv')
