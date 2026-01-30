START = "start"
ASK_SOURCE = "ask_source"
ASK_DEST = "ask_destination"
ASK_DATE = "ask_date"
CONFIRM = "confirm"

context = {
    "state": START,
    "source": None,
    "destination": None,
    "date": None
}

def chatbot(user_input, context):

    if context["state"] == START:
        context["state"] = ASK_SOURCE
        return "Sure! Where are you traveling from?"

    elif context["state"] == ASK_SOURCE:
        context["source"] = user_input
        context["state"] = ASK_DEST
        return "Great! Where do you want to go?"

    elif context["state"] == ASK_DEST:
        context["destination"] = user_input
        context["state"] = ASK_DATE
        return "When do you want to travel?"

    elif context["state"] == ASK_DATE:
        context["date"] = user_input
        context["state"] = CONFIRM
        return (
            f"Please confirm:\n"
            f"From: {context['source']}\n"
            f"To: {context['destination']}\n"
            f"Date: {context['date']}\n"
            f"Type 'yes' to confirm."
        )

    elif context["state"] == CONFIRM:
        if "yes" in user_input.lower():
            context["state"] = START
            return "✅ Ticket booked successfully!"
        else:
            context["state"] = START
            return "❌ Booking cancelled."

print("Chatbot: Hi! I can help you book a ticket.")

while True:
    user = input("You: ")
    print("Chatbot:", chatbot(user, context))

slots = {
    "source": None,
    "destination": None,
    "date": None
}

def slot_filling_bot(user_input, slots):

    if slots["source"] is None:
        slots["source"] = user_input
        return "Where do you want to go?"

    elif slots["destination"] is None:
        slots["destination"] = user_input
        return "When do you want to travel?"

    elif slots["date"] is None:
        slots["date"] = user_input
        return (
            f"Booking confirmed from {slots['source']} "
            f"to {slots['destination']} on {slots['date']} ✅"
        )

