import streamlit as st

# Custom CSS to make the app look attractive
st.markdown("""
    <style>
    body {
        background-color: #f0f2f6;
    }
    .stApp {
        background-color: #ffffff;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 5px 5px 15px rgba(0,0,0,0.1);
    }
    .title {
        color: #ff5733;
        font-size: 32px;
        font-weight: bold;
        text-align: center;
    }
    .stButton>button {
        background-color: #ff5733 !important;
        color: white !important;
        font-size: 18px;
        border-radius: 10px;
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Function to convert units
def convert_unit(value, unit_from, unit_to):
    conversion = {
        "meter_kilometer": 0.001,  # 1 meter = 0.001 kilometer
        "kilometer_meter": 1000,
        "gram_kilogram": 0.001,  # Fixed: "gram_kilometer" → "gram_kilogram"
        "kilogram_gram": 1000
    }

    key = f"{unit_from}_{unit_to}"

    if key in conversion:
        factor = conversion[key]
        return value * factor
    else:
        return "⚠️ Conversion not supported!"
    
# Title with emoji
st.markdown("<p class='title'>🔄 Unit Converter 🔄</p>", unsafe_allow_html=True)

# Input value
value = st.number_input("🔢 Enter Value:", min_value=0.0, step=0.1)

# Select boxes for units
unit_from = st.selectbox("📏 Convert from:", ["meter", "kilometer", "gram", "kilogram"])
unit_to = st.selectbox("🎯 Convert to:", ["meter", "kilometer", "gram", "kilogram"])

# Conversion button
if st.button("🚀 Convert"):
    result = convert_unit(value, unit_from, unit_to)
    st.success(f"✅ **Converted Value:** {result}")  # Styled output
