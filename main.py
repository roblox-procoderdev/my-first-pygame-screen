import pygame
pygame.init()
screen_width,screen_height=500,500
display_surface=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("My first game screen!")
bgimg=pygame.transform.scale(pygame.image.load('rice.jpg').convert(),(300,300))
bgimg_rect=bgimg.get_rect(center=(screen_width//2,screen_height//2+40))
running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    display_surface.blit(bgimg,bgimg_rect)
pygame.display.flip()
pygame.quit()