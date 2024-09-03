import streamlit as st
from tornado.options import options

st.title('Tech Academy')
st.write('Hello Student')
x=st.selectbox('Are you intrested for this course',options=['Yes','No'])
if x=='Yes':
    st.write('which technology you want to learn')
    y = st.radio('Are you Graduate', options=['Yes', 'No'])
    if y == 'Yes':
        st.write('You can enroll in our diploma course')
        z = st.selectbox('Select the technology', ('python', 'java', 'c++'))
        if z == 'python':
            st.write('contact', 'xyz', '56556')
        elif z == 'java':
            st.write('contact', 'xyz', '742475')
        elif z == 'c++':
            st.write('contact', 'nkf', '54667')
    else:
        st.write('You are not eligible this diploma course')
else:
    st.write('thank you')

