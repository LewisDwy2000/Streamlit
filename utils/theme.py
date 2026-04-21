import streamlit as st

def apply_color_theme(config):
    """
    Applies a color theme to the Streamlit page based on the provided configuration.

    Args:
        config (dict): Configuration dictionary containing color settings.
                      Expected keys: 'background_color', 'primary_color'
    """
    background_color = config.get('background_color', '#ffffff')
    primary_color = config.get('primary_color', '#ff4b4b')

    st.markdown(
        f"""
        <style>
        /* Set background color for the main content area */
        .stApp {{
            background-color: {background_color} !important;
        }}

        /* Customize primary color for buttons and other elements */
        .stButton>button {{
            background-color: {primary_color} !important;
            color: white !important;
            border: none !important;
        }}
        .stButton>button:hover {{
            background-color: {primary_color} !important;
            opacity: 0.8;
        }}

        /* Additional theme customizations can be added here */
        </style>
        """,
        unsafe_allow_html=True,
    )