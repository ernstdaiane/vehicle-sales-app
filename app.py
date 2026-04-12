import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv("vehicles_us.csv")

st.header("Análise de anúncios de venda de carros")

st.write("Este aplicativo permite visualizar dados de anúncios de carros e gerar gráficos interativos.")

hist_button = st.button("Criar histograma")

if hist_button:
    st.write("Criando um histograma para a coluna odometer")
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button("Criar gráfico de dispersão")

if scatter_button:
    st.write("Criando um gráfico de dispersão entre odometer e price")
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
