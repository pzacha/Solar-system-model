import sqlite3
import pygame


# Animation
pygame.init()
screen = pygame.display.set_mode((screen_size,screen_size))
pygame.display.update()

# Variable for screen refresh frequency
iter = 0 

 # Update screen and reset iter variable

    if iter == 1000:
        pygame.display.update()
        screen.fill((0,0,0))
        iter = 0
    iter = iter + 1

# Update screen every iter iterations
        if iter == 1000:
            if obj == sun:
                pygame.draw.circle(screen, (255,255,0), (norm_coords(sun.xcor),norm_coords(sun.ycor)), 10)
            elif obj == earth:
                pygame.draw.circle(screen, (0,255,0), (norm_coords(obj.xcor),norm_coords(obj.ycor)), 4)
            else:
                pygame.draw.circle(screen, (255,255,255), (norm_coords(obj.xcor),norm_coords(obj.ycor)), 3)
                60*60*24*365