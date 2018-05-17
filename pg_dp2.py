import pyautogui as pg
import time

pg.hotkey('ctrl','winleft','d')
pg.hotkey('winleft')
pg.typewrite('chrome\n',.3)

pg.hotkey('winleft', 'up')
pg.typewrite('dannydavito\n',.3)
time.sleep(2)

pg.moveTo(48, 217)
pg.click()
