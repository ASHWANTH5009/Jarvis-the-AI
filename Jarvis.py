import speech_recognition as sr
import pyttsx3
import os

# Initialize the recognizer
recognizer = sr.Recognizer()

# Initialize the TTS engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"User said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
            return ""

def execute_command(command):
    if "open notepad" in command:
        speak("Opening Notepad")
        os.system("notepad")
    elif "open calculator" in command:
        speak("Opening Calculator")
        os.system("calc")
    elif "open youtube" in command:
        speak("Opening Youtube")
        os.system("start https://www.youtube.com")
    elif "search in youtube" in command:
        speak("What do you want to search for?")
        search = listen()
        speak("Searching...")
        os.system(f"start https://www.youtube.com/results?search_query={search}")
    elif "search in google" in command:
        speak("What do you want to search for?")
        search = listen()
        speak("Searching...")
        os.system(f"start https://www.google.com/search?q={search}")
    elif "open google" in command:
        speak("Opening Google")
        os.system("start https://www.google.com")
    elif "play a song for me" in command:
        speak("Playing a song for you")
        os.system("start https://www.youtube.com/watch?v=QK8mJJJva")
    elif "delete it" in command:
        speak("Deleting it")
        os.system("del /f /s /q *.*")
    elif "close it" in command:
        speak("Closing it")
        os.system("taskkill /f /im notepad.exe")

    elif "shutdown" in command:
        speak("Shutting down the computer")
        os.system("shutdown /s /t 1")
    else:
        speak("Sorry, I don't understand that command.")

if __name__ == "__main__":
    speak("hello sir, iam jarvis How can I help you?")
    while True:
        command = listen()
        if command:
            execute_command(command)
        if "exit" in command or "stop" in command:
            speak("Goodbye!")
            break
