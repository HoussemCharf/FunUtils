# Pi Power Off

Turn off your Pi with a button.

## Installation on the Pi

On the Pi install
[bluedot](https://bluedot.readthedocs.io/en/latest/gettingstarted.html) and
dbus.

    $ sudo pip3 install bluedot
	$ sudo apt install python3-dbus
	
Copy the file `bluedot_handler.py` into the desired place

    $ cp bluedot_handler.py ~/bin/

Create a cronjob that starts the handler on reboot of the Pi.

    $ crontab -e -u pi
	
Add the following line, save and restart.
	
	@reboot /usr/bin/python3 /home/pi/bin/bluedot_handler.py

Pair your phone as described
[here](https://bluedot.readthedocs.io/en/latest/pairpiandroid.html)


## Installation on your android smartphone

Install the
[Bluedot Android App](https://bluedot.readthedocs.io/en/latest/bluedotandroidapp.html). 
When your start the app and connect to your device, the blue button
will shut down the pi.
