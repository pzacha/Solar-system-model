import numpy as np
import pygame
import globals
import SQL_db

def norm_coords_x(xcor):
    """Adjust x axis coordinates to screen. 0 = middle of the screen"""
    if xcor == 0:
        # Middle of the screen
        xcor = globals.screen_size_x/2
    elif xcor >= 0:
        # Right side of the screen
        xcor = globals.screen_size_x/2 + xcor/globals.max_dist*globals.screen_size_x/2
    else:
        # Left side of the screen
        xcor = globals.screen_size_x/2 - abs(xcor)/globals.max_dist*globals.screen_size_x/2
    return int(round(xcor))

def norm_coords_y(ycor):
    """Adjust y axis coordinates to screen. 0 = middle of the screen"""
    if ycor == 0:
        # Middle of the screen
        ycor = globals.screen_size_y/2
    elif ycor >= 0:
        # Right side of the screen
        ycor = globals.screen_size_y/2 + ycor/globals.max_dist*globals.screen_size_y/2
    else:
        # Left side of the screen
        ycor = globals.screen_size_y/2 - abs(ycor)/globals.max_dist*globals.screen_size_y/2
    return int(round(ycor))

def display(anim_speed):
    """Display solar system animation"""
    
    # animation
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
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
            for num in range(globals.rand_mass_num + 9):
                # Make the sun yellow and big
                if num == 0:
                    pygame.draw.circle(screen, (255,255,0), (norm_coords_x(coords_table[i + globals.iter_num * 2 * num]), norm_coords_y(coords_table[i + globals.iter_num + globals.iter_num * 2 * num])), 7)
                elif num == 1:
                    pygame.draw.circle(screen, (255,255,255), (norm_coords_x(coords_table[i + globals.iter_num * 2 * num]), norm_coords_y(coords_table[i + globals.iter_num + globals.iter_num * 2 * num])), 1)
                elif num == 2:
                    pygame.draw.circle(screen, (255,255,255), (norm_coords_x(coords_table[i + globals.iter_num * 2 * num]), norm_coords_y(coords_table[i + globals.iter_num + globals.iter_num * 2 * num])), 2)
                elif num == 3:
                    pygame.draw.circle(screen, (255,255,255), (norm_coords_x(coords_table[i + globals.iter_num * 2 * num]), norm_coords_y(coords_table[i + globals.iter_num + globals.iter_num * 2 * num])), 2)
                elif num == 4:
                    pygame.draw.circle(screen, (255,255,255), (norm_coords_x(coords_table[i + globals.iter_num * 2 * num]), norm_coords_y(coords_table[i + globals.iter_num + globals.iter_num * 2 * num])), 1)
                elif num == 5:
                    pygame.draw.circle(screen, (255,255,255), (norm_coords_x(coords_table[i + globals.iter_num * 2 * num]), norm_coords_y(coords_table[i + globals.iter_num + globals.iter_num * 2 * num])), 5)
                elif num == 6:
                    pygame.draw.circle(screen, (255,255,255), (norm_coords_x(coords_table[i + globals.iter_num * 2 * num]), norm_coords_y(coords_table[i + globals.iter_num + globals.iter_num * 2 * num])), 4)
                elif num == 7:
                    pygame.draw.circle(screen, (255,255,255), (norm_coords_x(coords_table[i + globals.iter_num * 2 * num]), norm_coords_y(coords_table[i + globals.iter_num + globals.iter_num * 2 * num])), 4)
                elif num == 8:
                    pygame.draw.circle(screen, (255,255,255), (norm_coords_x(coords_table[i + globals.iter_num * 2 * num]), norm_coords_y(coords_table[i + globals.iter_num + globals.iter_num * 2 * num])), 3)
                else:
                    pygame.draw.circle(screen, (255,255,255), (norm_coords_x(coords_table[i + globals.iter_num * 2 * num]), norm_coords_y(coords_table[i + globals.iter_num + globals.iter_num * 2 * num])), 1)
               
        # Below code is added in order to prevent pygame crash
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                exit(0)
    pygame.display.quit()
    pygame.QUIT