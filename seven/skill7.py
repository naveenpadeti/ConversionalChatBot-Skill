class DialogueState:
    def __init__(self):
        self.intent = None
        self.slots = {}

state = DialogueState()

def detect_intent(text):
    if "flight" in text.lower():
        return "book_flight"
    return "unknown"

def update_slots(text, state):
    cities = ["hyderabad", "delhi", "mumbai"]
    for city in cities:
        if city in text.lower():
            if "source" not in state.slots:
                state.slots["source"] = city
            else:
                state.slots["destination"] = city

def next_action(state):
    if "source" not in state.slots:
        return "ask_source"
    if "destination" not in state.slots:
        return "ask_destination"
    return "confirm_booking"

def generate_response(action):
    responses = {
        "ask_source": "From which city?",
        "ask_destination": "Where do you want to go?",
        "confirm_booking": "Your flight has been booked!"
    }
    return responses[action]

