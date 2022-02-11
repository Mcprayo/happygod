#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
from math import pi
st.header('simple web app')
st.write('* my app*')
st.write('**start scrolling to get your actual volume of the sphere**')
r= st.slider('val')
st.write(r,'volume of the sphere  is ',4/3*pi*r**3)


# In[ ]:


import streamlit as st
st.header('simple web app')
st.write('* my app*')
st.write('**start scrolling to get your actual farenheight**')
celcius= st.slider('val', 0 ,500,1000)
st.write(celcius,'farenheight is ',(celcius*9/5)+32 )


# In[ ]:


import streamlit as st
from math import pi
st.header('simple web app')
st.write('* my app*')
st.sidebar.number_input('**start scrolling to get your actual volume of the sphere**')
r= st.sidebar.number_input('val')
st.write(r,'volume of the sphere  is ',4/3*pi*r**3)


# In[ ]:


import streamlit as st
st.write('* convert furenheight to celcius* ')
farenheight = st.number_input('enter any farenheight value')
st.write(farenheight,'temperature in celcius is',5/9 *(farenheight-32))


st.write('* convert celcius to farenheight  *')
celcius = st.number_input('enter any celicius  value')
st.write(celcius,'farenheight is ',(celcius*9/5)+32 )

