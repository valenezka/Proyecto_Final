import pygame,sys
from Button import Button

pygame.init()
SCREEN=pygame.display.set_mode((728,447))
pygame.display.set_caption("Menu")
fondo=pygame.image.load(r"imagenes\fondo_meu.jpg")
def get_font(size): 
    return pygame.font.Font("font.ttf", size)

def main_menu():
   
    while True:
        SCREEN.blit(fondo,(0,0))
        menu_mouse_pos=pygame.mouse.get_pos()
        menu_text=get_font(30).render("Cachau",True,(255, 0, 0))
        menu_rect=menu_text.get_rect(center=(350,100))

        easy_button=Button(image=pygame.image.load(r"imagenes\rect (2).jpg"), pos=(350,200),text_input="Easy", font=get_font(15), base_color=(255, 255, 255), hovering_color="White")
    
        hard_button= Button(image=pygame.image.load(r"imagenes\rect (2).jpg"), pos=(350, 300),text_input= "Hard", font=get_font(15), base_color= (255, 255, 255), hovering_color="White")
        quit_button = Button(image=pygame.image.load(r"imagenes\rect (2).jpg"), pos=(350, 400),text_input="QUIT", font=get_font(15), base_color=(255, 255, 255), hovering_color="White")
        SCREEN.blit (menu_text, menu_rect)
        for button in [easy_button, hard_button, quit_button]:
            button.change_color(menu_mouse_pos)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_button.checkforinput(menu_mouse_pos):
                    return True
                if hard_button.checkforinput(menu_mouse_pos):
                    return False
                if quit_button.checkforinput(menu_mouse_pos):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()

