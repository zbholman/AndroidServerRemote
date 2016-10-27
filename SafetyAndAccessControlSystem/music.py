#Shivang Patel
#10/12/2016
#IST 440W
#PENNSTATE ABINGTON
#Prof Joe Oakes
#python code for playing sound/music.

import pygame
pygame.mixer.init() #initialize the mixer module

#Load a music file forever.mp3 for playback
pygame.mixer.music.load("Forever.mp3")

#Start the playback of the music stream
pygame.mixer.music.play()
