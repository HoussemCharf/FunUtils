# C0de by H taken from Annie Assistant code
# Importing needed libs
from datetime import datetime
from threading import Timer
import os
import time
# fetching todays date
x=datetime.today() 
# defining tomorrow date
y=x.replace(day=x.day+1,hour=7,minute=0,second=0,microsecond=0)
# calculating remaining time
delta_t=y-x
# converting remaining time in seconds for the tread
secs =delta_t.seconds+1
# morning wake up ritual lol
def morning():
	# executing local player
	os.system("omxplayer -o local test.mp3")
	time.sleep(16)
	os.system("omxplayer -o local rooster.mp3")
	os.system("omxplayer -o local ispy.mp3") 
# creating thread and impelmenting ritual
t = Timer(secs,morning) 
t.start()
