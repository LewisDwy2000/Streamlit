import streamlit as st
import json
from ui.banner import apply_banner

# Load configuration
with open('config/config.json', 'r') as f:
    config = json.load(f)

# Apply banner
apply_banner(config)

st.write("About Us")
st.write("This page contains information about the application.")