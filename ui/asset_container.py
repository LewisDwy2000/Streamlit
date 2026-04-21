import streamlit as st
from pathlib import Path

ASSET_TYPES = ["Text", "Image", "Button"]


def _resolve_image_source(value: str):
    if value.startswith("http://") or value.startswith("https://"):
        return value
    path = Path(value)
    if path.exists():
        return str(path)
    return None


def render_asset_container(config):
    """Render a page-level asset container that can be modified at runtime."""
    if "managed_assets" not in st.session_state:
        st.session_state.managed_assets = []

    if "asset_container_height" not in st.session_state:
        st.session_state.asset_container_height = 400
    if "asset_container_width" not in st.session_state:
        st.session_state.asset_container_width = 80

    st.sidebar.header("Asset container")
    asset_type = st.sidebar.selectbox("Asset type", ASSET_TYPES)
    asset_value = st.sidebar.text_input(
        "Asset value",
        value="Example text or image URL/path",
        help="Enter text, image URL/path, or button label depending on the selected asset type.",
    )
    st.sidebar.markdown("---")
    width = st.sidebar.slider(
        "Container width (%)",
        min_value=40,
        max_value=100,
        value=st.session_state.asset_container_width,
    )
    height = st.sidebar.slider(
        "Container min height (px)",
        min_value=200,
        max_value=1200,
        value=st.session_state.asset_container_height,
    )

    if st.sidebar.button("Add asset"):
        st.session_state.managed_assets.append({
            "type": asset_type,
            "value": asset_value.strip(),
        })

    if st.sidebar.button("Clear assets"):
        st.session_state.managed_assets = []

    st.session_state.asset_container_height = height
    st.session_state.asset_container_width = width

    st.write("### Managed Asset Container")
    st.write("Drag the bottom-right corner of the container to resize it using the mouse.")
    st.markdown(
        f"""
        <style>
        .asset-container {{
            min-height: {height}px;
            width: {width}%;
            max-width: 100%;
            resize: both;
            overflow: auto;
            background: rgba(255, 255, 255, 0.85);
            border: 1px solid #ddd;
            border-radius: 12px;
            padding: 18px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.06);
            margin-bottom: 24px;
        }}
        .asset-container::-webkit-resizer {{
            background: transparent;
        }}
        .asset-item {{
            margin-bottom: 16px;
            padding: 12px;
            border-radius: 10px;
            background: #fafafa;
            border: 1px solid #ececec;
        }}
        .asset-item-title {{
            font-weight: 700;
            margin-bottom: 8px;
        }}
        .asset-text {{
            white-space: pre-wrap;
        }}
        </style>
        <div class="asset-container">
        """,
        unsafe_allow_html=True,
    )

    if not st.session_state.managed_assets:
        st.info("Use the sidebar controls to add assets to this container.")
    else:
        for index, asset in enumerate(st.session_state.managed_assets):
            st.markdown(
                f"""
                <div class='asset-item'>
                    <div class='asset-item-title'>Asset {index + 1}: {asset['type']}</div>
                """,
                unsafe_allow_html=True,
            )
            if asset["type"] == "Text":
                st.markdown(f"<div class='asset-text'>{asset['value']}</div>", unsafe_allow_html=True)
            elif asset["type"] == "Image":
                image_source = _resolve_image_source(asset["value"])
                if image_source:
                    st.image(image_source, use_column_width=True)
                else:
                    st.warning("Image asset could not be resolved. Enter a valid URL or local path.")
            elif asset["type"] == "Button":
                st.button(asset["value"], key=f"asset_button_{index}")
            st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
