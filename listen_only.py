import speech_recognition as sr

MIC_INDEX = 0   # CHANGE THIS to your mic index from list_mics.py

r = sr.Recognizer()
r.energy_threshold = 300
r.dynamic_energy_threshold = False

mic = sr.Microphone(device_index=MIC_INDEX)

with mic as source:
    r.adjust_for_ambient_noise(source, duration=1)
    print("🎤 Ready. Speak...")

while True:
    try:
        with mic as source:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
        text = r.recognize_google(audio)
        print("You said:", text)
    except Exception as e:
        print("Listening error:", e)

