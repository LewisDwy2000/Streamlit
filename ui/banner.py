import base64
import pathlib

import streamlit as st


def _resolve_logo_src(path):
    path = path.strip()
    if not path:
        return ''
    if path.startswith('http://') or path.startswith('https://'):
        return path
    asset_path = pathlib.Path(path)
    if not asset_path.is_file():
        return ''
    encoded = base64.b64encode(asset_path.read_bytes()).decode('utf-8')
    ext = asset_path.suffix.lstrip('.').lower()
    return f'data:image/{ext};base64,{encoded}'


def apply_banner(config):
    """
    Applies the custom banner with optional logo and background color from config.
    """
    banner_logo = _resolve_logo_src(config.get('banner_logo', ''))

    st.markdown(
        f"""
        <style>
        .banner-row {{
            background-color: {config['banner_bg_color']};
            color: white;
            padding: 15px 20px;
            display: flex;
            align-items: center;
            gap: 16px;
            border-radius: 10px;
            margin-bottom: 20px;
        }}
        .banner-logo {{
            height: 48px;
            width: auto;
            display: block;
        }}
        .banner-text {{
            font-size: 28px;
            font-weight: bold;
            margin: 0;
            line-height: 1.2;
        }}
        </style>
        <div class="banner-row">
            {f'<img src="{banner_logo}" class="banner-logo" alt="logo">' if banner_logo else ''}
            <div class="banner-text">{config['banner']}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )