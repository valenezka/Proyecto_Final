import pygame
import sys
def get_font(size): 
    return pygame.font.Font("font.ttf", size)
def comparacion_puntajes(puntajes):
    pygame.init()
    size = (800, 335)
    screen = pygame.display.set_mode(size) 
    fondo=pygame.image.load(r'imagenes\copaPiston.jpg').convert()
    fondo=pygame.transform.scale(fondo,(800,355))
    puntajes_ordenados=[0,0]
    for cadena in puntajes: 
        
        for numeros in range (len(cadena)): 
            if cadena[numeros]==".":
                if cadena[numeros+1]=="1":
                    puntajes_ordenados[0]=int(float(cadena))
                else:
                    puntajes_ordenados[1]=int(float(cadena))
    print(puntajes_ordenados)
    
    
    while True:
        screen.blit(fondo,(0,0))
        
        
        if puntajes_ordenados[0]>puntajes_ordenados[1]:
            menu_text=get_font(30).render("Gano el jugador 1",True,(255, 0, 0))
        else:
            menu_text=get_font(30).render("Gano el jugador 2",True,(255, 0, 0))

        menu_rect=menu_text.get_rect(center=(370,150))
        
        screen.blit (menu_text, menu_rect)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  
           
        pygame.display.flip()
        
            
