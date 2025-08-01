import streamlit as st
import pandas as pd
import numpy as np
st.title("Medical Reports")
a=pd.csv_input()
x=pd.read_csv(a)
st.write(x)


