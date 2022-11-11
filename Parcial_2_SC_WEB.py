import streamlit as st

st.header("Calcula tu capital final al paso del tiempo.")
st.subheader("Ingrese el capital inicial: ")
capital_inicial = st.number_input()
st.subheader("La tasa de interes es: ")
interes = st.number_input()
st.subheader("Ingrese los años a transcurrir: ")
años = st.slider()

capital_final = float(round(capital_inicial * (1 + interes / 100) ** años, 2))

st.header("El capital final es de: ", capital_final)
