import json
import streamlit as st
from ui.banner import apply_banner, apply_header_strip
from utils.products import PRODUCTS, get_product, get_risk_color, get_risk_label
from utils.theme import apply_color_theme

# Load configuration
with open('config/config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

# Apply color theme, header strip, and banner
apply_color_theme(config)
apply_header_strip(config)
apply_banner(config)

st.set_page_config(
    page_title=f"{config['title']} - Options",
    layout='wide'
)

if 'selected_product_id' not in st.session_state:
    st.session_state.selected_product_id = ''

selected_id = st.session_state.get('selected_product_id', '')

if selected_id:
    # Show product details
    product = get_product(selected_id)
    if product:
        st.title('Product Details')
        st.subheader(product['name'])
        st.write(product['details'])

        st.markdown('**Key features:**')
        for feature in product['features']:
            st.write(f'- {feature}')

        st.markdown(f"**Price:** {product['price']}")
        st.markdown('---')

        if st.button('Back to product list'):
            st.session_state.selected_product_id = ''
    else:
        st.error("Product not found.")
        if st.button('Back to product list'):
            st.session_state.selected_product_id = ''
else:
    # Show product options as a table of buttons
    st.title('Product Options')
    st.write('Choose a product from the table below to view its details.')

    # Add custom CSS for risk circles
    st.markdown(
        """
        <style>
        .risk-circle-container {
            display: flex;
            align-items: center;
            gap: 16px;
            margin-bottom: 12px;
        }
        .risk-circle {
            width: 80px;
            height: 80px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            color: black;
            background: white;
            flex-shrink: 0;
            border: 4px solid;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

        
    # Create a table-like layout with buttons
    cols = st.columns(3)  # Adjust number of columns as needed
    for i, product in enumerate(PRODUCTS):
        with cols[i % 3]:
            risk_pct = product.get('risk_percentage', 50)
            risk_color = get_risk_color(risk_pct)
            risk_label = get_risk_label(risk_pct)
            
            # Display risk circle with colored border
            st.markdown(
                f"""
                <div class="risk-circle-container" style="color: white;">
                    <div class="risk-circle" style="border-color: {risk_color};">
                        {risk_pct}%
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            
            st.markdown(f"### {product['name']}")
            st.write(product['summary'])
            if st.button('View details', key=f"view_{product['id']}"):
                st.session_state.selected_product_id = product['id']
