conversation_memory = []

def save_to_memory(user_message, ai_response):
    conversation_memory.append({
        "user": user_message,
        "bot": ai_response
    })

def get_memory():
    return conversation_memory
