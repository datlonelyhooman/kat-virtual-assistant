def get_intent(text):
    text = text.lower()

    if any(word in text for word in ["hi", "hello", "hey"]):
        return "greeting"

    if "time" in text:
        return "time"

    if "open google" in text:
        return "open_google"

    if "exit" in text:
        return "exit"

    if any(word in text for word in ["ok", "thanks", "thank you"]):
        return "polite"

    return "unknown"
