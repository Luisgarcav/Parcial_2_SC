import streamlit as st

st.header("Calcula tu capital final al paso del tiempo.")

capital_inicial = st.number_input("Ingrese el capital inicial: ")
interes = st.number_input("La tasa de interes es: ")
años = st.slider("Ingrese los años a transcurrir: ")

capital_final = float(round(capital_inicial * (1 + interes / 100) ** años, 2))

st.subheader("El capital final es de: ")
st.write(capital_final)

