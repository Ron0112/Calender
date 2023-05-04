from datetime import datetime
from time import sleep
from pygame import mixer

mixer.init()
mixer.music.load(r"Clock alarm.mp3")

while 1:
    now = datetime.now()
    hour = int(now.strftime("%I"))
    minute = int(now.strftime("%M"))
    second = int(now.strftime("%S"))
    
    if minute == 0 and second == 0:        
        mixer.music.play(abs(hour - 1))
        
    if minute == 30 and second == 0:
        mixer.music.play(1)

    sleep(1)