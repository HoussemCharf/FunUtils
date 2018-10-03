from pygame import *

'''
The music must be in the same folder/project to work
You have to install pygame
command: pip install pygame
'''

mixer.init()
msc = input('Song Name: ')
mixer.music.load('{}.mp3'.format(msc))
mixer.music.play()

while mixer.music.get_busy():
    time.Clock().tick(10)
    if input() == 'pause':
        break;