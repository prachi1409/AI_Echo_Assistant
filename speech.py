import speech_recognition as sr
import asyncio
import edge_tts
from playsound import playsound
import threading
import os

VOICE = "en-IN-NeerjaNeural"

# 🔥 Global flag
stop_speaking = False


async def speak_async(text):
    global stop_speaking

    filename = "voice.mp3"

    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(filename)

    if not stop_speaking:
        playsound(filename)

    if os.path.exists(filename):
        os.remove(filename)


def speak(text):
    global stop_speaking

    stop_speaking = False

    thread = threading.Thread(
        target=lambda: asyncio.run(speak_async(text))
    )

    thread.start()


def stop_voice():
    global stop_speaking
    stop_speaking = True


def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")

        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = recognizer.listen(source, timeout=7, phrase_time_limit=5)

            print("Recognizing...")
            query = recognizer.recognize_google(audio, language="en-IN")

            print("You said:", query)

            return query.lower()

        except:
            return ""