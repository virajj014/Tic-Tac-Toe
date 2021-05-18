#  ______________________________________________________________________________________________________
# |                                                                                                      |
# |                             PLEASE SUBSCRIBE CODERS HUB ON YOUTUBE                                   |
# |                   https://www.youtube.com/channel/UCtvr7uwDVkNbMDGKUrd-8ug                           |
# |______________________________________________________________________________________________________|


import pygame, sys
import numpy as np

pygame.init()

width = 600
height = 600
linewidth = 15
winninglinewidth = 15
boardrows = 3
boardcolumns = 3
squaresize = 200


backgroundcolor = (28, 170, 156)    #neon red color for window 


linecolor = (120,57,57)     #grey color for lines -|-|-        
                            #                     -|-|-



#for 0 
circleradius = 60
circlewidth = 15
circlecolor = (239, 231, 200)


#for X
crosswidth = 25
crosscolor = (66, 66, 66)
gap = 55


screen = pygame.display.set_mode( (width, height) )
pygame.display.set_caption( 'TIC TAC TOE                      ' )
screen.fill((251,63,63))
board = np.zeros( (boardrows, boardcolumns))



def drawlines():
	pygame.draw.line( screen, linecolor, (0, squaresize), (width, squaresize), linewidth )
	pygame.draw.line( screen, linecolor, (0, 2 * squaresize), (width, 2 * squaresize), linewidth )
	pygame.draw.line( screen, linecolor, (squaresize, 0), (squaresize, height), linewidth )
	pygame.draw.line( screen, linecolor, (2 * squaresize, 0), (2 * squaresize, height), linewidth )

def drawfigure():
	for row in range(boardrows):
		for col in range(boardcolumns):
			if board[row][col] == 1:
				pygame.draw.circle( screen, circlecolor, (int( col * squaresize + squaresize//2 ), int( row * squaresize + squaresize//2 )), circleradius, circlewidth )
			elif board[row][col] == 2:
				pygame.draw.line( screen, crosscolor, (col * squaresize + gap, row * squaresize + squaresize - gap), (col * squaresize + squaresize - gap, row * squaresize + gap), crosswidth )	
				pygame.draw.line( screen, crosscolor, (col * squaresize + gap, row * squaresize + gap), (col * squaresize + squaresize - gap, row * squaresize + squaresize - gap), crosswidth )

def marksquares(row, col, player):
	board[row][col] = player

def availablesquares(row, col):
	return board[row][col] == 0

def boardfull():
	for row in range(boardrows):
		for col in range(boardcolumns):
			if board[row][col] == 0:
				return False
	return True


def winnercheck(player):
	# vertical win check
	for col in range(boardcolumns):
		if board[0][col] == player and board[1][col] == player and board[2][col] == player:
			verticalwinningline(col, player)
			return True

	# horizontal win check
	for row in range(boardrows):
		if board[row][0] == player and board[row][1] == player and board[row][2] == player:
			horizontalwinningline(row, player)
			return True

	# asc diagonal win check
	if board[2][0] == player and board[1][1] == player and board[0][2] == player:
		ascendingdiagonalwin(player)
		return True

	# desc diagonal win chek
	if board[0][0] == player and board[1][1] == player and board[2][2] == player:
		descendingdiagonalwin(player)
		return True

	return False

def verticalwinningline(col, player):
	posX = col * squaresize + squaresize//2

	if player == 1:
		color = circlecolor
	elif player == 2:
		color = crosscolor

	pygame.draw.line( screen, color, (posX, 15), (posX, height - 15), linewidth )

def horizontalwinningline(row, player):
	posY = row * squaresize + squaresize//2

	if player == 1:
		color = circlecolor
	elif player == 2:
		color = crosscolor

	pygame.draw.line( screen, color, (15, posY), (width - 15, posY), winninglinewidth )

def ascendingdiagonalwin(player):
	if player == 1:
		color = circlecolor
	elif player == 2:
		color = crosscolor

	pygame.draw.line( screen, color, (15, height - 15), (width - 15, 15), winninglinewidth )

def descendingdiagonalwin(player):
	if player == 1:
		color = circlecolor
	elif player == 2:
		color = crosscolor

	pygame.draw.line( screen, color, (15, 15), (width - 15, height - 15), winninglinewidth )

def restart():
	screen.fill((251,63,63))
	drawlines()
	for row in range(boardrows):
		for col in range(boardcolumns):
			board[row][col] = 0

drawlines()

player = 1
game_over = False


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

			mouseX = event.pos[0] 
			mouseY = event.pos[1] 

			clickedrow = int(mouseY // squaresize)
			clickedcol = int(mouseX // squaresize)

			if availablesquares( clickedrow, clickedcol ):
				marksquares( clickedrow,clickedcol, player)
				if winnercheck( player ):
					game_over = True
				player = player % 2 + 1

				drawfigure()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_r:
				restart()
				player = 1
				game_over = False
            
			if event.key == pygame.K_q:
				import gameoverdisplay 
	pygame.display.update()


