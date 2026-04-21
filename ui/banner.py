import base64
import pathlib
import streamlit as st

def apply_banner(config):
    """
    Applies the custom banner with optional logo and background color from config.
    """
    banner_logo = config.get('banner_logo', '')
    banner_spacing = config.get('banner_bottom_spacing', 20)

    # Prepare logo HTML
    logo_html = ''
    if banner_logo and pathlib.Path(banner_logo).exists():
        try:
            with open(banner_logo, 'rb') as f:
                logo_data = base64.b64encode(f.read()).decode()
            logo_html = f'<img src="data:image/png;base64,{logo_data}" class="banner-logo" alt="logo">'
        except Exception as e:
            st.warning(f"Failed to load logo: {e}")

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
            margin-bottom: {banner_spacing}px;
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
            {logo_html}
            <div class="banner-text">{config['banner']}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )