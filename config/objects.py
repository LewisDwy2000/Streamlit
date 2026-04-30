import streamlit as st

# Object that stores Streamlit interactive elements (widgets)

OBJECTS = [
    {
        "ObjectType": "Button",
        "Function": st.button,
        "Example": "st.button('Click me')"
    },
    {
        "ObjectType": "Checkbox",
        "Function": st.checkbox,
        "Example": "st.checkbox('Check me')"
    },
    {
        "ObjectType": "Radio",
        "Function": st.radio,
        "Example": "st.radio('Select one', ['Option 1', 'Option 2'])"
    },
    {
        "ObjectType": "Selectbox",
        "Function": st.selectbox,
        "Example": "st.selectbox('Choose', ['A', 'B', 'C'])"
    },
    {
        "ObjectType": "Multiselect",
        "Function": st.multiselect,
        "Example": "st.multiselect('Select multiple', ['A', 'B', 'C'])"
    },
    {
        "ObjectType": "Slider",
        "Function": st.slider,
        "Example": "st.slider('Select value', 0, 100)"
    },
    {
        "ObjectType": "Text Input",
        "Function": st.text_input,
        "Example": "st.text_input('Enter text')"
    },
    {
        "ObjectType": "Number Input",
        "Function": st.number_input,
        "Example": "st.number_input('Enter number', min_value=0, max_value=100)"
    },
    {
        "ObjectType": "Text Area",
        "Function": st.text_area,
        "Example": "st.text_area('Enter long text')"
    },
    {
        "ObjectType": "Date Input",
        "Function": st.date_input,
        "Example": "st.date_input('Select date')"
    },
    {
        "ObjectType": "Time Input",
        "Function": st.time_input,
        "Example": "st.time_input('Select time')"
    },
    {
        "ObjectType": "File Uploader",
        "Function": st.file_uploader,
        "Example": "st.file_uploader('Upload file')"
    },
    {
        "ObjectType": "Color Picker",
        "Function": st.color_picker,
        "Example": "st.color_picker('Pick a color')"
    }
]

