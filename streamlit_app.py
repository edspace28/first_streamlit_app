import streamlit

streamlit.title("My Parents' New Healthy Diner")

streamlit.header('Breakfast Menu')
streamlit.text('🍳Full English')
streamlit.text('🧇Fruit Topped Waffles')
streamlit.text('🥞Pancakes with Maple Syrup')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

streamlit.dataframe(my_fruit_list)
