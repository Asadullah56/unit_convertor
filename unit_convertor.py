import streamlit as st

def convert_unit(value, unit_from ,unit_to):

    converstion = {
        "meter_kilometer": 0.001, # 1 meter = 0.001 = 0.001 kilometer
        "kilometer_meter":1000,
        "gram_kilometer":0.001,
        "kilogram_gram":1000
    }

    key = f"{unit_from}_{unit_to}"

    if key in converstion:
        converstion = converstion[key]
        return value * converstion
    else:
        return "Conversion not supported"
    
st.title("Unit Converter")

value = st.number_input("Enter Value:")

unit_from = st.selectbox("Convert from: ",["meter","kilometer","gram","kilogram"])

unit_to = st.selectbox("Convert to:",["meter","kilometer","gram","kilogram"])

if st.button("Convert"):
    result = convert_unit(value, unit_from, unit_to)
    st.write(f"Convert value: {value}")
