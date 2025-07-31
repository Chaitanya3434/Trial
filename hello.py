import streamlit as st
import pandas as pd
import numpy as np
st.write("Graph")
x=pd.DataFrame("Bitcoin Historical Data.csv")
st.line_chart(x)
