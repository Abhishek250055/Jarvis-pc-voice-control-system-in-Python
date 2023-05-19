from re import S
import pyttsx3 #pip install pyttsx3 #pip install PyAudio
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib 
import PyPDF2 #read pdf
import pywhatkit #google search #play google youtube  any thing
import random #randem
import pyautogui #valumup and down
import webbrowser as web #youtube search
# import closeapp #function for close app
import screen_brightness_control as screen # screen_brightness_control 
import psutil #showing battery 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',200)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

 
#-----------------------------------------------wish by the marko --------------------------------------------------------------------------------
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am maarko Sir. Please tell me how may I help you")  


#----------------------------------------------- def function youtube search --------------------------------------------------------------------------------

def youtube_search(term):
    result="https://www.youtube.com//results?search_query="+term
    web.open(result)
    speak("According to youtube ")

    pywhatkit.playonyt(term)

#----------------------------------------------- read pdf file --------------------------------------------------------------------------------
def read_pdf():
    # creating a pdf file object
    book = open('E:\python\my marko\RDPD.pdf', 'rb')
    # creating a pdf reader object
    pdfReader = PyPDF2.PdfFileReader(book)
    # printing number of pages in pdf file
    pages_no=pdfReader.numPages
    speak(f"sir this is the rich dad poor dad book and total numbers of page is {pages_no} ")
    # creating a page object
    pageObj = pdfReader.getPage(int(10))
    text_pdf=pageObj.extractText()
    speak(text_pdf)
  
#-----------------------------------------------take command by user --------------------------------------------------------------------------------

def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query
#-----------------------------------------------send email --------------------------------------------------------------------------------

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('bisenabhishek65@gmail.com', 'enter your passs...')
    server.sendmail('bisenabhishek65@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()

#-----------------------------------------------for loop for time to play the code --------------------------------------------------------------------------------

    for i in range(0,100):
        query = takeCommand().lower()
#----------------------------------------------open wikipedia--------------------------------------------------------------------------------

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
#-----------------------------------------------open the youtube --------------------------------------------------------------------------------

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

#-----------------------------------------------open facebook--------------------------------------------------------------------------------

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

#-----------------------------------------------open google --------------------------------------------------------------------------------

        elif 'open google' in query:
            webbrowser.open("google.com")

#-----------------------------------------------open sreach google --------------------------------------------------------------------------------

        elif 'google search' in query:
            query = query.replace("google search", "")
            # query = query.replace("wikipedia", "")
            speak("According to google  ")
            try:
                pywhatkit.search(query)
                result=wikipedia.summary(query, sentences=1)
                speak(result)
            except:
                speak("not searching try again")

#-----------------------------------------------play video--------------------------------------------------------------------------------

        elif 'play video' in query:
            music_dir = 'C:\\Users\\HP\\Videos\\Harry Potter all'
            songs = os.listdir(music_dir)
            print(songs) #play video randam 
            r1 = random.randint(0, 7)
            os.startfile(os.path.join(music_dir, songs[r1]))

#-----------------------------------------------time  --------------------------------------------------------------------------------

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S") 
            print(strTime)   
            speak(f"Sir, the time is {strTime}")

#-----------------------------------------------open vs code --------------------------------------------------------------------------------

        elif 'open code' in query:
            codePath = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

#-----------------------------------------------open file--------------------------------------------------------------------------------

        elif 'open file' in query:
            codePath = "E:\\"
            os.startfile(codePath)  

#-----------------------------------------------email to pretion --------------------------------------------------------------------------------

        elif 'email to abhishek' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "bisenabhishek65@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Abhishek Bisen bhai. I am not able to send this email") 


#-----------------------------------------------volume system -------------------------------------------------------------------------------
        #----------volume_down -------------------------------------------------------------

        elif 'volume up' in query:
            pyautogui.press("volumeup")
        #----------volume_down -------------------------------------------------------------

        elif 'volume down' in query:
            pyautogui.press("volumedown")

        #----------volume_down -------------------------------------------------------------

        elif 'volume mute' in query:
            pyautogui.press("volumemute")


#----------------------------------------------------------------- screen_brightness_up and down-------------------------------------------------------------

        elif 'brightness down' in query:
            screen.set_brightness(0)

        #----------volume_down -------------------------------------------------------------
        
        elif 'brightness up' in query:
            screen.set_brightness(80)


#----------------------------------------------------------------- screen_brightness_up and down-------------------------------------------------------------
        elif 'battery power' in query:
            battery = psutil.sensors_battery()
            b=str(battery.percent)
            # b_left=str(battery.secsleft)
            speak("your pc Battery percentage is"+b)
            # speak("your pc Battery left in"+b_left)
            print("Battery percentage : ", battery.percent)
            
            
#-----------------------------------------------read a book--------------------------------------------------------------------------------

        elif 'read book' in query:
           read_pdf()

#-----------------------------------------------hello marko how are you --------------------------------------------------------------------------------

        elif "hello" in query:
            speak("Hello sir, how are you ?")
        elif "i am fine" in query:
            speak("that's great, sir")
        elif "how are you" in query:
            speak("Perfect, sir")
        elif "thank you" in query:
            speak("you are welcome, sir")
        elif "who are you" in query:
            speak("sir i my maarko")
             


#-----------------------------------------------other fuction--------------------------------------------------------------------------------
        # elif "news" in query:
            # from NewsRead import latestnews
            # latestnews()

#-----------------------------------------------shutdown the system --------------------------------------------------------------------------------

        elif "shutdown the system" in query:
            speak("Are You sure you want to shutdown")
            shutdown = input("Do you wish to shutdown your computer? (yes/no)")
            if shutdown == "yes":
                os.system("shutdown /s /t 1")
            elif shutdown == "no":
                break

#-----------------------------------------------youtube search --------------------------------------------------------------------------------

        elif "youtube search" in query:
            query = query.replace("youtube search", "")
            youtube_search(query)

 #-------------------------------------------------pc open-------------------------------------------------------------

        elif 'open pc' in query:
            query=query.replace("open pc","")
            # query=query.replace("open pc","")
            pyautogui.press("super")
            pyautogui.typewrite(query)
            pyautogui.sleep(1)
            pyautogui.press("enter")

#-------------------------------------------------pc open-------------------------------------------------------------

        # elif 'close' in query:
        #     query=query.replace("close","")
        #     closeapp.close(query)
        #     # speak("close the app")




#-------------------------------------------------networl speed-------------------------------------------------------------

# elif "internet speed" in query:
#                     wifi  = speedtest.Speedtest()
#                     upload_net = wifi.upload()/1048576         #Megabyte = 1024*1024 Bytes
#                     download_net = wifi.download()/1048576
#                     print("Wifi Upload Speed is", upload_net)
#                     print("Wifi download speed is ",download_net)
#                     speak(f"Wifi download speed is {download_net}")
#                     speak(f"Wifi Upload speed is {upload_net}")
#-----------------------------------------------stop the terminal --------------------------------------------------------------------------------

        elif 'stop' in query:
            speak("welcome sir it's my pleasure ")
            break   
