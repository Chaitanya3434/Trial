import streamlit as st
import pandas as pd
import numpy as np
st.write("Graph")
x=pd.DataFrame(
  np.random(20, 3)
)
st.line_chart(x)
