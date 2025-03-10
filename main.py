import streamlit as st
import streamlit.components.v1 as components

def length_converter(value, target):
    units = {'m': 1, 'cm': 100, 'mm': 1000, 'km': 0.001}
    if target in units:
        return f"{value} m = {value * units[target]} {target} ✨"
    return "⚠️ Invalid unit"

def weight_converter(value, target):
    units = {'kg': 1, 'g': 1000, 'mg': 1000000, 'lb': 2.20462}
    if target in units:
        return f"{value} kg = {value * units[target]} {target} 🍏"
    return "⚠️ Invalid unit"

def temperature_converter(value, target):
    if target == 'F':
        return f"{value}°C = {value * 9/5 + 32}°F 🔥"
    elif target == 'K':
        return f"{value}°C = {value + 273.15}K ❄️"
    return "⚠️ Invalid unit"

st.markdown(
    """
    <style>
    body, .stTextInput, .stSelectbox, .stNumberInput, .stButton {
        font-size: 14px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🔄 Unit Converter")
option = st.selectbox("Choose a conversion type:", ["Length 📏", "Weight ⚖️", "Temperature 🌡️"])

if option == "Length 📏":
    value = st.number_input("Enter length in meters:", min_value=0.0, step=0.1)
    target = st.selectbox("Convert to:", ["cm", "mm", "km"])
    if st.button("Convert"):
        st.success(length_converter(value, target))

elif option == "Weight ⚖️":
    value = st.number_input("Enter weight in kg:", min_value=0.0, step=0.1)
    target = st.selectbox("Convert to:", ["g", "mg", "lb"])
    if st.button("Convert"):
        st.success(weight_converter(value, target))

elif option == "Temperature 🌡️":
    value = st.number_input("Enter temperature in Celsius:", step=0.1)
    target = st.selectbox("Convert to:", ["F", "K"])
    if st.button("Convert"):
        st.success(temperature_converter(value, target))
