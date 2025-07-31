import streamlit as st
import pandas as pd
import numpy as np
st.write("Graph")
x=pd.DataFrame(
  np.random.randn(2, 1),
  columns=["a"]
  
)
st.line_chart(x)
