#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
from math import pi
st.header('hello guys welcome to my simple web  app hope you will enjoy😉😉😉😉')
st.write('* my app✈*')
st.write('**start scrolling to get your actual volume of the sphere**')
r= st.slider('val')
st.write(r,'volume of the sphere  is ',4/3*pi*r**3)


# In[ ]:


import streamlit as st
st.header('simple web app')
st.write('* my app*')
st.write('**start scrolling to get your actual farenheit**')
celcius= st.slider('val', 0 ,500,1000)
st.write(celcius,'farenheit is ',(celcius*9/5)+32 )


# In[ ]:


import streamlit as st
from math import pi
st.header('simple web app')
st.write('* my app*')
r = st.sidebar.number_input('**enter any radius value in the side bar to get the volume of the sphere**')
st.write(r,'volume of the sphere  is ',4/3*pi*r**3)


# In[ ]:


import streamlit as st
st.write('* convert farenheit to celcius* ')
farenheit = st.number_input('enter any farenheit value')
st.write(farenheit,'temperature in celcius is',5/9 *(farenheit-32))


st.write('* convert celcius to farenheit  *')
celcius = st.number_input('enter any celicius  value')
st.write(celcius,'farenheit is ',(celcius*9/5)+32 )

