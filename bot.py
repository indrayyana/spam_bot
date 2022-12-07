import pyautogui as pg
import time

time.sleep(7)

p = "Message"

for i in range(1, 101):
    pg.write(p + ' ' + str(i))
    pg.press('Enter')