# following this tutorial: https://towardsdatascience.com/create-a-photo-converter-app-using-streamlit-surprisingly-easy-and-fun-db291b5010c6

import streamlit as st
import numpy as np
import cv2
import pandas as pd
from  PIL import Image
from streamlit_drawable_canvas import st_canvas


#Create two columns with different width
col1, col2 = st.columns( [0.8, 0.2])
with col1:               # To display the header text using css style
    st.markdown(""" <style> .font {
    font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Upload your circuit here...</p>', unsafe_allow_html=True)
    

#Add a header and expander in side bar
st.sidebar.markdown('<p class="font">Tools</p>', unsafe_allow_html=True)
with st.sidebar.expander("About the App"):
     st.write("""
        This app is for analyzing your breadboard circuit prototypes. \n \n Upload a KiCAD netlist file as a reference and a top-down view of your circuit to see if you've assembled it correctly.
     """)

# Specify canvas parameters in application
drawing_mode = st.sidebar.selectbox(
    "Drawing tool:", ("rect", "point", "transform")
)

if drawing_mode == 'point':
    point_display_radius = st.sidebar.slider("Point display radius: ", 1, 25, 3)
uploaded_file = st.file_uploader("", type=['jpg','png','jpeg'])
bg_image = uploaded_file


realtime_update = st.sidebar.checkbox("Update in realtime", True)

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    image = image.resize((500,500))

    st.markdown('<p style="text-align: center;">Uploaded circuit</p>',unsafe_allow_html=True)
    # Create a canvas component
    canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
        stroke_width=2,
        stroke_color="#000",
        background_color="#000",
        width=image.width,
        background_image=Image.open(bg_image) if bg_image else None,
        update_streamlit=realtime_update,
        drawing_mode=drawing_mode,
        point_display_radius=point_display_radius if drawing_mode == 'point' else 0,
        key="canvas",
    )

    if canvas_result.json_data is not None:
        objects = pd.json_normalize(canvas_result.json_data["objects"]) # need to convert obj to str because PyArrow#
        objects = objects[['type', 'left', 'top', 'width', 'height']]
        for col in objects.columns:
            objects[col] = objects[col].astype("str")
        st.dataframe(objects)



