#Paint en python 
import pygame
from pygame.locals import*
from listarcolores import listarcolores
from dibujarlinea import dibujarlinea
from dibujarcuadrado import hacercuadrado
from dibujarrectangulos import dibujarrectanguloh
from dibujarrectangulos import dibujarrectangulov
from help import help
from fondo import pantalla

#Colores
AzulCielo=(63,255,238)
Blanco=(255, 255, 255)
Negro=(0, 0, 0)
Rojo=(255, 0, 0)
Verde=(0, 255, 0)
Azul=(0, 0, 255)

#Pantalla
SCREEN_AL=1100
SCREEN_AN=600
SCREEN=pygame.display.set_mode((SCREEN_AL,SCREEN_AN))
SCREEN.fill(Blanco)

#Nombre del programa
pygame.display.set_caption('Paint')
print("Para recibir ayuda usa /help")
def comandos(comando):
    comandos = comando.strip().split()
    if comandos[0] == "/help":
    	help()
    elif comandos[0] == "comando":
        if comandos[1] == "-linea":
            c, g, x1, x2, y1, y2 = map(int, comandos[2:])
            dibujarlinea(c,g,x1,x2,y1,y2)
        elif comandos[1] == "-triangulo":
            c, g, x1, y1= map(int, comandos[2:])
            #hacertriangulo(c,g,x1,y1)
        elif comandos[1] == "-rectanguloh":
            c, g, x1, y1 = map(int, comandos[2:])
            dibujarrectanguloh(c,g,x1,y1)
        elif comandos[1] == "-rectangulov":
            c, g, x, y = map(int, comandos[2:])
            dibujarrectangulov(c,g,x,y)
        elif comandos[1] == "-cuadrado":
        	c, g, x1, y1= map(int, comandos[2:])
        	hacercuadrado(c,g,x1,y1)
        elif comandos[1] == "-colores":
        	listarcolores()
        elif comandos[1] == "-fondo":
        	c, = map(int, comandos[2:])
        	pantalla(c)


myfile = open("comandos.cmd", "r")
for cmd in myfile:
    cmd = cmd.strip()
    comandos(cmd)
    print(f"-{cmd}-")
myfile.close()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
    pygame.display.update()
    pygame.display.flip()
