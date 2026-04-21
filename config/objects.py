import streamlit as st

# https://www.geeksforgeeks.org/python/a-beginners-guide-to-streamlit/

OBJECTS = [
    {
        "ObjectType": "Title",
        "Function": st.title,
        "Example": "st.title('Hello GeeksForGeeks !!!')"
    }
]
st.header("This is a header") 
st.subheader("This is a subheader")
st.text("Hello GeeksForGeeks!!!")
st.markdown("### This is a markdown")
st.success("Success")
st.info("Information")
st.warning("Warning")
st.error("Error")
st.exception(ZeroDivisionError("Trying to divide by Zero"))
st.write("Text with write")
from PIL import Image  # Import Image from Pillow
img = Image.open("streamlit.png") # Open the image file
st.image(img, width=200) # Display the image with a specified width
# Display a checkbox with the label 'Show/Hide'
if st.checkbox("Show/Hide"):
    # Show this text only when the checkbox is checked
    st.text("Showing the widget")

# Create a radio button to select gender
status = st.radio("Select Gender:", ['Male', 'Female'])

# Display the selected option using success message
if status == 'Male':
    st.success("Male")
else:
    st.success("Female")

