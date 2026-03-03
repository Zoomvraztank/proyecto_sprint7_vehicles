import pandas as pd
import plotly.express as px
import streamlit as st

# Título de la aplicación
st.header("Análisis de Anuncios de Venta de Coches")

# Leer dataset
car_data = pd.read_csv("vehicles_us.csv")

# Limpieza mínima necesaria
clean_data = car_data.dropna(subset=["odometer", "model_year"]).copy()
clean_data["model_year"] = clean_data["model_year"].astype(int)
clean_data["is_4wd"] = clean_data["is_4wd"].fillna(0).astype(bool)

# Checkbox para histograma
build_histogram = st.checkbox("Mostrar histograma de kilometraje")

if build_histogram:
    st.write("Distribución del kilometraje de los vehículos")

    fig_hist = px.histogram(
        clean_data,
        x="odometer",
        title="Distribución del kilometraje"
    )

    st.plotly_chart(fig_hist, use_container_width=True)

# Checkbox para scatter
build_scatter = st.checkbox("Mostrar relación entre kilometraje y precio")

if build_scatter:
    st.write("Relación entre kilometraje y precio")

    fig_scatter = px.scatter(
        clean_data,
        x="odometer",
        y="price",
        opacity=0.5,
        title="Kilometraje vs Precio"
    )

    st.plotly_chart(fig_scatter, use_container_width=True)
