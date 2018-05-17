import win32com.client as wincl
import pyautogui as pg
import webbrowser as web

speak = wincl.Dispatch("SAPI.SpVoice")

speak.Speak("What is your name big guy")
answer = pg.prompt("Enter your name")

speak.Speak("Hello" + answer + "." + "Nice to meet you.")

speak.Speak("What is your favorite color")
color = pg.prompt("Enter in your favorite color.")

if color == "Blue":
    speak.Speak("Blue is terrible and I hate you and you are not big man anymo")

speak.Speak("What video would you like to watch?")
video = pg.prompt("Enter video here")
wb.open("https://www.youtube.com/results?search_query=" + video)





