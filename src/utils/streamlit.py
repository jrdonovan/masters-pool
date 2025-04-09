import streamlit as st

def get_secret(key: str):
    """
    Fetches a secret from the Streamlit secrets.
    """
    if key in st.secrets:
        return st.secrets[key]
    else:
        raise KeyError(f"Secret '{key}' not found in Streamlit secrets.")
