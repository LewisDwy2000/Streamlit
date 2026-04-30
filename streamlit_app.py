import streamlit as st
import json
import base64
import mimetypes
from pathlib import Path

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

# Sidebar logo above the pages list
logo_path = config.get('sidebar_logo') or config.get('banner_logo', '')
logo_width = config.get('sidebar_logo_width', 160)
logo_height = config.get('sidebar_logo_height', 160)
logo_text = config.get('sidebar_logo_text', config.get('title', ''))

try:
    logo_width = int(logo_width)
except (TypeError, ValueError):
    logo_width = 160

try:
    logo_height = int(logo_height)
except (TypeError, ValueError):
    logo_height = 160


def add_logo():
    if not logo_path:
        return

    logo_file = Path(logo_path)
    if logo_file.exists():
        mime_type, _ = mimetypes.guess_type(str(logo_file))
        mime_type = mime_type or 'image/png'
        with open(logo_file, 'rb') as f:
            logo_data = base64.b64encode(f.read()).decode('utf-8')
        background_image = f"url('data:{mime_type};base64,{logo_data}')"
    else:
        background_image = f"url('{logo_path}')"

    st.markdown(
        f"""
        <style>
            [data-testid="stSidebarNav"] {{
                background-image: {background_image};
                background-repeat: no-repeat;
                background-size: {logo_width}px {logo_height}px;
                padding-top: {logo_height + 40}px;
                background-position: center 20px;
            }}
            [data-testid="stSidebarNav"]::before {{
                content: '{logo_text}';
                display: block;
                text-align: center;
                margin-top: 12px;
                font-size: 22px;
                font-weight: 700;
                color: #111827;
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )

with st.sidebar:
    add_logo()
    pg = st.navigation(pages)

pg.run()