import streamlit as st
import json

# Load configuration
with open('config/config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

# Set page configuration
st.set_page_config(
    page_title=config['title'],
    layout='wide'
)

# Load pages configuration
with open('config/pages.json', 'r', encoding='utf-8') as f:
    pages_config = json.load(f)

# Sort pages by page_order
pages_config.sort(key=lambda x: x['page_order'])

# Create pages list
pages = [
    st.Page(p['page_path'], title=p['page_title'], icon=p['icon'])
    for p in pages_config
]

# Navigation
pg = st.navigation(pages)
pg.run()