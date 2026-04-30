import streamlit as st
import json
from streamlit_elements import elements, mui, dashboard
from ui.banner import apply_banner, apply_header_strip
from ui.asset_container import render_asset_container
from config.objects import OBJECTS

# Load configuration
with open('config/config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

# Apply header strip and banner
apply_header_strip(config)
apply_banner(config)

st.title('Home')
st.write('Welcome to the Home Page! Explore the interactive containers below, rendered with streamlit_elements.')

with elements(key='home_containers'):
    with mui.Box(
        sx={
            'display': 'grid',
            'gridTemplateColumns': 'repeat(auto-fit, minmax(320px, 1fr))',
            'gap': '20px',
            'width': '100%',
            'padding': '12px',
        }
    ):
        with mui.Paper(
            elevation=3,
            sx={
                'padding': '22px',
                'minHeight': '240px',
                'display': 'flex',
                'flexDirection': 'column',
                'justifyContent': 'space-between',
            },
        ):
            mui.Typography('Overview', variant='h5')
            mui.Typography(
                'This card demonstrates a styled container built with streamlit_elements. Use it as a foundation for dashboard or panel sections.'
            )
            mui.Button('Primary action', variant='contained', color='primary', sx={'mt': 2})

        with mui.Paper(
            elevation=3,
            sx={
                'padding': '22px',
                'minHeight': '240px',
                'backgroundColor': '#f7f9fc',
                'display': 'flex',
                'flexDirection': 'column',
                'justifyContent': 'space-between',
            },
        ):
            mui.Typography('Controls', variant='h5')
            mui.Typography(
                'This panel can be extended with buttons, inputs, and interactive elements powered by streamlit_elements.'
            )
            mui.Button('Secondary action', variant='outlined', color='secondary', sx={'mt': 2})

        with mui.Paper(
            elevation=3,
            sx={
                'padding': '22px',
                'minHeight': '240px',
                'display': 'flex',
                'flexDirection': 'column',
                'justifyContent': 'space-between',
            },
        ):
            mui.Typography('Media & Layout', variant='h5')
            mui.Typography(
                'These containers render inside the Elements context, enabling rich layout and component behavior.'
            )
            mui.Button('Explore more', variant='contained', color='success', sx={'mt': 2})

st.markdown('---')

with elements("dashboard"):
    # You can create a draggable and resizable dashboard using
    # any element available in Streamlit Elements.

    # First, build a default layout for every element you want to include in your dashboard

    layout = [
        # Parameters: element_identifier, x_pos, y_pos, width, height, [item properties...]
        dashboard.Item("first_item", 0, 0, 2, 2),
        dashboard.Item("second_item", 2, 0, 2, 2, isDraggable=False, moved=False),
        dashboard.Item("third_item", 0, 2, 1, 1, isResizable=False),
    ]

    # If you want to retrieve updated layout values as the user move or resize dashboard items,
    # you can pass a callback to the onLayoutChange event parameter.

    def handle_layout_change(updated_layout):
        # You can save the layout in a file, or do anything you want with it.
        # You can pass it back to dashboard.Grid() if you want to restore a saved layout.
        print(updated_layout)

    with dashboard.Grid(layout, onLayoutChange=handle_layout_change):
        mui.Paper("First item", key="first_item")
        mui.Paper("Second item (cannot drag)", key="second_item")
        mui.Paper("Third item (cannot resize)", key="third_item")

st.markdown('---')

st.header("Interactive Objects Selector")

with st.container():
    selected_objects = st.multiselect(
        "Choose objects to add:",
        [obj["ObjectType"] for obj in OBJECTS],
        key="object_selector"
    )
    
    if selected_objects:
        st.subheader("Selected Objects:")
        for obj_type in selected_objects:
            obj = next(o for o in OBJECTS if o["ObjectType"] == obj_type)
            st.markdown(f"**{obj_type}:**")
            # Execute the example
            try:
                eval(obj["Example"], {"st": st})
            except Exception as e:
                st.error(f"Error displaying {obj_type}: {e}")
            st.markdown("---")
