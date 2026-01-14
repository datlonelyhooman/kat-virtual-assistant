import datetime
import webbrowser
import wikipedia
def execute_task(intent: str):
    if intent == "greeting":
        return "Hey! How can I help you today?"

    if intent == "time":
        now = datetime.datetime.now().strftime("%H:%M:%S")
        return f"The current time is {now}"

    if intent == "open_google":
        webbrowser.open("https://www.google.com")
        return "Opening Google."

    if intent == "polite":
        return "You're welcome 🙂"

    if intent == "exit":
        return "Goodbye!"

    return "Task not implemented."

def fetch_from_wikipedia(query: str):
    try:
        summary = wikipedia.summary(query, sentences=2)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return f"That term is ambiguous. Try being more specific. Options include: {e.options[:3]}"
    except wikipedia.exceptions.PageError:
        return "I couldn't find information on that topic."
    except Exception:
        return "Something went wrong while fetching information."
