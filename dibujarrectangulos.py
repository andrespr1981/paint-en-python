import pygame
from pygame.locals import*

AzulCielo=(63,255,238)
Blanco=(255, 255, 255)
Negro=(0, 0, 0)
Rojo=(255, 0, 0)
Verde=(0, 255, 0)
Azul=(0, 0, 255)

SCREEN_AL=1100
SCREEN_AN=600
SCREEN=pygame.display.set_mode((SCREEN_AL,SCREEN_AN))
SCREEN.fill(Blanco)

def dibujarrectanguloh(c,g,x1,y1):
	if c == 1:
		color=AzulCielo
	if c == 2:
		color=Blanco
	if c == 3:
		color=Negro
	if c == 4:
		color=Rojo
	if c == 5:
		color=Verde
	if c == 6:
		color=Azul
	y2=y1+270#Que tan largo va a ser el rectangulo
	x2=x1
	pygame.draw.line(SCREEN, color, (x1,y1),(x2,y2), g)

def dibujarrectangulov(c,g,x1,y1):
	if c == 1:
		color=AzulCielo
	if c == 2:
		color=Blanco
	if c == 3:
		color=Negro
	if c == 4:
		color=Rojo
	if c == 5:
		color=Verde
	if c == 6:
		color=Azul
	x2=x1+270
	y2=y1
	pygame.draw.line(SCREEN, Verde, (x1,y1),(x2,y2), g)