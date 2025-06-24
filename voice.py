# === voice.py ===

import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def say(text):
    print(f"Echolish: {text}")
    engine.say(text)
    engine.runAndWait()

def take_command():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5)
            print("Recognizing...")
            query = recognizer.recognize_google(audio)
            return query
        except sr.UnknownValueError:
            say("Sorry, I couldn't understand.")
        except sr.WaitTimeoutError:
            say("I didn't hear anything.")
        except Exception as e:
            print(f"Voice Error: {e}")
            say("Sorry, something went wrong.")
        return ""