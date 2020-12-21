import pygame
import time
import random

pygame.init()
FPS = 30
clock = pygame.time.Clock()#sets clock so you can create FPS

#define colours
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

#Set window size
display_width = 800
display_height = 600

game_display = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Test Game')


# flipbook by using frames - updates entire surface
# pygame.display.flip()


#sets exiting game to false for normal play


font = pygame.font.SysFont(None, 25) #number is font size
def message_to_screen(msg,color):
    screen_text = font.render(msg, True, color)
    game_display.blit(screen_text, [display_width / 2, display_height / 2]) #where the message shows


def snake(block_size, snakelist):
    for XnY in snakelist:
        pygame.draw.rect(game_display, black, [XnY[0],XnY[1],block_size,block_size]) #draws the snake

block_size = 10

"""
MAIN LOOP
"""
def gameLoop():#calls main loop
    gameExit = False
    gameOver = False

    #lead is leader of blocks in snake
    lead_x = display_width / 2
    lead_y = display_height / 2
    lead_x_change = 0
    lead_y_change = 0
    snakelist = []
    snakelength = 1
    AppleThickness = 30

    #round dimensions of random apple to the nearest 10
    randAppleX = round(random.randrange(0, display_width - block_size) / 10.0) * 10.0
    randAppleY = round(random.randrange(0, display_height - block_size) / 10.0) * 10.0

    while not gameExit:

        while gameOver == True:
            game_display.fill(white)
            message_to_screen("You lose... WHITE BOY.. press c to play again or q to quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False#make sure to set to false to break loop
                    if event.key == pygame.K_c:
                        gameLoop()#makes gameloop run again


        for event in pygame.event.get():#event handling loop
            if event.type == pygame.QUIT:#if you press closewindow
                gameExit = True
            if event.type == pygame.KEYDOWN:#if keydown is pressed
                if event.key == pygame.K_LEFT:#goes left
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:#goes right
                    lead_x_change = block_size
                    lead_y_change = 0

                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0

    #if you hit the edge of the screen
        if lead_x >= display_width or lead_x <= 0 or lead_y >= display_height or lead_y <= 0:
            gameOver = True

        #rendering/drawing block
        lead_x += lead_x_change#adds change in x to current state of x
        lead_y += lead_y_change
        game_display.fill(white)#fills the screen with white
        pygame.draw.rect(game_display, red, [randAppleX, randAppleY, AppleThickness, AppleThickness])#draws the apple


        #lists for the snake
        snakehead = []
        snakehead.append(lead_x)
        snakehead.append(lead_y)
        snakelist.append(snakehead)

        if len(snakelist) > snakelength:
            del snakelist[0]

        for eachsegment in snakelist[:-1]:
            if eachsegment == snakehead:
                gameOver = True


        snake(block_size, snakelist)
        pygame.display.update()#updates the display/window

        #asks if snake is same coordinates as the apple
        # if lead_x == randAppleX and lead_y == randAppleY:
        #     randAppleX = round(random.randrange(0, display_width - block_size) / 10.0) * 10.0
        #     randAppleY = round(random.randrange(0, display_height - block_size) / 10.0) * 10.0
        #     snakelength += 1

        if lead_x >= randAppleX and lead_x <= randAppleX + AppleThickness:
            if lead_y >= randAppleY and lead_y <= randAppleY + AppleThickness:
                randAppleX = round(random.randrange(0, display_width - block_size) / 10.0) * 10.0
                randAppleY = round(random.randrange(0, display_height - block_size) / 10.0) * 10.0
                snakelength += 1





        clock.tick(FPS)#sets FPS for events


    #quits game
    pygame.quit()
    quit()
gameLoop()


# NOTES
#
# v this event makes it so the block moves as long as you have it pressed v
#
#         if event.type == pygame.KEYUP:
#             if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
#                 lead_x_change = 0
#
#
# message_to_screen("YOU DIED", red)
# pygame.display.update() # updates the screen again
# time.sleep(2) # forces the system to wait for set seconds
