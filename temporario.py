import streamlit as st
import pandas as pd
st.header("cabeçalho")
st.toggle("botão salvar")
st.text_area("Enter text")
st.text_input("Movie title", "Life of Gilson")
st.selectbox("Qual a sua cor favorita?", ("Azul", "Vermelho","Verde","Azul"))

st.button("Botão Salvar")
st.color_picker("Pick A Color", "#00f900")
st.feedback("stars")
df = pd.Dataframe(
  [
    {"command": "st.slectbox", "rating":4, "is_winget":True},
    {"command": "st.balloons", "rating":5, "is_winget":False},
    {"command": "st.time_input", "rating":3,"is_winget":True},
  ]
)

edited_df=st.data_editor(df)
