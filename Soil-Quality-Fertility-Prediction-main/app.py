import streamlit as st
import joblib
import numpy as np

# Load the trained Random Forest model using joblib
model = joblib.load('soil_fertility.pkl')

# Streamlit interface
st.title("Soil Fertility Prediction System By Asah James Boluwatife 20/47XCS/00236")

# Input features for soil fertility prediction
st.header("Enter Soil Elemental Analysis")

# Input fields corresponding to the 12 features
import streamlit as st

# Soil parameters with appropriate min and max values
N = st.number_input("Nitrogen (N) ratio (%)", min_value=0.02, max_value=0.5, value=0.1, step=0.01)
P = st.number_input("Phosphorous (P) ratio (ppm)", min_value=5.0, max_value=60.0, value=20.0, step=1.0)
K = st.number_input("Potassium (K) ratio (ppm)", min_value=50.0, max_value=400.0, value=200.0, step=10.0)
ph = st.number_input("Soil Acidity (pH)", min_value=4.5, max_value=8.5, value=6.5, step=0.1)
ec = st.number_input("Electrical Conductivity (ec) (dS/m)", min_value=0.1, max_value=5.0, value=1.0, step=0.1)
oc = st.number_input("Organic Carbon (oc) (%)", min_value=0.2, max_value=3.5, value=1.5, step=0.1)
S = st.number_input("Sulfur (S) (ppm)", min_value=5.0, max_value=50.0, value=20.0, step=1.0)
zn = st.number_input("Zinc (Zn) (ppm)", min_value=0.5, max_value=10.0, value=5.0, step=0.1)
fe = st.number_input("Iron (Fe) (ppm)", min_value=2.0, max_value=100.0, value=50.0, step=1.0)
cu = st.number_input("Copper (Cu) (ppm)", min_value=0.2, max_value=5.0, value=2.0, step=0.1)
Mn = st.number_input("Manganese (Mn) (ppm)", min_value=1.0, max_value=50.0, value=25.0, step=1.0)
B = st.number_input("Boron (B) (ppm)", min_value=0.1, max_value=2.0, value=1.0, step=0.1)


# Predict button
if st.button("Predict Soil Fertility"):
    # Create an array with the input features
    input_features = np.array([[N, P, K, ph, ec, oc, S, zn, fe, cu, Mn, B]])

    # Predict soil fertility class
    prediction = model.predict(input_features)[0]

    # Display the result with corresponding label
    if prediction == 0:
        st.success("The predicted soil fertility class is: Less Fertile")
    elif prediction == 1:
        st.success("The predicted soil fertility class is: Fertile")
    else:
        st.success("The predicted soil fertility class is: Highly Fertile")

# Footer
st.write("---")
st.write("Developed using a Random Forest model for soil fertility prediction.")
