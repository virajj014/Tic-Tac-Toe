
import pygame
 
pygame.init()
 
white = (255, 255, 255)
black = (0,0,0)
green = (0, 255, 0)
blue = (0, 0, 128)
 
# assigning values to width and Y variable
width = 600
height = 600
 
# create the display surface object
# of specific dimension..e(width, Y).
display_surface = pygame.display.set_mode((width, height))
 
# set the pygame window name
pygame.display.set_caption('Tic Tac Toe')
font = pygame.font.Font(None, 60)
text = font.render('Game Over !!', True,black,white)
textRect = text.get_rect()
textRect.center = (width // 2, height // 2)
 
# infinite loop
while True:
 
    # completely fill the surface object
    # with white color
    display_surface.fill(white)
 
    # copying the text surface object
    # to the display surface object
    # at the center coordinate.
    display_surface.blit(text, textRect)
 
    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for event in pygame.event.get():
 
        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update() 
