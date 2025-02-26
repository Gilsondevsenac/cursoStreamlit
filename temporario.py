import streamlit as st
st.header("cabeçalho")
st.toggle("botão salvar")
st.text_area("Enter text")
st.text_input("Movie title", "Life of Gilson")
st.selectbox("Qual a sua cor favorita?", ("Azul", "Vermelho","Verde","Azul"))
st.multiselect(
  "Quais são sua cores favoritas?",
  ["Verde", "Vermelho","Azul"],
  ["Amarelo", "Vermelho"])
st.button("Botão Salvar")
