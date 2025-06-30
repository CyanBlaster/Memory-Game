import sys
import pygame
import datetime
import math
import pygame.freetype
import random

pygame.init()

GAME_FONT = pygame.freetype.Font("Oswald-VariableFont_wght.ttf", 80)

def ZeroField(n):
    return [[0] * n for i in range(n)]

def main():
    width = 800
    height = 800
    cellAmount = 10
    cellHeight = height/cellAmount
    cellWidth = width/cellAmount
    xIdx = 0
    yIdx = 0

    screen = pygame.display.set_mode((width, height))
    running = True
    map = ZeroField(cellAmount)

    map[9][0] = 1
    map[7][2] = 1
   

    while running:
        # text_surface, rect = GAME_FONT.render(str(map[0][0]), (255, 0, 0))
        # screen.blit(text_surface, (100, 100))
        pygame.display.flip()
        print(map)
        for y in range(len(map)):
             for x in range(len(map[y])):
                pygame.draw.rect(screen, (255, 0, 0), (x * cellHeight, y * cellWidth, cellHeight, cellWidth), 1, border_radius = 1)
                
                pygame.draw.rect(screen, (255, 0, 0), (x * cellHeight, y * cellWidth, cellHeight, cellWidth), 1, border_radius = 1)
                text_surface, rect = GAME_FONT.render(str(map[x][y]), (255, 0, 0))
                screen.blit(text_surface, (x * cellHeight + 22.5, y * cellWidth + 5))
        
        pygame.draw.rect(screen, (255, 255, 255), (xIdx * cellHeight, yIdx * cellWidth, cellHeight, cellWidth), 1, border_radius = 5)

        for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    running = False
                if events.type == pygame.KEYDOWN:
                    if events.key == pygame.K_SPACE:
                        print("x")
                    elif events.key == pygame.K_LEFT:
                        xIdx -= 1
                    elif events.key == pygame.K_RIGHT:
                        xIdx += 1
                    elif events.key == pygame.K_UP:
                        yIdx -= 1
                    elif events.key == pygame.K_DOWN:
                        yIdx += 1


main()