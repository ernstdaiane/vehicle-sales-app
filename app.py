import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv("vehicles_us.csv")

st.title("Vehicle Sales Analytics")

st.write(
    "Explore vehicle sales data through interactive visualizations "
    "and discover patterns related to mileage and price."
)

st.subheader("Mileage Distribution")

hist_button = st.button("Create mileage histogram")

if hist_button:
    fig = px.histogram(
        car_data,
        x="odometer",
        title="Distribution of Vehicle Mileage"
    )

    fig.update_layout(
        xaxis_title="Mileage",
        yaxis_title="Number of Vehicles"
    )

    st.plotly_chart(fig, use_container_width=True)

st.subheader("Mileage vs Price")

scatter_button = st.button("Explore mileage and price")

if scatter_button:
    fig = px.scatter(
        car_data,
        x="odometer",
        y="price",
        title="Vehicle Price vs Mileage"
    )

    fig.update_layout(
        xaxis_title="Mileage",
        yaxis_title="Price"
    )

    st.plotly_chart(fig, use_container_width=True)
