# pip install pyttsx3
import pyttsx3

if __name__ == "__main__":
    print("Welcome to Text to Speech Converter")
    engine = pyttsx3.init() # init() gets an engine instance for the speech synthesis
    while True:
        x = input("Enter the text to convert to speech: ")
        if x == "x":
            engine.say('Bye Bye')
            engine.runAndWait() # runAndWait() processes the voice commands queued up to that point
            break
        engine.say(x)
        engine.runAndWait()
