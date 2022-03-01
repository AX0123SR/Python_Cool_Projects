import pygame
from time import sleep
pygame.init()   #Initialising the pygame

#creating a window for the screen
window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

#Initialise the mixer for pygame
pygame.mixer.init()

#Loading the music
pygame.mixer.music.load('scary_classic.mp3')
pygame.mixer.music.play()
sleep(5)

#Loading the second music
pygame.mixer.music.load('scary_ghost.mp3')
pygame.mixer.music.play()
sleep(1)

#image for background with voice
image = pygame.image.load("scr.jpg")
window.blit(image, (0,0))      #block image transfer,,,display the image
pygame.display.update()
sleep(5)


