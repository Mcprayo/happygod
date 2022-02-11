#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#To use a python program 
import streamlit as st
st.hearder('**welcome to my simple web app**')
st.write('* convert celcius to farenheit  *')
celcius = st.number_input('enter any celicius  value')
st.write(celcius,'temperature in farenheit is: ',(celcius*9/5)+32,'°F' )

