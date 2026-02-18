from speech import listen, speak
from commands import execute_command
from utils import wish_user

def main():
    wish_user()
    speak("Hello, I am Echo assistant. How can I help you?")

    running = True

    while running:
        query = listen()

        if query:
            running = execute_command(query)

if __name__ == "__main__":
    main()
