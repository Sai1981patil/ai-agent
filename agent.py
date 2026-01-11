import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
engine.say("AI agent is ready")
engine.runAndWait()

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Listening...")
    audio = r.listen(source)

try:
    command = r.recognize_google(audio)
    print("You said:", command)
except:
    print("Could not understand")
