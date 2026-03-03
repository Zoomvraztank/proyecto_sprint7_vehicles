import pandas as pd
import streamlit as st

st.title("Sprint 7 - Vehicles Project")
st.write("Aplicación en construcción")

car_data = pd.read_csv("vehicles_us.csv")

st.subheader("Vista previa del dataset")
st.dataframe(car_data.head(20))
