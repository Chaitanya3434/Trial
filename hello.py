import streamlit as st
import pandas as pd
import numpy as np
st.title("Medical Reports")
a=st.text_input("Aadhar No.: ")
x=pd.read_csv(a)
st.write(x)


