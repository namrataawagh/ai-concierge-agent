def classify_intent(message: str) -> str:
    if "book" in message.lower():
        return "booking"
    elif "cancel" in message.lower():
        return "cancellation"
    else:
        return "general"
