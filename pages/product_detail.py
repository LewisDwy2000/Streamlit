import json
import streamlit as st
from ui.banner import apply_banner
from utils.products import get_product
from utils.theme import apply_color_theme

# Load configuration
with open('config/config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

# Apply color theme and banner
apply_color_theme(config)
apply_banner(config)

st.set_page_config(
    page_title=f"{config['title']} - Product Details",
    layout='wide'
)

selected_product_id = st.session_state.get('selected_product_id', '')
product = get_product(selected_product_id) if selected_product_id else None

st.title('Product Details')

if not product:
    st.warning('No product is selected yet. Please choose a product from the Options page.')
    if st.button('Back to product list'):
        st.session_state.selected_product_id = ''
        st.markdown(
            "<script>window.location.href = window.location.pathname + '?page=Options';</script>",
            unsafe_allow_html=True,
        )
else:
    st.subheader(product['name'])
    st.write(product['details'])

    st.markdown('**Key features:**')
    for feature in product['features']:
        st.write(f'- {feature}')

    st.markdown(f"**Price:** {product['price']}")
    st.markdown('---')

    cols = st.columns(2)
    if cols[0].button('Back to product list'):
        st.session_state.selected_product_id = ''
        st.markdown(
            "<script>window.location.href = window.location.pathname + '?page=Options';</script>",
            unsafe_allow_html=True,
        )
    if cols[1].button('Exit details'):
        st.session_state.selected_product_id = ''
        st.markdown(
            "<script>window.location.href = window.location.pathname + '?page=Options';</script>",
            unsafe_allow_html=True,
        )
