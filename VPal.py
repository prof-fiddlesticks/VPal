import pygame
import sys

#RUN WITH py -3.13 C:\Users\ishaa\Desktop\VirtualPet\VPal.py

pygame.init()

HEIGHT = 600
WIDTH = 900

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("VPal")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 48)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((30,30,30))

    def draw_bar(label, x, y, width, height, percent, fill_color):

        bg = pygame.Rect(x, y , width, height)
        pygame.draw.rect(screen, (143, 150, 143), bg)

        fill_width = int(width * percent)
        fill = pygame.Rect(x, y, fill_width, height)
        pygame.draw.rect(screen, (fill_color), fill)

        text = font.render(label, True, (255, 255, 255))
        screen.blit(text, (x, y - 40))
     

    draw_bar("Hunger", 600, 100, 200, 30, 0.3, (222, 152, 53))
    draw_bar("Thirst", 600, 220, 200, 30, 0.4, (52, 121, 217))
    draw_bar("Happy",  600, 340, 200, 30, 0.8, (230, 36, 18))
    draw_bar("Energy", 600, 460, 200, 30, 0.6, (11, 222, 187))


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()


 
