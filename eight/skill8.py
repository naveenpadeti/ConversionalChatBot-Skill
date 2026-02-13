import speech_recognition as sr

def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        return "Sorry, I didn't understand."

def generate_response(text, context):
    text = text.lower()

    if "hello" in text:
        return "Hello! How can I help you?"
    elif "time" in text:
        return "I can help you with that. Please enable time access."
    else:
        return "Can you please repeat that?"

from gtts import gTTS
import os

def text_to_speech(response):
    tts = gTTS(text=response, lang='en')
    tts.save("response.mp3")
    os.system("start response.mp3")  # Windows

context = {}

while True:
    user_text = speech_to_text()
    response = generate_response(user_text, context)
    print("Bot:", response)
    text_to_speech(response)

