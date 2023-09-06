import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


class Assistant():
    def speak(audio, string):
        engine.say(string)
        engine.runAndWait()

    def takeCommand(string):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            Assistant.speak("","Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            Assistant.speak("", "Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"you said: {query}\n")
        except Exception as e:
            print(e)
            Assistant.speak("Unable to Recognize your voice.")
            return "None"
        return query
