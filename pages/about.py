import streamlit as st
import json
from ui.banner import apply_banner
from utils.theme import apply_color_theme

# Load configuration
with open('config/config.json', 'r') as f:
    config = json.load(f)

# Apply color theme
apply_color_theme(config)

# Apply banner
apply_banner(config)

st.write("About Us")
st.write("This page contains information about the application.")