import pyautogui as pg
import time
time.sleep(1)
for i in range(5):
    pg.write("Hello!")
    time.sleep(0.5)
    pg.press("Enter")
