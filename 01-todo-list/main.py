import streamlit as st

# Initialize session state for tasks
if "tasks" not in st.session_state:
    st.session_state.tasks = []

st.set_page_config(page_title="unit convertor", page_icon="📝")

st.title("📝 To-Do List App")

# Input field to add tasks
new_task = st.text_input("Add a new task:")

# Button to add task
if st.button("➕ Add Task"):
    if new_task:  # Ensure task is not empty
        st.session_state.tasks.append(new_task)
        st.success(f"Task '{new_task}' added!")
    else:
        st.warning("Please enter a task before adding.")

st.divider()  # Adds a separator

# Display tasks with checkboxes
st.subheader("Your Tasks:")
if st.session_state.tasks:
    for i, task in enumerate(st.session_state.tasks): # enumerate is use to insert index on task that we display it make easy to doing futher logic using index
        if st.checkbox(task, key=task):  # Checkbox to mark as done
            st.session_state.tasks.pop(i)  # Remove completed task
            st.rerun()  # Refresh UI
else:
    st.info("No tasks added yet!")
st.warning("Click on checkbox that task you completed todo app remove the completed task")

