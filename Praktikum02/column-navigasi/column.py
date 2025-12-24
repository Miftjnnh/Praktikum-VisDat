import streamlit as st

st.title("Columns")
st.write("Kelompok: 29")
st.markdown("""
    - Amirullah (0110222106)
    - Indah Agustin (0110222250)
    - Miftahul Jannah (0110222101)
""")

coll, col2 = st.columns(2)

coll.write("Ini adalah kolom pertama")
coll.image.("../../praktikum01/assets/panda.jpeg")

col2.write("Ini adalah kolom kedua")