import streamlit as st

# Define the STAR_DELTA function
def STAR_DELTA(R1, R2, R3):
    denominator = R1 * R2 + R2 * R3 + R3 * R1
    R12 = denominator / R3/1000
    R23 = denominator / R1/1000
    R31 = denominator / R2/1000
    return R12, R23, R31

# Streamlit Application
st.title("2205A21053")

st.header("Calculate Delta Connection Resistances (R12, R23, R31)")

# Input fields for STAR resistances
R1 = st.number_input("Enter Resistance R1 (Kilo Ohms):", min_value=0.0, format="%.2f")
R2 = st.number_input("Enter Resistance R2 (Kilo Ohms):", min_value=0.0, format="%.2f")
R3 = st.number_input("Enter Resistance R3 (Kilo Ohms):", min_value=0.0, format="%.2f")

# Button to trigger calculation
if st.button("Calculate"):
    # Validate inputs
    if R1 > 0 and R2 > 0 and R3 > 0:
        R12, R23, R31 = STAR_DELTA(R1, R2, R3)
        st.success(f"Calculated Resistances:\nR12 = {R12:.2f} Ω\nR23 = {R23:.2f} Ω\nR31 = {R31:.2f} Ω")
    else:
        st.error("Please enter positive values for R1, R2, and R3.")