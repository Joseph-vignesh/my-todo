import streamlit as st
import function

todos = function.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    function.write_todos(todos)

st.title("My-Todo-App")
st.subheader("Chase your Tasks")
st.write("This app boosts your productivity")

for i, todo in enumerate(todos):
    st.checkbox(todo, key=f"todo_{i}")

st.text_input(label="A*****Z", placeholder="Add your todo here", on_change=add_todo, key='new_todo')
