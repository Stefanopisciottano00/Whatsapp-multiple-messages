import os
import time
import webbrowser as web
import pyautogui as pg
import keyboard as k
from pywhatkit.core import core

pg.FAILSAFE = False

phone_no = "+393286369063"
message = "ciao"
wait_time = 15,
tab_close = False,
close_time = 3,
core.check_connection()
"""Send WhatsApp Message Instantly"""

web.open("https://web.whatsapp.com")
time.sleep(5)
pg.click(core.WIDTH / 7, core.HEIGHT / 3)

for i in range(301):
    k.write("Zazingra")
    k.press("enter")
