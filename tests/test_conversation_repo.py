from memory.conversation_repo import ConversationRepo

# Simple test for conversation memory

def main():
    repo = ConversationRepo()
    thread_id = "test-thread-1"
    repo.add_message(thread_id, "alice@example.com", "bob@example.com", "Hello Bob!", "sent")
    repo.add_message(thread_id, "bob@example.com", "alice@example.com", "Hi Alice!", "received")
    messages = repo.get_conversation(thread_id)
    print(f"Conversation for thread {thread_id}:")
    for msg in messages:
        print(f"{msg[3]} | {msg[0]} -> {msg[1]} | {msg[4]}: {msg[2]}")
    print("All threads:", repo.get_all_threads())

if __name__ == "__main__":
    main()
