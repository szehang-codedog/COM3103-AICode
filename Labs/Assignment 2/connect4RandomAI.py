import numpy as np
import pygame
import sys
import math
import random


###########################################
#  GUI Related Functions(You may skip over)
###########################################
BLUE = (0,183,235)
BLACK = (50,50,50)
RED = (255,0,0)
YELLOW = (255,255,0)


ROW_COUNT = 6
COLUMN_COUNT = 7

def init_gui_setting():
    global size, screen, myfont, SQUARESIZE, RADIUS, width, height
    pygame.init()
    SQUARESIZE = 100
    width = COLUMN_COUNT * SQUARESIZE
    height = (ROW_COUNT+1) * SQUARESIZE
    size = (width, height)
    RADIUS = int(SQUARESIZE/2 - 5)
    screen = pygame.display.set_mode(size)
    pygame.display.update()
    myfont = pygame.font.SysFont("monospace", 65)

def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
    
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):      
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
            elif board[r][c] == 2: 
                pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
    pygame.display.update()

def print_board(board):
    if SHOW_TEXT_BOARD:
        print(np.flip(board, 0))

############## 
#  Game Logic 
##############
   
def create_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board

#Drop a piece on a column, and update the matrix
def drop_piece(board, row, col, turn):
    board[row][col] = turn

#Return True if the selected column is not full
def is_valid_location(board, col):    
    return board[ROW_COUNT-1][col] == 0

#Return True all positions have been filled (i.e., end of game)
def no_more_moves(board):
    return np.count_nonzero(board) == COLUMN_COUNT * ROW_COUNT

#Place a piece into a column and update the game matrix 
def do_move(board, col, turn):
    for row in range(ROW_COUNT):
        if board[row][col] == 0:
            board[row][col] = turn
            break
        
                           
       

#################################################### 
#  Code for handling Human Player's move
#    It returns the column mouse-selected by the user
####################################################  

def player_move(board, turn):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
                posx = event.pos[0]
                if turn == 1:
                    pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
                else: 
                    pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
                    
            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
                             
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))
                if is_valid_location(board, col):
                     return col

#############################################
# Functions for checking if one side has won
#############################################
#  Return the longest continous sequence of a player's pieces in a line
#    (if length of line is less than 4, it always return zero)   
#
#  E.g., check_line([ 0, 1, 1, 1, 0, 1, 1], 1) woukd return 3
#
def check_line(line, turn):
    count=0
    max_count=0
    if len(line) <4:
        return 0
    
    for x in line:
        if x==turn:
            count+=1
            if count >= max_count:
                max_count=count
        else:
            count=0
    return max_count       

#
# Check if either side is won by checking each row, columm and diagonal in turn.
# If the player has >= 4 consecutive pieces, it has won.
#
def win(board, turn):
    # Check eack column for win 
    for c in range(COLUMN_COUNT):
        col = board[:,c]
        if check_line(col, turn) >=4:            
            return True

    # Check eack row for win 
    for r in range(ROW_COUNT):
        row = board[r,:]
        if check_line(row, turn) >=4:            
            return True

    # Check diaganols  [\\]
    for d in range(-4,4):
        diag = board.diagonal(d)
        if check_line(diag, turn) >=4:            
            return True
        
    # Check opposite diagonals [//]
    for d in range(-4,4):
        diag = np.flip(board,1).diagonal(d)
        if check_line(diag, turn) >=4:            
            return True
        
###########################################
#   AI FUNCTIONS
###########################################

####################
## Scoring Functions
####################

#
#  Define the score function as the sum of 
#   the longest consecutive sequence of each players in all cols, rows and diagonals
#  The score is +ve for player1 and -ve for player2
#  
def score(board):

    score=0
    # Check score of each column 
    for c in range(COLUMN_COUNT):
        col = board[:,c]
        pass
        ## ADD YOUR CODE HERE
        
    # Check score of each row
    for r in range(ROW_COUNT):
        row = board[r,:]
        pass
        ## ADD YOUR CODE HERE
        
    # Check diagonols scores  [\\]
    for d in range(-4,4):
        diag = board.diagonal(d)
        pass
        ## ADD YOUR CODE HERE
                   
        
    # Check opposite diagonals scores [//]
    for d in range(-4,4):
        diag = np.flip(board,1).diagonal(d)
        pass
        ## ADD YOUR CODE HERE
                
    return score
    
       
def list_moves(board, turn):
    children=[]
    for col in range(0,COLUMN_COUNT):
        if is_valid_location(board, col):
                children.append(col)
    return children    


def max_value(board, level):
    pass
    ## ADD YOUR CODE HERE
            
def min_value(board, level):
    pass
    ## ADD YOUR CODE HERE

def computer_move_minimax(board, turn):
    pass
    ## ADD YOUR CODE HERE
                        
def computer_move_random(board, turn):
    done = False
    while not done:
        col = random.randint(0, COLUMN_COUNT-1)
        if is_valid_location(board, col):
            done=True
    return col


def play_game():  
    board = create_board()
    print_board(board)
    draw_board(board)
    game_over = False
    turn = 1

    while not game_over:
        if no_more_moves(board):
            game_over = True
            break;
        
        if (turn==1 and player1=="human") or (turn==2 and player2=="human"):
            col= player_move(board, turn)
        else:
            col= computer_move_random(board, turn)
            #col= computer_move_minimax(board, turn)
            #CHANGE IT TO  computer_move_minimax(board, turn) WHEN YOU ARE READY

        do_move(board, col, turn)
        
        if win(board, turn):
            label = myfont.render("Player {} wins!!".format(turn), 1, BLUE)
            screen.blit(label, (40,10))
            game_over = True

                
        print_board(board)
        draw_board(board)
        if turn ==1:
            turn = 2
        else:
            turn=1
                                
    if game_over:
         pygame.time.wait(5000)

########################
#  Main
########################

player1="computer"
#player1="human"
player2="human"
#player2="computer"

SHOW_TEXT_BOARD=False

MAX_PLY = 5

init_gui_setting()
play_game()
pygame.quit()
sys.exit()
