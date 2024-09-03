import streamlit as st
st.title('My first app')
st.write('Hello all')
x=st.text_input('which technology you want to learn')
if x=='Ai':
    st.write('kindly enroll in python first')
else:
    st.write('sorry')
y=st.radio('Are you Graduate',options=['Yes','No'])
if y=='Yes':
    st.write('You can enroll in our diploma course')
else:
    st.write('You are not eligible this diploma course')
#a=st.button('show')
#if a==1
z=st.selectbox('Select the technology',('python','java','c++'))
if z=='python':
    st.write('contact','xyz','56556')
elif z=='java':
    st.write('contact','xyz','742475')
elif z=='c++':
    st.write('contact','nkf','54667')
