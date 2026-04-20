import streamlit as st
import json
from ui.banner import apply_banner

# Load configuration
with open('config/config.json', 'r') as f:
    config = json.load(f)

# Apply banner
apply_banner(config)

st.write("Welcome to the Home Page!")
st.write("This is the main page of the application.")