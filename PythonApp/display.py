import numpy as np
import pygame
import globals
import SQL_db

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

def display(anim_speed):
    """Display solar system animation"""
    
    # animation
    pygame.init()
    screen = pygame.display.set_mode((globals.screen_size, globals.screen_size))
    pygame.display.update()

    # variable for screen refresh frequency
    anim_iter = 0

    # Get table wit coords
    coords_table = SQL_db.create_coords_table()

    for i in range(globals.iter_num):
        if anim_iter == anim_speed:
            pygame.display.update()
            screen.fill((0,0,0))
            anim_iter = 0
        # update screen and reset freq variable        
        anim_iter = anim_iter + 1
        # update screen every iter iterations
        if anim_iter == anim_speed:
            for num in range(globals.rand_mass_num + 2):
                # Make the sun yellow and big
                if num == 0:
                    pygame.draw.circle(screen, (255,255,0), (norm_coords(coords_table[i + globals.iter_num * 2 * num]), norm_coords(coords_table[i + globals.iter_num + globals.iter_num * 2 * num])), 6)
                else:
                    pygame.draw.circle(screen, (255,255,255), (norm_coords(coords_table[i + globals.iter_num * 2 * num]), norm_coords(coords_table[i + globals.iter_num + globals.iter_num * 2 * num])), 3)
               
        # Below code is added in order to prevent pygame crash
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                exit(0)
    pygame.display.quit()
    pygame.QUIT