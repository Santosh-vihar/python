import pyautogui as pg
import time
import random
hero = ['some','thing']#enter anything you want
time.sleep(5)
for i in range(20):
    a=random.choice(hero)
    pg.write(f"{i+1}. {a}")
    time.sleep(0.5)
    pg.press('enter')
    
