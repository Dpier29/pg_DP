import pyautogui as pg
import time
pg.click(1098, 36)
pg.typewrite('https://accounts.google.com/ServiceLogin/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin\n')
time.sleep (4)
pg.typewrite('daross@gcds.net\n',.2)
time.sleep (4)
pg.typewrite(pg.password(text='', title='', default='', mask='*')+'\n')
