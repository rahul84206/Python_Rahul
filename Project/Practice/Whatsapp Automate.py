import pyautogui as pg
import time
time.sleep(5)
for i in range(10):
    pg.write("Hello!")
    time.sleep(0.5)
    pg.press("Enter")
