# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 14:39:32 2021

@author: Chekuri Viroopaksh
"""

'''
Try changing the wish function to wish you according
to the day and the occasion.

Define a set of words like won't, could'nt etc and separate them to
will not, could not etc. Use this to take the command and
use this to determine if not is present in the command to segregate between
positive and negative statements

Do that github student pack for domain names
'''

import pyttsx3,datetime,sys,wikipedia,smtplib,os,pyautogui,psutil,pyjokes
import speech_recognition as sr
import webbrowser as wb

engine=pyttsx3.init()

voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def wish():
    '''
    No parameters
    
    Greets the user based on the time
    
    Returns
    -------
    None.

    '''
    speak("Welcome Back sir!",210)
    hour=datetime.datetime.now().hour
    if 6<=hour<=12:
        speak("Good morning",210)
    elif 12<=hour<=18:
        speak("Good afternoon",210)
    elif 18<=hour<=24:
        speak("Good evening",210)
    else:
        speak("Good night",210)
    speak("I am friday! Happy to see you back! ",210)
def time():
    '''
    No parameters
    
    Returns
    -------
    Returns the current time in hours:minutes:seconds format
    using the datetime module.

    '''
    time=datetime.datetime.now().strftime("%I:%M:%S PM")
    return time

def date():
    '''
    
    No parameters
    Returns
    -------
        
    Returns the date string in day date month year format
    Formatting uses the strftime from the datetime module

    '''
    return datetime.datetime.now().strftime("%A %d %B %Y")

def cpu():
    '''
    Tells the battery percentage and cpu usage 

    Returns
    -------
    None.

    '''
    usage=str(psutil.cpu_percent())
    speak("CPU is at "+usage)
    battery=psutil.sensors_battery
    speak("Battery is at ")
    speak(battery().percent)


def screenshot():
    '''
    Takes a screenshot of the present screen using pyautogui

    Returns
    -------
    None.

    '''
    img=pyautogui.screenshot()
    img.save("C:\\Users\\kabali\\OneDrive\\Desktop\\Screenshot.png")
    
def takeCommand():
    '''
    This function takes the command from the user
    voice and prints if it is able to understand

    Returns
    -------
    String.
    The command given by the user through the speech
    '''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ....")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language="en-in")
        #print(query)
    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"
    return query

def speak(audio,VoiceRate=200):
    '''
    
    The function sets up the virtual assistant to speak the 
    text passed as an argument 'audio' in the passed in speed 'VoiceRate'

    Parameters
    ----------
    audio : string 
    For the virtual assistant to speak
    VoiceRate : It is the speed of the virtual assistant to speak in 
    
        
    Function does not return anything.
    -------
    None.

    '''
    engine.setProperty('rate',VoiceRate)
    engine.say(audio)
    engine.runAndWait()

def sendmail(to,content):
    '''
    Sends mail to the receiver 
    directly with the content as the message body

    Parameters
    ----------
    to : String
    Mail address of the receiver.
    
    content : String
    Content to be sent to the receiver through mail.

    Returns
    -------
    None.

    '''
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('chekuriviroopaksh4950@gmail.com','viroopak')
    server.sendmail('chekuriviroopaksh4950@gmail.com',to,content)
    server.close()
    pass

def jokes():
    '''
    Tells a joke to us using pyjokes module

    Returns
    -------
    None.

    '''
    speak(pyjokes.get_joke())

if __name__=="__main__":
    wish()
    while True:
        query=takeCommand().lower()
        if query!="none":
            print(query)
        else:
            speak("Didn't understand that .")
            continue
        if "time" in query:
            speak("Time is "+time(),190)
            if "date" in query:
                speak("Today is "+date(),190)
        elif "offline" in query:
            speak("Going offline sir.",190)
            sys.exit(0)
        elif "wikipedia" in query:
            speak("Searching...")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2)
            speak(result)
        elif "send" in query and ("mail" in query or "email" in query):
            try:
                speak("What should i Say?")
                content=takeCommand()
                to="chekuriviroopaksh@gmail.com"
                sendmail(to,content)
                speak("Email sent successfully")
            except Exception as e:
                speak(e)
                speak("Unable to send the message")
        elif "search" in query and ("chrome" in query or "google" in query):
            speak("What should I search")
            chromepath="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s"
            search=takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+".com")
        elif "logout" in query:
            os.system("shutdown -1")
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")
        elif "restart" in query:
            os.system("shutdown /r /t 1")
        elif "play songs" in query:
            songs_dir=""
            #Try this so that asst plays songs from youtube or other app
        elif "remember" in query:
            speak("What should I remember?")
            data=takeCommand()
            speak("You said me to remember "+data)
            
            remember=open("C:\\Users\\kabali\\OneDrive\\data.txt","a")
            remember.append(data+"\n")
            remember.close()
        elif "what did i say to remember" in query:
            data=open("C:\\Users\\kabali\\OneDrive\\data.txt",'r')
            speak("You said to remember "+data.readlines()[-1])
        elif "screenshot" in query and "take" in query:
            screenshot()
            speak("Screenshot taken and saved to desktop in name of Screenshot.png")
        elif "battery percent" in query or "cpu usage" in query:
            cpu()
        elif "joke" in query:
            jokes()