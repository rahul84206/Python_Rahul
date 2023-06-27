import pyautogui as pg
while True:
    a = pg.confirm('Are you a good boy?', buttons=['Yes', 'No', 'Not Sure'])
    if a == 'Yes':
        break
