import datetime
import os
from os import system
import subprocess
import webbrowser
from time import ctime, time
import requests
from requests import get
import pyttsx3
import cv2
from cv2 import split
import speech_recognition as sr
from wikipedia import wikipedia
import sys
import pyautogui
import pyjokes 
import instaloader 
from urllib3 import Timeout   
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTime,QTimer,QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvisui1 import Ui_jarvisUi




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',170)



def speak(audio):
    engine.say(audio)
    print(audio)

    engine.runAndWait()




# to wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if 0 <= hour < 12:
        speak("Good Morning")
    elif 12 < hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("This is jack")
    speak("How can I help you")
    



class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.TaskExecution()

    def takecommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en_in")
            print(f"user said:{query}")

        except Exception as e:
            speak("say that again please..")
            return "none"
        return query

    def TaskExecution(self):
        wish()
        while True:
        #if 1:

            self.query = self.takecommand().lower()
            # logic

            if "open notepad" in self.query:
                apath = "C:\\WINDOWS\\system32\\notepad.exe"
                os.startfile(apath)
            elif "open cmd" in self.query:
                bpath = "C:\WINDOWS\system32\\cmd.exe"
                os.startfile(bpath)

            elif "open wordpad" in self.query:
                bpath = "C:\Program Files\Windows NT\Accessories\wordpad.exe"
                os.startfile(bpath)

            elif 'what is the time' in self.query:
                speak("Sir the time is :" + ctime())
            
                
            elif 'open gmail' in self.query:
                webbrowser.open_new_tab("https://mail.google.com/mail/u/0/#inbox")
                speak("Google Mail open now")
                
            elif 'who are you' in self.query or 'what can you do' in self.query or 'what is your name' in self.query:
                speak('I am jack version 1 point O your persoanl assistant. I am programmed to minor tasks like'
                    'opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather'
                    'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')
            
            elif 'open camera' in self.query:
                cap=cv2.VideoCapture(0)
                while True:
                    ret,img=cap.read()
                    cv2.imshow('webcam',img)
                    k=cv2.waitKey(1)
                    if k==27:
                        break
                cap.release()
                cv2.destroyWindow()
            

            

            elif "ip address" in self.query:
                ip = get('https://api.ipify.org').text
                speak(f"your ip address is {ip}")

            elif "open facebook" in self.query:
                webbrowser.open("https://www.google.com")

           
            elif "open stack overflow" in self.query:
                 
                 webbrowser.open("www.stackoverflow.com")

            elif 'open youtube' in self.query:
                
                 webbrowser.open("https://youtube.com")

               
            elif 'news' in self.query:
                news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
                speak('Here are some headlines from the Times of India,Happy reading')
                

            elif "log off" in self.query or "sign out" in self.query:
                speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
                subprocess.call(["shutdown", "/l"])

            elif "weather" in self.query:
                api_key = "8ef61edcf1c576d65d836254e11ea420"
                base_url = "https://api.openweathermap.org/data/2.5/weather?"
                speak("whats the city name")
                city_name = self.takecommand()
                complete_url = base_url + "appid=" + api_key + "&q=" + city_name
                response = requests.get(complete_url)
                x = response.json()
                if x["cod"] != "404":
                    y = x["main"]
                    current_temperature = y["temp"]
                    current_humidiy = y["humidity"]
                    z = x["weather"]
                    weather_description = z[0]["description"]
                    speak(" Temperature in kelvin unit is " +
                        str(current_temperature) +
                        "\n humidity in percentage is " +
                        str(current_humidiy) +
                        "\n description  " +
                        str(weather_description))
                    print(" Temperature in kelvin unit = " +
                        str(current_temperature) +
                        "\n humidity (in percentage) = " +
                        str(current_humidiy) +
                        "\n description = " +
                        str(weather_description))

                else:
                    speak(" City Not Found ")

           

            elif "open c drive" in self.query:
                apath = "C:\\"
                os.startfile(apath)

            elif "open d drive" in self.query:
                apath = "D:\\"
                os.startfile(apath)

            elif "open e drive" in self.query:
                apath = "E:\\"
                os.startfile(apath)

            

            elif "wikipedia" in self.query:

                speak('searching wikipedia.......')
                self.query = self.query.replace('wikipedia', " ")
                result = wikipedia.summary(self.query, sentences=2)
                speak('according to wikipedia')
                speak(result)
                #print(result)

            elif "open google" in self.query:
                speak('sir , what should search on google')
                cm = self.takecommand().lower()
                webbrowser.open(f"{cm}")

            
            #to find a joke
            elif "tell me a joke" in self.query:
                joke = pyjokes.get_joke()
                speak(joke)

            elif "log off" in self.query or "sign out" in self.query:
                speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
                subprocess.call(["shutdown", "/l"])
            

            #------------------To check a instagram profile----
            elif "instagram profile" in self.query or "profile on instagram" in self.query:
                  speak("sir please enter the user name correctly.")
                  name = input("Enter username here:")
                  webbrowser.open(f"www.instagram.com/{name}")
                  speak(f"sir here is the profile of the user {name}")
                  speak("sir would you like to dowload profile picture of this account.")
                  condition =self.takecommand().lower()
                  if "yes" in condition:
                    mod = instaloader.Instaloader() #pip install instadownloader
                    mod.download_profile(name, profile_pic_only=True)
                    speak("i am done sir, profile picture is saved in our main folder. now i am ready for next command")
                  else:
                   pass




                 #------------------  To take screenshot ---------

            elif "take screenshot" in self.query or "take a screenshot" in self.query:
                speak("sir, please tell me the name for this screenshot file")
                name = self.takecommand().lower()
                speak("pleae sir hold the screen for few seconds, i am taking screenshot")
                
                img = pyautogui.screenshot()
                img.save(f"{name}.png")
                speak("i am done sir, the screenshot is saved in our main folder. now i am ready for next command")


              
            
            
        
            
            elif "tell me the news" in self.query :
                speak("please wait sir, fetching the latest news")
                news()

            

            elif 'exit' in self.query:
                speak('Thanks have a good day ')
                exit()



startExecution = MainThread()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_jarvisUi()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)
        
    

    
    def startTask(self):
        self.ui.movie = QtGui.QMovie("EllipticalCostlyChrysomelid-size_restricted.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("initiating.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("flo-motion_5sec.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date =current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)

app=QApplication(sys.argv)
jarvis = Main()
jarvis.show()
sys.exit(app.exec_())


