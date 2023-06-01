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

def dibujarlinea(c,g,x1,x2,y1,y2):
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
	pygame.draw.line(SCREEN, color, (x1,x2),(y1,y2), g)
