import streamlit as st
import matplotlib
from race_inputs import RaceInputs
from PIL import Image

# Set session states
if 'clicked' not in st.session_state:
    st.session_state.clicked = False

# Definitions
circuits = ["Select Circuit", "Austria", "Baku", "Bahrain", "Belgium", "Monaco"]
circuit_diagrams = ["", "images\Austria_Circuit.png", "images\Baku_Circuit.png", "images\Bahrain_Circuit.png", "images\Belgium_Circuit.png", "images\Monaco_Circuit.png"]

# Functions
def model_start_click():
    st.session_state.clicked = True
    model_load_bar = st.progress(0, text=None)
    for i in range(100):
        model_load_bar.progress(i, text="Loading...")

# Add a sidebar
with st.sidebar:
  st.title("Inputs")
  option = st.selectbox("Select Circuit", circuits)
  index = circuits.index(option)
  image_path = circuit_diagrams[index]

  # Add a slider
  slider_val = st.slider("Select a value", 0, 100, 50)

# Main content area
st.title("Pit Stop Strategy Sim")

# Load the image
st.write(option)
if image_path:
    image = Image.open(image_path)
    # Display the image
    st.image(image)

if not option == "Select Circuit":
    st.button("Model Start!", on_click=model_start_click)

if st.session_state['clicked']:
    print("meow!!")



