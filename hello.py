import streamlit as st
import pandas as pd
import numpy as np
st.title("Medical Reports")
a=st.file_uploader("Upload File", type={"csv"})
if a is not None:
    x=pd.read_csv(a)
    st.line_graph(x)



