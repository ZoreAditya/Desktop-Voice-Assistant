from datetime import datetime
from http import server
import re
from time import sleep
from keyboard import press
from bs4 import BeautifulSoup
from jmespath import search
from numpy import take
import pyttsx3
import datetime
from requests import request
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import pywhatkit
import smtplib
import requests
import sys
import pyautogui 
import pydirectinput
import googlescrap
import keyboard
import export


    
     
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
  
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

for i in range(3):
    passs=input("Enter the password: ")
    with open(r"C:\Users\DELL\OneDrive\Documents\Python\Password.txt","r") as file:
        password=file.read()
        file.close()
    if (passs==password):
        print("Password granted")
        break
    elif(i==2 and passs!=password):
        exit()    
    else:
        print("Try again")
   
       

     
def wishme():
    hour=int(datetime.datetime.now().hour)  
    if hour>=0 and hour<12:
        speak("Good morning Sir ")
    elif hour>=12 and hour<18:
        speak("Good afternoon Aditya")
    elif hour>=18 and hour<20:
        speak("Good afternoon Aditya")  
    elif hour>=20 and hour<24:
        speak("Good night Aditya")

def takecomments():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....") 
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        query=r.recognize_google(audio,language="en-in")
        print("Recognizing")

    except Exception as e:
            print("Say that again")
            return "None"
    return query  

def sendmail(to,content):
    server=smtplib.SMTP("smtp.google.com",587)
    server.ehlo
    server.login("adityazore00@gmail.com","Aditya@01")
    server.sendmail("adityazore00@gmail.com",to,content)
    server.close()

if __name__=="__main__":
    speak("Hello i am jarvis speaking sir")
    wishme()

    speak("What can i do for you:")

    while True: 
       
        query=takecomments().lower()
        if 'wikipedia' in query:
                speak("Searching ")
                query=query.replace("wikipedia","")
                results=wikipedia.summary(query,sentences=2)
                speak(results)
        
        elif "search" in query:
            query=query.replace("search","")
            url=str(query)+".com"
            chrome=r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            webbrowser.register("chrome",None,webbrowser.BackgroundBrowser(chrome))
            webbrowser.get("chrome").open_new_tab(url)
                        
        elif "play" in query:
                music="D:\\Music"
                song=os.listdir(music)
                os.startfile(os.path.join(music,song[random.randint(0,5)]))
        elif "youtube" in query:
                songs=query.replace("youtube","")
                speak("Your search is" + songs)
                print("Your search  is" + songs)
                pywhatkit.playonyt(songs)
        elif "time" in query:
                time=datetime.datetime.now().strftime("%I:%M:%p")
                speak("Time is "+time)
                print(time)
        elif "send mail " in query:
            try:
              speak("What should i write")
              content=query
              to="adityazore00@gmail.com"
              sendmail(to,content)    
            except Exception as e:
                print(e)  
        elif "temperature" in query:
            search="temperature in pune"
            url=f"https://www.google.com/search?q={search}"
            r=requests.get(url)
            data=BeautifulSoup(r.text,"html.parser")
            temp=data.find("div",class_="BNeawe").text
            speak(f"current{search} is {temp}")
            print(temp)

        elif "volume up" in query:
            pyautogui.press("volumeup") 
        
        elif "volume down" in query:
            pyautogui.press("volumedown") 
       
        elif "mute" in query:
            pyautogui.press("volumemute")

        elif "unmute" in query:
            pyautogui.press("volumeunmute")    

        elif "google" in query:
            query=query.replace("google","")
            speak("This what i found on google")
            pywhatkit.search(query)
            try:
                results=googlescrap.summary(query,2)
                speak(results)
            except Exception as e:
                speak(e)
       
            

        elif "new tab" in query:
            pyautogui.hotkey("ctrl","t")

        elif "incognito" in query:
            pyautogui.hotkey("ctrl","shift","n")        

        elif  "k" in query:
            pyautogui.hotkey("k")    
        elif "close window" in query:
            
            pyautogui.hotkey("ctrl","w")   


        # elif "launch" in query:
        #     from _launch_ import openapp
        #     openapp(query)     
       
        
                
                
                
        elif "stop" in query:
            speak("It was great working with you")
            sys.exit()    

           
    


                


