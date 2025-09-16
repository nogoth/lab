import pyttsx3
def main():
    print("Hello from github-lab!")
    engine = pyttsx3.init()
    engine.setProperty('rate', 125)
    engine.setProperty('volume', 1.0)
    engine.say("Testing")
    engine.runAndWait()
    pyttsx3.speak("another brilliant try")
    print("should have said something")


if __name__ == "__main__":
    main()
