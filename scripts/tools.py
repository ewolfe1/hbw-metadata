import streamlit as st
import pandas as pd

# set page configuration. Can only be set once per session and must be first st command called
def page_config():

    try:
        st.set_page_config(page_title='HBW Novel Metadata', page_icon=':book:', layout='wide')
    except st.errors.StreamlitAPIException as e:
        if "can only be called once per app" in e.__str__():
            return


def get_google_sheet(url):

    url = url.replace('/edit#gid=', '/export?format=csv&gid=')
    df = pd.read_csv(url)
    df = df.dropna(how='all')

    return df
