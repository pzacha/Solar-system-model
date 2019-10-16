import numpy as np
import sqlite3
import pygame

import globals



def norm_coords(coord):
    """Adjust coordinates to screen (0,0) = middle of the screen"""
    if coord == 0:
        # Middle of the screen
        coord = globals.screen_size/2
    elif coord >= 0:
        # Right/top side of the screen
        # If absolute distance is bigger than max_dist show the planet on the edge of the screen
        if abs(coord) > globals.max_dist:
            coord = globals.screen_size
        else:
            coord = globals.screen_size/2 + coord/globals.max_dist*globals.screen_size/2
    else:
        # Left/bottom side of the screen
        # If absolute distance is bigger than max_dist show the planet on the edge of the screen
        if abs(coord) > globals.max_dist:
            # If distance is bigger than max_dist show the planet on the edge of the screen
            coord = 0
        else:           
            coord = globals.screen_size/2 - abs(coord)/globals.max_dist*globals.screen_size/2       
    return int(round(coord))

#def display(coords_table):
#    """Display solar system animation"""
    
#    # Animation
#    pygame.init()
#    screen = pygame.display.set_mode((screen_size,screen_size))
#    pygame.display.update()

#    # Variable for screen refresh frequency
#    freq = 0

#    for 
#    # Update screen and reset freq variable
#    if frq == 1000:
#        pygame.display.update()
#        screen.fill((0,0,0))
#        freq = 0
#    frq = freq + 1

#    # Update screen every iter iterations
#    if freq == 1000:
#        if obj == sun:
#            pygame.draw.circle(screen, (255,255,0), (norm_coords(sun.xcor),norm_coords(sun.ycor)), 10)
#        elif obj == earth:
#            pygame.draw.circle(screen, (0,255,0), (norm_coords(obj.xcor),norm_coords(obj.ycor)), 4)
#        else:
#            pygame.draw.circle(screen, (255,255,255), (norm_coords(obj.xcor),norm_coords(obj.ycor)), 3)