import streamlit as st
import json
from ui.banner import apply_banner, apply_header_strip
from utils.products import PRODUCTS, get_product
from utils.theme import apply_color_theme

# Load configuration
with open('config/config.json', 'r') as f:
    config = json.load(f)

# Apply color theme
apply_color_theme(config)

# Apply header strip and banner
apply_header_strip(config)
apply_banner(config)

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="UI Demo",
    page_icon="◻",
    layout="wide",
)


with st.container(key="about_main_container"):
    st.markdown(
        """ <style>
        .st-key-about_main_container {
        color: #FFFFFF;
        background-color: #FFFFFF;
        height: 100vh;
        width: 100vw;
        }
        </style>
        """,  unsafe_allow_html=True,
    )
    st.markdown('<div> st-key-about_main_container </div>', unsafe_allow_html=True)
    st.title("About Us")
    st.write("This page contains information about the application.")
    st.html("""<style>
        .horizontal-bar {
            width: 400px;
            height: 30px;
            background-color: #ffffff;
        }
    </style>
</head>
 
<body>
    <div class="horizontal-bar"></div>
</body>
        """)

# Create a full-width white background container
with st.container(key="wide_container"):        
    st.markdown(
        """
        <style>
        .about-container {
            background-color: white;
            font-color: black;
            padding: 64px;
            border-radius: 12px;
            margin: 20px calc(-50vw + 50%) 20px calc(-50vw + 50%);
            width: 100vw;
            max-width: none;
            box-sizing: border-box;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    # Apply the container styling
    st.markdown('<div class="about-container">', unsafe_allow_html=True)
        
    if st.button("Learn more about our company", key="company_info_btn"):
        st.write("We are a leading provider of innovative solutions designed to help businesses succeed in the digital age.")
    
    # Add slider
    st.markdown("**Select a value:**")
    slider_value = st.slider("Company rating", min_value=0, max_value=100, value=50, key="company_slider")
    st.write(f"You selected: {slider_value}%")
        
    # Company Info Section
    with st.container(border=True):
        st.subheader("Company Information")
        st.write("We are a leading provider of innovative solutions designed to help businesses succeed in the digital age.")

    # Mission Section
    with st.container(border=True):
        st.subheader("Our Mission")
        st.write("To deliver exceptional value through cutting-edge technology, outstanding customer service, and continuous innovation.")

    # Contact Section
    with st.container(border=True):
        st.subheader("Get in Touch")
        st.write("Have questions? We'd love to hear from you!")
    
    st.markdown('</div>', unsafe_allow_html=True)
    

