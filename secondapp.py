import streamlit as st
# Page Setup
st.set_page_config(page_title="🌎 My Streamlit App - Fiyda",layout="wide")

st.title("Layout And Sidebar")
col1 , col2 = st.columns(2)


with col1:
    st.header("Left Side")
    name = st.text_input("Enter Your Name?")
    if name:
        st.success(f'Welcome User (name) !')

with col2:
    st.header("Odd Even Checker")
    num = st.slider("Select A Number")
    if num%2==0:
        st.write("even Number")
    else:
        st.write("Odd Number")


with st.sidebar:
    st.header("Control Panel")
    user_color = st.color_picker("Pick Your Favourite Color","#000000")
    st.write("You have selected : ",user_color )

# in sidebar provide 2 option to user
# select dark or light theme
# if user selects Dark change the theme of streamlit app
import streamlit as st

# --- Sidebar Theme Selector ---
st.sidebar.title("Theme Settings")
theme = st.sidebar.radio("Choose Theme", ["Light", "Dark"])

# --- Theme Styles ---
light_theme = """
<style>
body {
    background-color: #FFFFFF;
    color: #000000;
}
</style>
"""

dark_theme = """
<style>
body {
    background-color: #0E1117;
    color: #FAFAFA;
}
</style>
"""

# --- Apply Selected Theme ---
if theme == "Dark":
    st.markdown(dark_theme, unsafe_allow_html=True)
else:
    st.markdown(light_theme, unsafe_allow_html=True)

# --- Main App UI ---
st.title("🌗 Theme Switcher App")
st.write(f"You are currently using the **{theme} Mode**!")

st.write("This is an example of dynamic theming using Streamlit + CSS.")