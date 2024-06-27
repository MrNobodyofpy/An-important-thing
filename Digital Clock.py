#Pygame is important
import pygame
import sys
from time import strftime

#Import module
from tkinter import *
from tkinter.ttk import * 

#Running time
pygame.init()

#Set the size of the "window"
width = 600
height = 600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("A digital clock")

#Set name of colors : )
GREY = (120, 120, 120)
WHITE = (255,255,255)
BLACK = (0,0,0)


#Set "is_running" turn on first : )
is_running = True

#Start running the program : )
while is_running:
	screen.fill(GREY)

#Event while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			is_running = False

	pygame.display.flip()
pygame.quit()