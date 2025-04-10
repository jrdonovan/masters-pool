import streamlit as st
from typing import Any


def get_secret(key: str):
    """
    Fetches a secret from the Streamlit secrets.
    """
    if key in st.secrets:
        return st.secrets[key]
    else:
        raise KeyError(f"Secret '{key}' not found in Streamlit secrets.")


def session_key_exists(key: str) -> bool:
    """
    Checks if a key exists in the Streamlit session state.
    """
    return (key in st.session_state) and (st.session_state[key] is not None)


def set_session_state(key: str, value: Any) -> None:
    """
    Sets a value in the Streamlit session state.
    """
    st.session_state[key] = value


def get_session_state(key: str = None):
    """
    Fetches a value from the Streamlit session state.
    """
    if key:
        if key in st.session_state:
            return st.session_state[key]
        else:
            raise KeyError(f"Key '{key}' not found in Streamlit session state.")
    else:
        return st.session_state
