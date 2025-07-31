import streamlit as st
import pandas as pd
import numpy as np
st.write("Graph")
x=pd.DataFrame(
  np.random.randn(234, 4),
  columns=["a", "b", "c", "d"]
  
)
st.line_chart(x)
