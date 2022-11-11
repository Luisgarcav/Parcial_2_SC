"""
Luis Alberto Garza Cavazos #736573
                        10/11/2022
"""

"""
Has un programa que pida al usuario una cantidad de dolares, una tasa de interés y un numero de años. 
Muestra por pantalla en cuanto se habrá convertido el capital inicial transcurridos esos años si cada 
año se aplica la tasa de interés introducida.

Recordar que un capital C dolares a un interés del x por cien durante n años se convierte en 
C * (1 + x/100)elevado a n (años). Probar el programa sabiendo que una cantidad de 10000 dolares 
al 4.5% de interés anual se convierte en 24117.14 dolares al cabo de 20 años.
"""
import streamlit as st

st.write("Calcula tu capital final al paso del tiempo.")

capital_inicial = float(input("Ingrese el capital inicial: "))
interes = float(input("Ingrese la tasa de interes: "))
años = int(input("Ingrese el número de años: "))

capital_final = float(round(capital_inicial * (1 + interes / 100) ** años, 2))

print("Capital final: ", capital_final)
