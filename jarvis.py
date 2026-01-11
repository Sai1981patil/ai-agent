import speech_recognition as sr
import pyttsx3
import subprocess
import time

# ================= VOICE SETUP =================
engine = pyttsx3.init()
engine.setProperty("rate", 165)
engine.setProperty("volume", 1.0)

voices = engine.getProperty("voices")
for v in voices:
    if "david" in v.name.lower() or "male" in v.name.lower():
        engine.setProperty("voice", v.id)
        break

def speak(text):
    print("AI:", text)
    engine.say(text)
    engine.runAndWait()

# ================= SPEECH SETUP =================
recognizer = sr.Recognizer()
mic = sr.Microphone()

WAKE_WORD = "jarvis"

# ================= APP COMMANDS =================
APP_COMMANDS = {
    "notepad": "notepad",
    "calculator": "calc",
    "calc": "calc",
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "edge": "msedge",
    "explorer": "explorer",
    "files": "explorer",
    "cmd": "cmd",
    "terminal": "wt",
    "settings": "start ms-settings:",
}

# ================= COMMAND HANDLER =================
def execute_command(text):
    for app in APP_COMMANDS:
        if app in text:
            speak(f"Opening {app}")
            subprocess.Popen(APP_COMMANDS[app], shell=True)
            return True
    return False

# ================= MAIN LOOP =================
print("🟢 Jarvis AI online")
speak("Jarvis AI online")

while True:
    try:
        print("🎤 Listening...")
        with mic as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.4)
            audio = recognizer.listen(source)

        text = recognizer.recognize_google(audio).lower()
        print("You said:", text)

        # Must contain wake word
        if WAKE_WORD in text:
            print("⚡ Wake detected")
            command_text = text.replace(WAKE_WORD, "").strip()

            if command_text:
                print("🧠 Processing...")
                if not execute_command(command_text):
                    speak("I did not understand that command.")
            else:
                speak("I am listening.")

    except sr.UnknownValueError:
        pass
    except Exception as e:
        print("Error:", e)
