import streamlit as st

def convert_unit(value, unit_from, unit_to):
    conversion = {
        "meter_kilometer": 0.001,  # 1 meter = 0.001 kilometer
        "kilometer_meter": 1000,
        "gram_kilogram": 0.001,  # Fixed: "gram_kilometer" → "gram_kilogram"
        "kilogram_gram": 1000
    }

    key = f"{unit_from}_{unit_to}"

    if key in conversion:
        factor = conversion[key]  # Fixed variable name
        return value * factor
    else:
        return "Conversion not supported"
    
st.title("Unit Converter")

value = st.number_input("Enter Value:")

unit_from = st.selectbox("Convert from:", ["meter", "kilometer", "gram", "kilogram"])
unit_to = st.selectbox("Convert to:", ["meter", "kilometer", "gram", "kilogram"])

if st.button("Convert"):
    result = convert_unit(value, unit_from, unit_to)
    st.write(f"Converted Value: {result}")  # Fixed `st.write` statement
