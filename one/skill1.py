def chatbot(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you?"

    elif "how are you" in user_input:
        return "I'm just a chatbot, but I'm doing great 😊"

    elif "your name" in user_input:
        return "I am a rule-based chatbot."

    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a nice day 👋"

    else:
        return "Sorry, I didn't understand that."


# Chat loop
print("Chatbot: Hi! Type 'bye' to exit.")

while True:
    user = input("You: ")
    response = chatbot(user)
    print("Chatbot:", response)

    if "bye" in user.lower():
        break