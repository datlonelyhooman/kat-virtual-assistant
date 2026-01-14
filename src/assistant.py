from src.intents import get_intent
from src.tasks import execute_task

def handle_input(user_input):
    intent = get_intent(user_input)

    if intent == "unknown":
        if "?" in user_input or len(user_input.split()) > 2:
            from src.tasks import fetch_from_wikipedia
            return fetch_from_wikipedia(user_input)
        return "Sorry, I didn't understand that."

    return execute_task(intent)