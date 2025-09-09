import numpy as np
import altair as alt
import pandas as pd
import streamlit as st
from datetime import time, datetime

st.header('Checkbox')

if st.button('Say hello'):
    st.write('Hello, *World!* :sunglasses:')
else:
    st.write('Goodbye')

# CHECKBOX
st.write('What would you like to order?')

icecream = st.checkbox('Ice Cream')
tomato = st.checkbox('Tomato')
cola = st.checkbox('Cola')

if icecream:
    st.write("Here's your :icecream:")
if tomato:
    st.write("Here's your :tomato:")
if cola:
    st.write("Here's your :cup_with_straw:")

# MULTISELECT
options = st.multiselect(
    'What are your favorite colors?',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'],
)
st.write('You selected:', options)

# SELECT BOX
option = st.selectbox(
    'What is your favorite color?',
    ('Blue', 'Red', 'Green')
)
st.write('Your favorite color is ', option)

# LINE CHART
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(chart_data)

# SLIDERS
st.subheader('Slider')

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, "years old")

st.subheader('Range slider')

values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)
st.write('Values:', values)

st.subheader('Range time slider')

appointment = st.slider(
    "Schedule your appointment:",
    value=(time(11, 30), time(12, 45))
)
st.write("You're scheduled for:", appointment)

st.subheader('Datetime slider')

start_time = st.slider(
    "When do you start?",
    value=datetime(2025, 1, 1, 9, 30),
    format="MM/DD/YY = hh:mm"
)
st.write("Start time:", start_time)

# PANDA DATAFRAME
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
st.write(df)

st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

df2 = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c']
)
c = alt.Chart(df2).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c']
)

st.write(c)





