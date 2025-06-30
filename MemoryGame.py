import sys
import pygame
import datetime
import math
import pygame.freetype
import random
import time

pygame.init()

GAME_FONT = pygame.freetype.Font("Oswald-VariableFont_wght.ttf", 80)

def ZeroField(n):
    return [[0] * n for i in range(n)]



def MemoryRandomizer(cellAmount, map):
    for i in range(cellAmount * 5):
        x = random.randint(0, 9)
        y = random.randint(0, 9)     
        while(map[x][y] != 0):
            x = random.randint(0, 9)
            y = random.randint(0, 9)
        map[x][y] = i
        X = random.randint(0, 9)
        Y = random.randint(0, 9)     
        while(map[X][Y] != 0):
            X = random.randint(0, 9)
            Y = random.randint(0, 9)
        map[X][Y] = i
    return map

def main():
    width = 800
    height = 800
    cellAmount = 10
    cellHeight = height/cellAmount
    cellWidth = width/cellAmount
    xIdx = 0
    yIdx = 0
    selector = False
    selectedX = -1
    selectedY = -1
    selectedx = -1
    selectedy = -1
    cheats = False
    cheatX = -1
    cheatY = -1

    screen = pygame.display.set_mode((width, height))
    running = True
    # map = ZeroField(cellAmount)

    map = MemoryRandomizer(cellAmount, ZeroField(cellAmount))
   

    while running:
        # text_surface, rect = GAME_FONT.render(str(map[0][0]), (255, 0, 0))
        # screen.blit(text_surface, (100, 100))
        pygame.display.flip()
        print(map)
        screen.fill((0, 0, 0))
        for y in range(len(map)):
             for x in range(len(map[y])):
                if(cheats):
                    if(selectedX != -1 and selectedY != -1 and map[x][y] == map[selectedX][selectedY]):
                        pygame.draw.rect(screen, (0, 0, 255), (x * cellHeight, y * cellWidth, cellHeight, cellWidth))
                        pygame.draw.rect(screen, (0, 0, 255), (xIdx * cellHeight, yIdx * cellWidth, cellHeight, cellWidth))
                        
                pygame.draw.rect(screen, (255, 0, 0), (x * cellHeight, y * cellWidth, cellHeight, cellWidth), 1, border_radius = 1)
                
                pygame.draw.rect(screen, (255, 0, 0), (x * cellHeight, y * cellWidth, cellHeight, cellWidth), 1, border_radius = 1)

                if(map[x][y] == -1):
                    pygame.draw.rect(screen, (0, 255, 0), (x * cellHeight, y * cellWidth, cellHeight, cellWidth))
                if((x == selectedX and y == selectedY) or (x == selectedx and y == selectedy) or cheats == True):
                    if(map[x][y] <= 9):
                        text_surface, rect = GAME_FONT.render(str(map[x][y]), (255, 0, 0))
                        screen.blit(text_surface, (x * cellHeight + 22.5, y * cellWidth + 5))
                    else:
                        text_surface, rect = GAME_FONT.render(str(map[x][y]), (255, 0, 0))
                        screen.blit(text_surface, (x * cellHeight + 5, y * cellWidth + 5))
                
            


        pygame.draw.rect(screen, (255, 255, 255), (xIdx * cellHeight, yIdx * cellWidth, cellHeight, cellWidth), 1, border_radius = 5)

        for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    running = False
                if events.type == pygame.KEYDOWN:
                    if events.key == pygame.K_SPACE:
                        if(selector):  
                            if(map[xIdx][yIdx] == map[selectedX][selectedY] and (xIdx != selectedX or yIdx != selectedY)):
                                map[selectedX][selectedY] = -1
                                map[xIdx][yIdx] = -1
                            selectedx = xIdx
                            selectedy = yIdx
                            selector = False
                        else:
                            if(map[xIdx][yIdx] != -1):
                                selector = True
                                selectedX = xIdx
                                selectedY = yIdx

                    elif events.key == pygame.K_LEFT:
                        xIdx -= 1
                        if(selectedx != -1 and selectedy != - 1):
                            selectedX = -1
                            selectedY = -1
                            selectedx = -1
                            selectedY = -1
                    elif events.key == pygame.K_RIGHT:
                        xIdx += 1
                        if(selectedx != -1 and selectedy != - 1):
                            selectedX = -1
                            selectedY = -1
                            selectedx = -1
                            selectedY = -1
                    elif events.key == pygame.K_UP:
                        yIdx -= 1
                        if(selectedx != -1 and selectedy != - 1):
                            selectedX = -1
                            selectedY = -1
                            selectedx = -1
                            selectedY = -1
                    elif events.key == pygame.K_DOWN:
                        yIdx += 1
                        if(selectedx != -1 and selectedy != - 1):
                            selectedX = -1
                            selectedY = -1
                            selectedx = -1
                            selectedY = -1
                    elif events.key == pygame.K_7:
                        if(cheats):
                            cheats = False
                        else:
                            cheats = True


main()