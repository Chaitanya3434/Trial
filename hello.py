import streamlit as st
import pandas as pd
st.write("Graph")
x=pd.read_csv("Bitcoin Historical Data.csv")
st.line_chart(x)
