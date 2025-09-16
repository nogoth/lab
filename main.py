import pyttsx3

def main():

    engine = pyttsx3.init()
    engine.setProperty('rate', 70)
    engine.setProperty('volume', 1.0)
    engine.setProperty('voice', 'mb-en1')
    engine.setProperty('voice', 'en')

    voices = engine.getProperty('voices')
    print(voices[0])
    printVoices(voices)

#    engine.setProperty('voice', 'us-mbrola-1')
    engine.say("this a test of the engine and it can say things")
    engine.runAndWait()
    # example of just running with a speak, engine is a global so it'll remember what was set up
    pyttsx3.speak("what is that you need grace in")
    engine.stop()

def printVoices(voicesArray):
    map(lambda x: print(x), voicesArray)
    for x in voicesArray:
        print(x)


if __name__ == "__main__":
    main()
