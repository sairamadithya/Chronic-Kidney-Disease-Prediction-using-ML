#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import numpy as np
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler
st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://images.unsplash.com/photo-1576671081837-49000212a370");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
html_temp = """ 
  <div style="background-color:orange ;padding:7px">
  <h2 style="color:black;text-align:center;"><b>AUTOMATED DIAGNOSIS OF CHRONIC KIDNEY DISEASE USING ML<b></h2>
  </div>
  """ 
st.markdown(html_temp,unsafe_allow_html=True)
model1= pickle.load(open("ckd model.pkl", 'rb'))
x1=st.number_input('enter the age')
x2=st.number_input('enter the blood pressure')
x3=st.number_input('enter the specific gravity')
x4=st.number_input('enter the aluminium')
x5=st.number_input('enter the su')
x6=st.number_input('enter the rbc')
x7=st.number_input('enter the platelet')
x8=st.number_input('enter the packed cell count')
x9=st.number_input('enter the barium')
x10=st.number_input('enter the bgr')
x11=st.number_input('enter the bu')
x12=st.number_input('enter the sc')
x13=st.number_input('enter the sodium')
x14=st.number_input('enter the potassium')
x15=st.number_input('enter the hemoglobin')
x16=st.number_input('enter the packed cell volume')
x17=st.number_input('enter the wbc')
x18=st.number_input('enter the rc')
x19=st.number_input('enter the htn')
x20=st.number_input('enter the diabetes risk')
x21=st.number_input('enter the cardiac risk')
x22=st.number_input('enter the appetite level')
x23=st.number_input('enter the pe')
x24=st.number_input('enter the anemia risk')
inp=pd.DataFrame([[x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23,x24]],columns=['age', 'bp', 'sg', 'al', 'su', 'rbc', 'pc', 'pcc', 'ba', 'bgr', 'bu',
       'sc', 'sod', 'pot', 'hemo', 'pcv', 'wc', 'rc', 'htn', 'dm', 'cad','appet', 'pe', 'ane'])
inp=StandardScaler().fit_transform(inp)
if st.button('Get diagnosis'):
    op=model1.predict(inp).astype(np.int16)
    if op==0:
        st.markdown(""" 
  <div style="background-color: green;padding:3px;border: 3px solid;">
  <h2 style="color:white;text-align:center;">Normal!!</h2>
  </div>
  """ ,unsafe_allow_html=True)
    else:
        st.markdown(""" 
  <div style="background-color: red;padding:3px;border: 3px solid;">
  <h2 style="color:white;text-align:center;">Chronic Kidney Disease!!</h2>
  </div>
  """ ,unsafe_allow_html=True)
st.write()
st.write()
st.write('https://www.linkedin.com/in/sairamadithya')
st.write('https://github.com/sairamadithya')
st.write('https://medium.com/@sairamadithya2002')
st.write('https://www.quora.com/profile/Sairam-Adithya')

