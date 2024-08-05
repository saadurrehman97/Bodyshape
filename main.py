import streamlit as st

def classify_body_shape(gender, shoulder, bust, waist, hip):
    if gender == 'Female':
        if abs(bust - hip) < 2 and abs(bust - waist) >= 9 and abs(hip - waist) >= 9:
            return "Hourglass"
        elif bust >= (hip * 1.05):
            return "Inverted Triangle"
        elif hip >= (bust * 1.05):
            return "Pear"
        elif abs(bust - hip) < 2 and abs(bust - waist) < 9 and abs(hip - waist) < 9:
            return "Rectangle"
        elif bust > hip and abs(bust - waist) < 9:
            return "Apple"
        elif waist >= (hip * 0.75):
            return "Spoon"
        elif hip > bust and hip > waist:
            return "Triangle"
        elif 0.85 <= shoulder/hip <= 1.05 and 1.001 <= bust/hip < 1.15 and 0.95 <= bust/waist < 1.15 and hip/waist < 1:
            return "Apple Body Shape"
        elif 0.9 <= shoulder/hip <= 1.1 and 0.9 <= bust/hip <= 1.1 and bust/waist >= 1.02 and hip/waist >= 1.02:
            return "Hourglass"
        elif shoulder/hip > 1 and bust/hip > 1 and bust/waist > 1 and hip/waist < 1:
            return "Inverted Triangle"
        elif shoulder/hip < 0.9 and hip/waist > 1:
            return "Pear"
        else:
            return "Undefined"
    else:  # Male
        if shoulder/bust < 1 and bust/waist < 1 and waist/hip < 1:
            return "Triangle"
        elif shoulder/bust > 1 and bust/waist > 1 and waist/hip < 1:
            return "Inverted Triangle"
        elif shoulder/bust > 1 and bust/waist > 1 and waist/hip >= 1:
            return "Trapezoid"
        elif shoulder/bust < 1 and bust/waist < 1 and waist/hip > 1:
            return "Oval"
        else:
            return "Undefined"

st.title("Body Shape Classifier")

# Option to select measurement units
units = st.radio("Select Measurement Units", ("Centimeters", "Inches"))

gender = st.radio("Select Gender", ("Female", "Male"))

# Adjust label based on selected units
unit_label = " (cm)" if units == "Centimeters" else " (in)"

shoulder = st.number_input(f"Shoulder Measurement{unit_label}", min_value=0.0)
bust = st.number_input(f"Bust Measurement{unit_label}", min_value=0.0)
waist = st.number_input(f"Waist Measurement{unit_label}", min_value=0.0)
hip = st.number_input(f"Hip Measurement{unit_label}", min_value=0.0)

if st.button("Classify"):
    if shoulder and bust and waist and hip:
        body_shape = classify_body_shape(gender, shoulder, bust, waist, hip)
        st.write(f"Your body shape is: {body_shape}")
    else:
        st.write("Please enter all measurements.")
