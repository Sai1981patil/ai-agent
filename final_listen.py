import speech_recognition as sr

# 🔴 CHANGE THIS TO YOUR MIC INDEX
MIC_INDEX = 1   # example

r = sr.Recognizer()
r.energy_threshold = 300
r.dynamic_energy_threshold = False

mic = sr.Microphone(device_index=MIC_INDEX)

print("🟢 Microphone locked. Calibrating...")

with mic as source:
    r.adjust_for_ambient_noise(source, duration=1)

print("🟢 Ready. Speak now.")

while True:
    try:
        with mic as source:
            audio = r.listen(
                source,
                timeout=5,
                phrase_time_limit=5
            )

        text = r.recognize_google(audio)
        print("You said:", text)

    except sr.WaitTimeoutError:
        print("⏳ No speech detected")
    except sr.UnknownValueError:
        print("❌ Could not understand")
    except Exception as e:
        print("❌ ERROR:", e)
