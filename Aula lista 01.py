import streamlit as st

xicarasfarinha  = float(st.text_input("Insira a quantidade de xicaras de farinha\n"))
gramasfarinha = float(st.text_input("Insira a quantidade de gramas de farinha\n"))
totalfarinha = xicarasfarinha*gramasfarinha
