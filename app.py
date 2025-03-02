import streamlit as st
import matplotlib.pyplot as plt

# Set Page Configurations
st.set_page_config(page_title="Advanced Unit Converter", page_icon="🔄", layout="wide")

# Custom CSS for styling
st.markdown(
    """
    <style>
    .main {background: linear-gradient(135deg, #f0f8ff, #add8e6); padding: 20px; border-radius: 15px;}
    .stTextInput, .stNumberInput, .stSelectbox, .stButton>button {
        border-radius: 10px; 
        width: 100%; 
        max-width: 500px;
        font-size: 16px;
    }
    .stButton>button {
        background: linear-gradient(45deg, #ff4500, #ff6347); 
        color: white; 
        font-size: 18px; 
        padding: 10px;
        border: none;
        border-radius: 10px;
        box-shadow: 3px 3px 5px rgba(0,0,0,0.3);
    }
    .stButton>button:hover {
        background: linear-gradient(45deg, #ff6347, #ff7f50);
    }
    .stSelectbox, .stNumberInput {
        padding: 8px;
        background: linear-gradient(135deg, #ffdab9, #ffe4b5);
        border: 2px solid #ff4500;
        border-radius: 10px;
    }
    .stSelectbox label, .stSidebar select, .stNumberInput label {
        color: black;
        font-weight: bold;
    }
    .container {
        display: flex; 
        flex-direction: column; 
        align-items: center; 
        justify-content: center; 
        text-align: center;
        padding: 20px;
    }
    h1 {
        color: #ff4500;
        text-shadow: 2px 2px 5px rgba(0,0,0,0.2);
        font-size: 2.5em;
        font-weight: bold;
    }
    
    @media (max-width: 768px) {
        .container {width: 100%; padding: 10px;}
        h1 {font-size: 2em;}
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.title("🔄 Advanced Unit Converter")
st.write("Convert various units with ease!")

# Conversion Logic
def convert_units(value, from_unit, to_unit, conversion_dict):
    if from_unit in conversion_dict and to_unit in conversion_dict:
        return value * (conversion_dict[to_unit] / conversion_dict[from_unit])
    return None

# Unit Categories
unit_categories = {
    "Length": {"Meter": 1, "Kilometer": 0.001, "Centimeter": 100, "Millimeter": 1000, "Mile": 0.000621371, "Yard": 1.09361, "Foot": 3.28084, "Inch": 39.3701},
    "Weight": {"Kilogram": 1, "Gram": 1000, "Milligram": 1000000, "Pound": 2.20462, "Ounce": 35.274},
    "Temperature": {"Celsius": 1, "Fahrenheit": 33.8, "Kelvin": 274.15},
    "Data Transfer Rate": {"bit per second": 1, "Kilobit per second": 0.001, "Megabit per second": 0.000001, "Gigabit per second": 0.000000001}
}

# Sidebar for Unit Selection
st.sidebar.markdown("### ⚙️ Unit Conversion Settings")
category = st.sidebar.selectbox("Select Category", list(unit_categories.keys()))
from_unit = st.sidebar.selectbox("Convert from", list(unit_categories[category].keys()))
to_unit = st.sidebar.selectbox("Convert to", list(unit_categories[category].keys()))

# User Input for Value
value = st.number_input("Enter Value", min_value=0.0, format="%.2f")

# Convert and Display Result
if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit, unit_categories[category])
    
    if result is not None:
        st.success(f"✅ {value} {from_unit} is equal to {result:.2f} {to_unit}")
        
        # Visualization
        fig, ax = plt.subplots()
        ax.bar([from_unit, to_unit], [value, result], color=['blue', 'orange'])
        ax.set_ylabel("Converted Values")
        ax.set_title("📊 Conversion Visualization")
        st.pyplot(fig)
    else:
        st.error("❌ Conversion not possible!")