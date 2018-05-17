import pyautogui as pg
import webbrowser

videos = ["https://www.youtube.com/watch?v=Uth5Vt6bc-M"]

music =["https://www.youtube.com/watch?v=UtVJdPfm0F8"]

answer = pg.prompt(
"""
Wich would you rather do?
a)Watch videos
b)listen to music

"""
   )

if answer == "a":
    for i in videos:
        webbrowser.open(i)

elif answer == "b"
    for i in music:
        webbrowser.open(i)
