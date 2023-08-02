import streamlit
import functions

todos = functions.get_todos()


def add_todo():
    todo_add = streamlit.session_state["new_todo"] + "\n"
    todos.append(todo_add)
    functions.write_todos(todos)


def complete_todo(todo_index, todo_complete):
    todos.pop(todo_index)
    functions.write_todos(todos)
    del streamlit.session_state[todo_complete]
    streamlit.experimental_rerun()


streamlit.title("My To-Do App")
streamlit.subheader("This is my personal todo app")
streamlit.write("This app is to increase my productivity")

for index, todo in enumerate(todos):
    checkbox = streamlit.checkbox(todo, key=todo)
    if checkbox:
        complete_todo(index, todo)

streamlit.text_input(label="", placeholder="Add new todo...", on_change=add_todo, key='new_todo')
