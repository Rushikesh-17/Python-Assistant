import ctypes
import datetime
import os
import pickle
import time
import webbrowser
import pyjokes
import requests
import wikipedia
import winshell
import wolframalpha
import random
import engine as e

a = e.Assistant()
def update_names():
    AName = open('Assistant_name.pickle', 'rb')
    global ass_name
    ass_name = pickle.load(AName)
    AName.close()
    UName = open('User_name.pickle', 'rb')
    global username
    username = pickle.load(UName)
    UName.close()

update_names()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        a.speak("Good Morning Sir !")

    elif hour >= 12 and hour < 18:
        a.speak("Good Afternoon Sir !")

    else:
        a.speak("Good Evening Sir !")

    a.speak("I am your Assistant")
    a.speak(ass_name)


def user_name():
    a.speak("Welcome Mister")
    a.speak(username)
    a.speak("How can i Help you, Sir")


def process_Query(query):
    if 'search in wikipedia' in query:
        a.speak('Searching Wikipedia...')
        query = query.replace("search in wikipedia", "")
        results = wikipedia.summary(query, sentences=3)
        a.speak("According to Wikipedia")
        print(results)
        a.speak(results)

    elif 'hello' in query :
        a.speak(f"Hello {username}")

    elif 'open youtube' in query:
        a.speak("Here you go to Youtube\n")
        webbrowser.open("youtube.com")

    elif 'open google' in query:
        a.speak("Here you go to Google\n")
        webbrowser.open("google.com")

    elif "where is" in query:
        query = query.replace("where is", "")
        location = query
        a.speak("User asked to Locate")
        a.speak(location)
        webbrowser.open("https://www.google.com/maps/search/" + location + "")

    elif 'play music' in query or "play song" in query:
        a.speak("Here you go with music")
        music_dir = "C:\\Users\\Rushikesh\\Music"
        songs = os.listdir(music_dir)
        print(songs)
        r= random.randint(0,len(songs))
        os.startfile(os.path.join(music_dir, songs[r]))

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        a.speak(f"Sir, the time is {strTime}")

    elif "change my name" in query:
        query = query.replace("change my name", "")
        a.speak("What would you like me to call you sir")
        usrname=a.takeCommand()
        A = open("User_name.pickle", "wb")
        pickle.dump(usrname, A)
        A.close()
        update_names()
        a.speak(f"Welcome mister {username}")

    elif "change your name " in query:
        a.speak("What would you like to call me, Sir ")
        assname = a.takeCommand()
        A = open("Assistant_name.pickle", "wb")
        pickle.dump(assname, A)
        A.close()
        update_names()
        a.speak("Thanks for naming me")

    elif "what's your name" in query or "what is your name" in query:
        a.speak("My friends call me")
        a.speak(ass_name)
        print("My friends call me", ass_name)

    elif "who made you" in query or "who created you" in query:
        a.speak("I have been created by rushi kesh , Krishna , Jeevan , Prince.")

    elif 'tell me a joke' in query:
        joke = pyjokes.get_joke()
        a.speak(joke)
        print(joke)

    elif "calculate" in query:
        app_id = "9EXUYP-ERW6R34ARE"
        client = wolframalpha.Client(app_id)
        query = query.replace("calculate","")
        res = client.query(query)
        answer = next(res.results).text
        print("The answer is " + answer)
        a.speak("The answer is " + answer)

    elif 'search' in query :
        query = query.replace("search", "")
        webbrowser.open(query)


    elif 'reason for your creation' in query:
        a.speak("I was created as a Mini project ")


    elif 'lock window' in query:
        a.speak("locking the device")
        ctypes.windll.user32.LockWorkStation()

    elif 'empty recycle bin' in query:
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
        a.speak("Recycle Bin Recycled")

    elif "don't listen" in query or "stop listening" in query:
        a.speak("for how much time you want to stop jarvis from listening commands")
        t = int(a.takeCommand())
        time.sleep(t)
        print(a)



    elif "write a note" in query:
        a.speak("What should i write, sir")
        note = a.takeCommand()
        file = open('jarvis.txt', 'a')
        a.speak("Sir, Should i include date and time")
        snfm = a.takeCommand()
        if 'yes' in snfm or 'sure' in snfm:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            file.write(strTime+"\t")
            file.write(" :-  ")
            file.write(note+"\n")
        else:
            file.write(note+"\n")

    elif "show note" in query:
        a.speak("Showing Notes")
        file = open("jarvis.txt", "r")
        print(file.read())
        a.speak(file.read(6))

    elif "weather" in query:
        # Google Open weather website
        # to get API of Open weather
        api_key = "b949ca8a5f5f4e5983fed493092031a6"
        weather_url = "http://api.openweathermap.org/data/2.5/weather?"
        city_name = "Mumbai"
        location = str(city_name)
        url = weather_url + "appid=" + api_key + "&q=" + location
        js = requests.get(url).json()
        print(js)
        if js["cod"] != "404":
            weather = js["main"]
            tempk = weather["temp"]
            tempc = round(ktoc(tempk))

            hum = weather["humidity"]
            desc = js["weather"][0]["description"]
            resp_string = " The temperature is " + str(tempc) + "degree celsius. The humidity is " + str(
                hum) + " and The weather description is " + str(desc)
            a.speak(resp_string)
        else:
            a.speak("City Not Found")


    elif "open wikipedia" in query:
        webbrowser.open("wikipedia.com")

    elif "good morning" in query or "good afternoon" in query or "good evening" in query or "good night" in query:
        a.speak("Have A " + query + " Sir ")

    elif 'how are you' in query:
        a.speak("I am fine, Thank you")
        a.speak(f"How are you, {username}")

    elif 'who are you' in query:
        a.speak(f"My name is {ass_name}")

    elif 'fine' in query or "good" in query:
        a.speak("It's good to know that your fine")

    elif 'exit' in query:
        a.speak("Thanks for giving me your time")
        exit()

    else:
        a.speak("Sorry I can't give response to your query")
        a.speak("We will try to resolve it in future versions")
        if query != "none":
            file = open('ForFutureVersions.txt', 'a')
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            file.write(username + ":" + strTime)
            file.write(" :- ")
            file.write(query + "\n")
            file.close()

def ktoc(k):
    celsius = k - 273.15
    return celsius


