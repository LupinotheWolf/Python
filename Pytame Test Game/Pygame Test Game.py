import pygame
import time
import random

# Initial Declarations
clock = pygame.time.Clock()
pygame.font.init()
pygame.init()
game_exit = False
game_over = False
FPS = 60
for event in pygame.event.get():
    if event.type == pygame.QUIT:# if you press closewindow
        game_exit = True

# Define Colours
white = (255, 255, 255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)


# Set window size and displays it
display_width = 800
display_height = 600
display = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Adventure Game')
pygame.display.flip()


# Definiton of basic Functions
def message_to_screen(msg,color):
    screen_text = font.render(msg, True, color)
    display.blit(screen_text, [display_width / 2, display_height / 2])

# Game Over
while game_over == True:
    game_display.fill(white)
    message_to_screen("YOU DIED", red)
    pygame.display.update()


# Sets font and text
font = pygame.font.SysFont(None, 25, bold=False, italic=False)

def starting():
    basicfont = pygame.font.SysFont(None, 36)
    text = basicfont.render('Starting...', True, white, red)
    textrect = text.get_rect()
    textrect.centerx = display.get_rect().centerx
    textrect.centery = display.get_rect().centery
    display.fill(white)
    display.blit(text, textrect)

starting()




# Main Loop!!!
while not game_exit:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True
    display.fill(white)
    pygame.draw.line(display, black, [0, 0], [300, 600], 30)
    pygame.draw.circle(display, black, [50, 50], 30, 5)
    pygame.draw.rect(b, green, (10, 10, 10, 10), width = 0)

    # update display
    pygame.display.flip()





# Functions to quit game
pygame.quit()
quit()
