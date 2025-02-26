import streamlit as st
st.header("cabeçalho")
st.toggle("botão salvar")
st.text_area("Enter text")
st.multiselect(
  "Quais são suas cores favoritas?",
  ["Verde","Vermelho","Azul"],
  ["Amarelo","Vermelho"])
st.text_input("Movie title", "Life of Gilson")
st.selectbox("Qual a sua cor favorita?", ("Azul", "Vermelho","Verde","Azul"))


st.button("Botão Salvar")
