import streamlit as st

st.write("Calcula tu capital final al paso del tiempo.")

capital_inicial = st.number_input("Ingrese el capital inicial: ")
interes = st.number_input("La tasa de interes es: ")
años = st.slider("Ingrese los años a transcurrir: ")

capital_final = float(round(capital_inicial * (1 + interes / 100) ** años, 2))

st.write("El capital final es de: ", capital_final)
