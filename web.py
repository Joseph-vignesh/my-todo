import streamlit as st
import function

todos = function.get_todos()

st.title("My-Todo-App")
st.subheader("Chase your Tasks")
st.write("This app boosts your productivity")

st.checkbox("Lets go !!!!!")
for todo in todos:
    st.checkbox(todo)
st.checkbox("yayyy")

st.text_input(label= "A*****Z", placeholder="Add your todo here")