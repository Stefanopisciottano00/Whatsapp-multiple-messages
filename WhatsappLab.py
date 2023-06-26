import os
import time
import webbrowser as web
import pyautogui as pg
import keyboard as k
from pywhatkit.core import core

pg.FAILSAFE = False

phone_no = "insert phone number of the first chat on whatsapp"
message = "Hi there, i'm using Whatsapp"
N_of_messages = 100
wait_time = 15,
tab_close = False,
close_time = 3,
core.check_connection()
"""Send WhatsApp Message Instantly"""

web.open("https://web.whatsapp.com")
time.sleep(5)

""" click on the first chat to select it """
pg.click(core.WIDTH / 7, core.HEIGHT / 3)

for i in range(N_of_messages):
    k.write(message)
    k.press("enter")
