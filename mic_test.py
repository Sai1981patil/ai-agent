import speech_recognition as sr

r = sr.Recognizer()

print("Available microphones:")
for i, name in enumerate(sr.Microphone.list_microphone_names()):
    print(i, name)

with sr.Microphone() as source:
    print("Say something...")
    audio = r.listen(source)

print("You said:", r.recognize_google(audio))
