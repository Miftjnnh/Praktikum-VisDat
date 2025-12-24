import streamlit as st
import graphviz as graphviz

st.title("Graphviz Chart")
st.write("Kelompok: 29")
st.markdown("""
    - Amirullah (0110222106)
    - Indah Agustin (0110222250)
    - Miftahul Jannah (0110222101)
""")

st.graphviz_chart("""
    digraph {
        "Training Data" -> "ML Algorithm"
        "ML Algorithm" -> "Model" 
        "Model" -> "Results Forencasting"
        "New Data" -> "Model"    
     }
""")