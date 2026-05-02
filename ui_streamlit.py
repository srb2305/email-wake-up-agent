import streamlit as st
from memory.conversation_repo import ConversationRepo

st.set_page_config(page_title="Email Wake-Up Agent Dashboard", layout="wide")
st.title("📧 Email Wake-Up Agent Dashboard")

repo = ConversationRepo()
threads = repo.get_all_threads()

st.sidebar.header("Conversation Threads")
selected_thread = st.sidebar.selectbox("Select a thread:", threads)

if selected_thread:
    st.subheader(f"Conversation: {selected_thread}")
    messages = repo.get_conversation(selected_thread)
    for sender, receiver, content, timestamp, direction in messages:
        with st.expander(f"{timestamp} | {direction.upper()} | {sender} → {receiver}"):
            st.write(content)

st.sidebar.markdown("---")
st.sidebar.write("Reload the page to refresh conversations.")
