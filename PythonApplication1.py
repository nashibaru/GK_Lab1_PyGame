from ctypes.wintypes import RECT
import pygame
import numpy as np

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("First Game")

def bend_surface(surface, px_back):
    
    s_width, s_height = surface.get_size()
    sur = pygame.Surface((s_width, s_height))
    sur.fill((0,0,0))
    for y in range(s_height):
        for x in range(s_width):
            # Calculate the new coordinates based on the bending angle
            new_x = x - int(px_back)
            color = surface.get_at((x, y))
            sur.set_at((new_x, y), color)
        if y % 3 == 0:
            px_back = px_back - 1
    return sur


# deklarowanie kolorów
CZERWONY = (255, 0, 0)
ZIELONY = (0, 255, 0)
ZOLTY = (255, 255, 0)
FIOLETOWY = (128, 0, 128)
JASNY_NIEBIESKI = (0, 255, 255)
POMARANCZOWY = (255, 165, 0)
NIEBIESKI = (0, 0, 255)
SZARY = (128, 128, 128)

tab = [(375, 429.9),
           (429.9, 375),
           (450, 300),
           (429.9, 225),
           (375, 170.1),
           (300, 150),
           (225, 170.1),
           (170.1, 225),
           (150, 300),
           (170.1, 375),
           (225, 429.1),
           (300, 450)]

pygame.draw.polygon(win, ZIELONY, tab, 0)    

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_1]:
        win.fill((0,0,0))
        s = pygame.Surface((600, 600))
        s.fill((0,0,0))
        pygame.draw.polygon(s, ZIELONY, tab, 0)
        s = pygame.transform.scale(s, (300, 300))
        win.blit(s, (150, 150))
        pygame.display.flip()
        
    elif keys[pygame.K_2]:
        win.fill((0,0,0))
        s = pygame.Surface((600, 600))
        s.fill((0,0,0))
        pygame.draw.polygon(s, ZIELONY, tab, 0)
        oldCenter = win.blit(s, [0, 0]).center
        s = pygame.transform.rotate(s, 15)
        rotRect = s.get_rect()
        rotRect.center = oldCenter
        win.blit(s, rotRect)
        pygame.display.flip()
        
    elif keys[pygame.K_3]:
        win.fill((0,0,0))
        s = pygame.Surface((600, 600))
        s.fill((0,0,0))
        pygame.draw.polygon(s, ZIELONY, tab, 0)
        oldCenter = win.blit(s, [0, 0]).center
        s = pygame.transform.flip(s, False, True)
        s = pygame.transform.scale(s, (301, 600))
        Rect = s.get_rect()
        Rect.center = oldCenter
        win.blit(s, Rect)
        pygame.display.flip()
        
    elif keys[pygame.K_4]:
        win.fill((0,0,0))
        s = pygame.Surface((600, 600))
        s.fill((0,0,0))
        pygame.draw.polygon(s, ZIELONY, tab, 0)
        s = bend_surface(s, 150)
        Rect = s.get_rect()
        Rect.center = [350, 300]
        win.blit(s, Rect)
        pygame.display.flip()
        
    elif keys[pygame.K_5]:
        win.fill((0,0,0))
        s = pygame.Surface((600, 600))
        s.fill((0,0,0))
        pygame.draw.polygon(s, ZIELONY, tab, 0)
        s = pygame.transform.scale(s, (600, 301))
        Rect = s.get_rect()
        Rect.center = [300, 75]
        win.blit(s, Rect)
        pygame.display.flip()
        
    elif keys[pygame.K_6]:
        win.fill((0,0,0))
        s = pygame.Surface((600, 600))
        s.fill((0,0,0))
        pygame.draw.polygon(s, ZIELONY, tab, 0)
        s = bend_surface(s, 150)
        s = pygame.transform.rotate(s, 90)
        Rect = s.get_rect()
        Rect.center = [300, 250]
        win.blit(s, Rect)
        pygame.display.flip()
        
    elif keys[pygame.K_7]:
        win.fill((0,0,0))
        s = pygame.Surface((600, 600))
        s.fill((0,0,0))
        pygame.draw.polygon(s, ZIELONY, tab, 0)
        oldCenter = win.blit(s, [0, 0]).center
        s = pygame.transform.rotate(s, 180)
        s = pygame.transform.scale(s, (301, 600))
        Rect = s.get_rect()
        Rect.center = oldCenter
        win.blit(s, Rect)
        pygame.display.flip()
        
    elif keys[pygame.K_8]:
        win.fill((0,0,0))
        s = pygame.Surface((600, 600))
        s.fill((0,0,0))
        pygame.draw.polygon(s, ZIELONY, tab, 0)
        s = pygame.transform.rotate(s, 37)
        s = pygame.transform.scale(s, (600, 301))
        Rect = s.get_rect()
        Rect.center = [200, 400]
        win.blit(s, Rect)
        pygame.display.flip()
        
    elif keys[pygame.K_9]:
        win.fill((0,0,0))
        s = pygame.Surface((600, 600))
        s.fill((0,0,0))
        pygame.draw.polygon(s, ZIELONY, tab, 0)
        s = bend_surface(s, 150)
        s = pygame.transform.rotate(s, 225)
        Rect = s.get_rect()
        Rect.center = [370, 350]
        win.blit(s, Rect)
        pygame.display.flip()
        
    elif keys[pygame.K_q]:
        win.fill((0,0,0))
        s = pygame.Surface((600, 600))
        s.fill((0,0,0))
        oldCenter = win.blit(s, [0, 0]).center
        pygame.draw.rect(s, CZERWONY, [(290, 88.5), (20, 423)], 0)
        s = pygame.transform.rotate(s, -45)
        pygame.draw.rect(s, CZERWONY, [(278.5, 267), (300, 20)], 0)
        pygame.draw.rect(s, CZERWONY, [(270, 560), (300, 20)], 0)
        Rect = s.get_rect()
        Rect.center = oldCenter
        win.blit(s, Rect)
        pygame.display.flip()
        
    elif keys[pygame.K_0]:
        pygame.quit()
        pygame.init()
        win = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("First Game")
        pygame.draw.polygon(win, ZIELONY, tab, 0)
        

    # wypisywanie tekstu
    #font = pygame.font.SysFont('comicsans', 30)
    #label = font.render('dwunastok¹t', 1, (255, 255, 255))
    #win.blit(label, (115, 320))

    pygame.display.update()