import bluedot
import os

bd = bluedot.BlueDot()
bd.wait_for_press()

os.system("sudo shutdown -h now")
