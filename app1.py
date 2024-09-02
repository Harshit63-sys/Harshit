import streamlit as st
from pygments.styles.dracula import background

st.title('My first app')
st.write('Hello all')
x=st.text_input('Which technology you want to learn')
if x=='Ai':
    st.write('Kindly enrolled in python first')
y=st.radio('are you graduate',option=['yes','No'])
if y=='yes':
    st.write('you can enroll in our diploma course')
else:
    st.write('You can do Internship')

z=st.selectbox('select the technology',('Python','Java','C++'))
if z=='python':
    st.write('connect abc 63077022')
elif z=='java':
    st.write('connect xyz 44246')
elif z=='c++':
    st.write('connect kds 646530')
st.button(background-color:'g')
