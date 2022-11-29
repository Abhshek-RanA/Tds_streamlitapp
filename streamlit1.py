import streamlit as st

value1 = st.number_input('First Number')
value2 = st.number_input('Second Number')
st.write('Sum of Numbers is ', value1+value2)
