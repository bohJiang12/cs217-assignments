"""
The script for building a Streamlit app for note-taking
"""

import streamlit as st

from notes import Notebook

nb = Notebook()

if not 'count' in st.session_state:
    st.session_state.count = 0

if "name_input" not in st.session_state:
    st.session_state.name_input = ""
if "text_input" not in st.session_state:
    st.session_state.text_input = ""

def click_add_note(name: str, text: str):
    """Function to call once clicking 'Add note' button"""
    if name and text:
        nb.add(new_name, new_text)
        st.session_state.name_input, st.session_state.text_input = "", ""
        st.info('Successfully added!')
    else:
        st.info('Incomplete note has been entered.')


"# Notebook"

# Sidebar of the website
#
# Function: search any existing note by giving a term
with st.sidebar:
    term = st.text_input(label="Search by a term:")

    st.write("**Notes found:**")

    if term:
        notes_found = nb.find(term=term)
    else:
        notes_found = nb.notes()

    for note in notes_found:
        # st.text_area(label='notes:', value=note)
        st.text(note)

    if st.button('Clear notes'):
        nb.clear()
        st.session_state["refresh"] = True
        st.rerun()



# Tabs for either: show notes or add a new note
show_note_tab, add_note_tab = st.tabs(["Show note", "Add note"])

# Show note tab:
with show_note_tab:
    exist_notes = nb.notes()
    selected_note = st.selectbox('Select a note', exist_notes)
    st.text("Contents:")
    st.info(nb[selected_note].text())


# Add note tab:
with add_note_tab:
    new_name = st.text_input(label='Name:', key='name_input')
    new_text = st.text_area(label='Contents:', key='text_input')
    st.button('Add note', on_click=click_add_note, args=(new_name, new_text))

    # Alternative way of adding note:
    # however, entered texts would be cleared after adding
    #
    # if st.button('Add note'):
    #     if new_name and new_text:
    #         nb.add(new_name, new_text)
    #         st.info('Successfully added!')
    #         st.rerun()
    #     else:
    #         st.info('Incomplete note has been entered.')



