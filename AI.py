import pyttsx3


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)


if __name__ == "__main__":
    speak("Sir please type the text that you want to hear!")
    speak(input())
