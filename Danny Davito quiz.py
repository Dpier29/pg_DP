import pyautogui as pg
import time
import webbrowser

points = 0

# Question 1

answer=pg.prompt (
"""
Wich would you rather do?

a)eat a bag of flower
b)not were cloths
c)fall out of a window

"""
   )

# Give points

if answer == "a":
    points +=1
elif answer == "b":
    points +=1
elif answer == "c":
    points +=5  
# Question 2

answer=pg.prompt (
"""
How tall would You like to be

a)4,10
b)6,9
c)3,10

"""
   )

# Give points

if answer == "a":
    points +=4
elif answer == "b":
    points +=1
elif answer == "c":
    points +=2  

# Question 3

answer=pg.prompt (
"""
How many times a day do you ask people if they want to eat you

a)6
b)0
c)over 20 times

"""
   )

# Give points

if answer == "a":
    points +=3
elif answer == "b":
    points +=0
elif answer == "c":
    points +=5 

# Question 3

answer=pg.prompt (
"""
How old are you

a)13
b)14
c)over 70

"""
   )

# Give points

if answer == "a":
    points +=0
elif answer == "b":
    points +=0
elif answer == "c":
    points +=5

# END OF SURVEY

if points <=3:
    pg.alert("you are not danny davito")

if points <=6:
    pg.alert("you are not danny davito but you were close")
    webbrowser.open("http://www.telegraph.co.uk/content/dam/comedy/2015-08/21Aug/dannydevito.jpg?imwidth=450")

if points >=8:
    pg.alert("you are danny davito")
    webbrowser.open ("https://www.youtube.com/watch?v=O6K0ZPRqzFU")
