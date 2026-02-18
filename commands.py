import webbrowser
import wikipedia
import os
from speech import speak, stop_voice
from ai_brain import ask_ai


def execute_command(query):

    # -------- STOP SPEECH --------
    if "stop" in query:
        stop_voice()
        print("Echo: Stopped")
        return True

    # -------- GOOGLE --------
    elif "google" in query:
        speak("Opening Google")
        print("Echo: Opening Google")
        webbrowser.open("https://google.com")

    # -------- YOUTUBE --------
    elif "youtube" in query:
        speak("Opening YouTube")
        print("Echo: Opening YouTube")
        webbrowser.open("https://youtube.com")

    # -------- WIKIPEDIA --------
    elif "wikipedia" in query:
        speak("Searching Wikipedia")
        topic = query.replace("wikipedia", "").strip()

        try:
            result = wikipedia.summary(topic, sentences=2)

            print("\nEcho:", result)
            speak(result)

        except Exception as e:
            print("Error:", e)
            speak("Sorry, I couldn't find information")

    # -------- NOTEPAD --------
    elif "notepad" in query:
        speak("Opening Notepad")
        print("Echo: Opening Notepad")
        os.startfile("C:/WINDOWS/system32/notepad.exe")

    # -------- EXIT --------
    elif "exit" in query or "bye" in query:
        speak("Goodbye")
        print("Echo: Goodbye")
        return False

    # -------- AI FALLBACK --------
    else:
        try:
            print("DEBUG → AI block entered")

            speak("Let me think")

            reply = ask_ai(query)

            print("DEBUG → AI reply received")

            print("\nEcho:", reply)

            speak(reply)

        except Exception as e:
            print("AI ERROR:", e)

    return True