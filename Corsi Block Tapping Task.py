
import pygame
import sys
from time import time
from pygame.locals import *
import random
from pygame.compat import unichr_, unicode_

class CorsiGame:
    'Representation of the Corsi Game'
    GameState = None

class BlockGenerator:
    'Generates blocks'

    def __init__(self):
        self._aRange = range(5, (screenSize[0] - 80),
                        80)  # sets the range for the coordinates; always 5 pixels from edge of screen and 5 pixels between blocks.
        self._bRange = range(5, (screenSize[1] - 80),
                        40)  # sets the range for the coordinates; always 5 pixels from edge of screen and 5 pixels between blocks.
        self._blockList = []

    def blockList(self):
        return self._blockList

    def generateBlocks(self):
        for blockNr in range(1, 10):
            x = self.generateXCoordinate()
            y = self.generateYCoordinate()
            block = Block(x, y, blockNr)
            self._aRange.remove(block.get_x())
            self._bRange.remove(block.get_y())
            self._blockList.append(block)

    def generateXCoordinate(self):
        random_number = random.choice(self._aRange)
        return random_number

    def generateYCoordinate(self ):
        random_number = random.choice(self._bRange)
        return random_number


class Block:
    'Representation of a block in the game'

    def __init__(self, x, y, blockNr):
        # Block sizes; width and heigth, you can change them here
        self._width = 75
        self._height = 75
        self._x = x
        self._y = y
        self._blockNr = blockNr
        self._blink = False

    def get_width(self):
        return self._height

    def get_height(self):
        return self._width

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y


##### VARIABLES #####
# Colors
col_white  = (255, 255, 255)
col_black = (0, 0, 0)
col_gray = (220, 245, 249)
col_green = (63, 246, 7)
col_green_dim = (0, 60, 0)


# empty list for storing the blocks to be presented during a trial.
UserInput = []
#empty list for storing the input of the user.
CorrectBlocks = []

backgroundColour = col_gray
screenSize = (1100, 680)

pygame.init()
pygame.display.set_mode(screenSize)
pygame.display.set_caption("Corsi Block Tapping Task")

screen = pygame.display.get_surface()
screen.fill(backgroundColour)

image = pygame.image.load("corsi.png")  # loads the image if it is in the same map as the .py code.

font = pygame.font.Font(None, 80)  # creates font sizes.
font_small = pygame.font.Font(None, 40)
font_xsmall = pygame.font.Font(None, 30)

screen = pygame.display.get_surface()
screen.fill(backgroundColour)

blockList = []

def main():
    #Booleans for passing to the draw function whether a block needs to 'blink'
    blink_1 = False
    blink_2 = False
    blink_3 = False
    blink_4 = False
    blink_5 = False
    blink_6 = False
    blink_7 = False
    blink_8 = False
    blink_9 = False
    on_spot = False
    on_spot_1 = False
    on_spot_2 = False
    on_spot_3 = False
    on_spot_4 = False
    on_spot_5 = False
    on_spot_6 = False
    on_spot_7 = False
    on_spot_8 = False
    on_spot_9 = False
    a_range = range(5, (screenSize[0] - 80), 80)    #sets the range for the coordinates; always 5 pixels from edge of screen and 5 pixels between blocks.
    b_range = range(5, (screenSize[1] - 80), 40)    #sets the range for the coordinates; always 5 pixels from edge of screen and 5 pixels between blocks.
    blocks = range(1,10)
    correct_count = [0,0]
    sequence_length = 2                     #the minimum sequence length is set to two.
    trial_number = 0
    GameState = "welcome"


    while True:
        pygame.display.get_surface().fill(backgroundColour)

        mouse = pygame.mouse.get_pos()      #gets the mouse position(x,y).
        
        #ITC
        for event in pygame.event.get():
            if GameState == "welcome":          #When state is "welcome" the welcome screen is shown.
                if event.type == KEYDOWN and event.key == K_SPACE:
                    GameState = "explanation"
                    
            elif GameState == "explanation":    #When state is "explanation", the experiment will be explained.
                if event.type == KEYDOWN and event.key == K_SPACE:
                    GameState = "draw_stimulus"
    
            elif GameState == "wait_for_response":
                if (blockList[0].get_x()+ blockList[0].get_width() > mouse[0] > blockList[0].get_x() and blockList[0].get_y()+blockList[0].get_height() > mouse[1] > blockList[0].get_y()): #is the mousecursor 'over' the rect area?
                    if event.type == MOUSEBUTTONUP:
                        on_spot_1 = True
                        time_on_1 = time() 
                        UserInput.append(1)  #appends the number for this block to the empty response list so it can be compared with the trial list.
                elif (blockList[1].get_x() + blockList[1].get_width() > mouse[0] > blockList[1].get_x() and blockList[1].get_y() + blockList[1].get_width() > mouse[1] > blockList[1].get_y()):
                    if event.type == MOUSEBUTTONUP:
                        on_spot_2 = True
                        time_on_2 = time() 
                        UserInput.append(2)
                elif (blockList[2].get_x() + blockList[2].get_width() > mouse[0] > blockList[2].get_x() and blockList[2].get_y() + blockList[2].get_width() > mouse[1] > blockList[2].get_y()):
                    if event.type == MOUSEBUTTONUP:
                        on_spot_3 = True
                        time_on_3 = time() 
                        UserInput.append(3)
                elif (blockList[3].get_x() + blockList[3].get_width() > mouse[0] > blockList[3].get_x() and blockList[3].get_y() + blockList[3].get_width() > mouse[1] > blockList[3].get_y()):
                    if event.type == MOUSEBUTTONUP:
                        on_spot_4 = True
                        time_on_4 = time() 
                        UserInput.append(4)
                elif (blockList[4].get_x() + blockList[4].get_width() > mouse[0] > blockList[4].get_x() and blockList[4].get_y() + blockList[4].get_width() > mouse[1] > blockList[4].get_y()):
                    if event.type == MOUSEBUTTONUP:
                        on_spot_5 = True
                        time_on_5 = time()
                        UserInput.append(5)
                elif (blockList[5].get_x() + blockList[5].get_width() > mouse[0] > blockList[5].get_x() and blockList[5].get_y() + blockList[5].get_width() > mouse[1] > blockList[5].get_y()):
                    if event.type == MOUSEBUTTONUP:
                        on_spot_6 = True
                        time_on_6 = time() 
                        UserInput.append(6)
                elif (blockList[6].get_x() + blockList[6].get_width() > mouse[0] > blockList[6].get_x() and blockList[6].get_y() + blockList[6].get_width() > mouse[1] > blockList[6].get_y()):
                    if event.type == MOUSEBUTTONUP:
                        on_spot_7 = True
                        time_on_7 = time() 
                        UserInput.append(7)
                elif (blockList[7].get_x() + blockList[7].get_width() > mouse[0] > blockList[7].get_x() and blockList[7].get_y() + blockList[7].get_width() > mouse[1] > blockList[7].get_y()):
                    if event.type == MOUSEBUTTONUP:
                        on_spot_8 = True
                        time_on_8 = time() 
                        UserInput.append(8)
                elif (blockList[8].get_x() + blockList[8].get_width() > mouse[0] > blockList[8].get_x() and blockList[8].get_y() + blockList[8].get_width() > mouse[1] > blockList[8].get_y()):
                    if event.type == MOUSEBUTTONUP:
                        on_spot_9 = True
                        time_on_9 = time() 
                        UserInput.append(9)
                if event.type ==  KEYDOWN and event.key == K_SPACE:
                    this_correctness = (CorrectBlocks == UserInput)
                    if this_correctness == True:
                        correct_count.append(1)
                    else:
                        correct_count.append(2)
                    time_when_feedback = time()
                    GameState = "feedback"
            
            elif GameState == "stop":           #When state is "stop" the result is shown.
                if (500+100 > mouse[0] > 500 and 400+50 > mouse[1] > 400):   #Is the mouse on the button spot?
                    on_spot = True
                    if event.type == MOUSEBUTTONUP:   #If button is pressed start the test again.
                        on_spot = False
                        GameState = "draw_stimulus"
                else:
                    on_spot = False
            if event.type == QUIT:
                GameState = "quit"
        
        
        #ATC
        if GameState == "draw_stimulus":      #The nine blocks positions are generated.
            blockList = generateBlockPositions()
            blockGeneration(sequence_length, blocks)
            time_ready = time()
            GameState = "ready"
        
        elif GameState == "ready":              #'ready?' is shown on screen.
            if time() - time_ready > 1:
                time_show_blocks = time()
                GameState = "show_blocks"
        
        elif GameState == "show_blocks":        #The nine blocks are shown on screen.
            if time() - time_show_blocks > 0.5:
                time_block_1 = time()
                GameState = "block_1"
                
        elif GameState == "block_1":
            if 1 in CorrectBlocks:
                blink_1 = True
                if time() - time_block_1 > 1:
                    blink_1 = False
                    GameState = "block_2"
                    time_block_2 = time()
            else:
                if time() - time_show_blocks > 0.01:
                    time_block_2 = time()
                    GameState = "block_2"
        
        elif GameState == "block_2":
            if 2 in CorrectBlocks:
                blink_2 = True
                if time() - time_block_2 > 1:
                    blink_2 = False
                    time_block_3 = time()
                    GameState = "block_3"
            else:
                if time() - time_block_2 > 0.01:
                    time_block_3 = time()
                    GameState = "block_3"
        
        elif GameState == "block_3":
            if 3 in CorrectBlocks:
                blink_3 = True
                if time() - time_block_3 > 1:
                    blink_3 = False
                    time_block_4 = time()
                    GameState = "block_4"
            else:
                if time() - time_block_3 > 0.01:
                    time_block_4 = time()
                    GameState = "block_4"
        
        elif GameState == "block_4":
            if 4 in CorrectBlocks:
                blink_4 = True
                if time() - time_block_4 > 1:
                    blink_4 = False
                    time_block_5 = time()
                    GameState = "block_5"
            else:
                if time() - time_block_4 > 0.01:
                    time_block_5 = time()
                    GameState = "block_5"
        
        elif GameState == "block_5":
            if 5 in CorrectBlocks:
                blink_5 = True
                if time() - time_block_5 > 1:
                    blink_5 = False
                    GameState = "block_6"
                    time_block_6 = time()
            else:
                if time() - time_block_5 > 0.01:
                    time_block_6 = time()
                    GameState = "block_6"
        
        elif GameState == "block_6":
            if 6 in CorrectBlocks:
                blink_6 = True
                if time() - time_block_6 > 1:
                    blink_6 = False
                    time_block_7 = time()
                    GameState = "block_7"
            else:
                if time() - time_block_6 > 0.01:
                    time_block_7 = time()
                    GameState = "block_7"
        
        elif GameState == "block_7":
            if 7 in CorrectBlocks:
                blink_7 = True
                if time() - time_block_7 > 1:
                    blink_7 = False
                    time_block_8 = time()
                    GameState = "block_8"
            else:
                if time() - time_block_7 > 0.01:
                    time_block_8 = time()
                    GameState = "block_8"
        
        elif GameState == "block_8":
            if 8 in CorrectBlocks:
                blink_8 = True
                if time() - time_block_8 > 1:
                    blink_8 = False
                    time_block_9 = time()
                    GameState = "block_9"
            else:
                if time() - time_block_8 > 0.01:
                    time_block_9 = time()
                    GameState = "block_9"
        
        elif GameState == "block_9":
            if 9 in CorrectBlocks:
                blink_9 = True
                if time() - time_block_9 > 1:
                    blink_9 = False
                    GameState = "wait_for_response"
            else:
                if time() - time_block_9 > 0.01:
                    GameState = "wait_for_response"
        #Unclicking of the blocks after 0.2 seconds
        elif on_spot_1 and time()- time_on_1 > 0.2:
                on_spot_1 = False
        elif on_spot_2 and time()- time_on_2 > 0.2:
                on_spot_2 = False
        elif on_spot_3 and time()- time_on_3 > 0.2:
                on_spot_3 = False
        elif on_spot_4 and time()- time_on_4 > 0.2:
                on_spot_4 = False
        elif on_spot_5 and time()- time_on_5 > 0.2:
                on_spot_5 = False
        elif on_spot_6 and time()- time_on_6 > 0.2:
                on_spot_6 = False
        elif on_spot_7 and time()- time_on_7 > 0.2:
                on_spot_7 = False
        elif on_spot_8 and time()- time_on_8 > 0.2:
                on_spot_8 = False
        elif on_spot_9 and time()- time_on_9 > 0.2:
                on_spot_9 = False
                
        elif GameState == "feedback":
            draw_feedback(this_correctness)
            if time() - time_when_feedback > 1:
                
                    trial_number += 1  
                    a_range = range(5, (screenSize[0] - 80), 80)
                    b_range = range(5, (screenSize[1] - 80), 40)
                    blocks = range(1,10)
                    del CorrectBlocks[:] #emptying the list
                    del UserInput[:] #emptying the list
            
                    if trial_number % 2.0 == 0: #checks if every n amunt of blocks is shown twice
                        if (correct_count[(len(correct_count) - 1)] == 1 or correct_count[(len(correct_count) - 2)] == 1): # checks the last two indcies of the correct count
                            sequence_length += 1
                            del correct_count[2:]
                    
                    GameState = "draw_stimulus"
                   
            elif time () - time_when_feedback > 0.8 and (correct_count[(len(correct_count) - 1)] == 2 and correct_count[(len(correct_count) - 2)] == 2):
        
                score = sequence_length - 1 #stopping criterion is met, so the score is the current (failed) n -1
                trial_number =  0
                a_range = range(5, (screenSize[0] - 80), 80)
                b_range = range(5, (screenSize[1] - 80), 40)
                blocks = range(1,10)
                del CorrectBlocks[:] #emptying the list
                del UserInput[:] #emptying the list
                del correct_count[2:]
                sequence_length = 2
                GameState = "stop"
            
        #drawing to the screen
        if GameState == "welcome":
            drawWelcomeText()

        if GameState == "explanation":
            drawExplanationText()
        
        if GameState == "ready":
            drawReadyText()
        
        if GameState == "show_blocks":
        
           drawButtons(blink_1, blink_2, blink_3, blink_4, blink_5, blink_6, blink_7, blink_8, blink_9, blockList, blockList[0].get_width(), blockList[0].get_height(), on_spot_1, on_spot_2, on_spot_3, on_spot_4, on_spot_5, on_spot_6, on_spot_7, on_spot_8, on_spot_9)
             
        if GameState == "block_1":
            drawButtons(blink_1, blink_2, blink_3, blink_4, blink_5, blink_6, blink_7, blink_8, blink_9, blockList, blockList[0].get_width(), blockList[0].get_height(), on_spot_1, on_spot_2, on_spot_3, on_spot_4, on_spot_5, on_spot_6, on_spot_7, on_spot_8, on_spot_9)
        
        if GameState == "block_2":
            drawButtons(blink_1, blink_2, blink_3, blink_4, blink_5, blink_6, blink_7, blink_8, blink_9, blockList, blockList[1].get_width(), blockList[0].get_height(), on_spot_1, on_spot_2, on_spot_3, on_spot_4, on_spot_5, on_spot_6, on_spot_7, on_spot_8, on_spot_9)
        
        if GameState == "block_3":
            drawButtons(blink_1, blink_2, blink_3, blink_4, blink_5, blink_6, blink_7, blink_8, blink_9, blockList, blockList[2].get_width(), blockList[1].get_height(), on_spot_1, on_spot_2, on_spot_3, on_spot_4, on_spot_5, on_spot_6, on_spot_7, on_spot_8, on_spot_9)
        
        if GameState == "block_4":
            drawButtons(blink_1, blink_2, blink_3, blink_4, blink_5, blink_6, blink_7, blink_8, blink_9, blockList, blockList[3].get_width(), blockList[2].get_height(), on_spot_1, on_spot_2, on_spot_3, on_spot_4, on_spot_5, on_spot_6, on_spot_7, on_spot_8, on_spot_9)
            
        if GameState == "block_5":
            drawButtons(blink_1, blink_2, blink_3, blink_4, blink_5, blink_6, blink_7, blink_8, blink_9, blockList, blockList[4].get_width(), blockList[3].get_height(), on_spot_1, on_spot_2, on_spot_3, on_spot_4, on_spot_5, on_spot_6, on_spot_7, on_spot_8, on_spot_9)
        
        if GameState == "block_6":
            drawButtons(blink_1, blink_2, blink_3, blink_4, blink_5, blink_6, blink_7, blink_8, blink_9, blockList, blockList[5].get_width(), blockList[4].get_height(), on_spot_1, on_spot_2, on_spot_3, on_spot_4, on_spot_5, on_spot_6, on_spot_7, on_spot_8, on_spot_9)
        
        if GameState == "block_7":
            drawButtons(blink_1, blink_2, blink_3, blink_4, blink_5, blink_6, blink_7, blink_8, blink_9, blockList, blockList[6].get_width(), blockList[5].get_height(), on_spot_1, on_spot_2, on_spot_3, on_spot_4, on_spot_5, on_spot_6, on_spot_7, on_spot_8, on_spot_9)
        
        if GameState == "block_8":
            drawButtons(blink_1, blink_2, blink_3, blink_4, blink_5, blink_6, blink_7, blink_8, blink_9, blockList, blockList[7].get_width(), blockList[6].get_height(), on_spot_1, on_spot_2, on_spot_3, on_spot_4, on_spot_5, on_spot_6, on_spot_7, on_spot_8, on_spot_9)
        
        if GameState == "block_9":
            drawButtons(blink_1, blink_2, blink_3, blink_4, blink_5, blink_6, blink_7, blink_8, blink_9, blockList, blockList[8].get_width(), blockList[7].get_height(), on_spot_1, on_spot_2, on_spot_3, on_spot_4, on_spot_5, on_spot_6, on_spot_7, on_spot_8, on_spot_9)
        
        if GameState == "wait_for_response":
            drawButtons(blink_1, blink_2, blink_3, blink_4, blink_5, blink_6, blink_7, blink_8, blink_9, blockList, blockList[0].get_width(), blockList[8].get_height(), on_spot_1, on_spot_2, on_spot_3, on_spot_4, on_spot_5, on_spot_6, on_spot_7, on_spot_8, on_spot_9)
            draw_next()
            
        if GameState == "stop":
            drawGoodbyeText(score)
            draw_button2(mouse, on_spot)
        
        
        if GameState == "quit":
            pygame.quit()
            sys.exit()
        
        
        pygame.display.update()


def generateBlockPositions():

    # Generate 9 blocks objects
    generator = BlockGenerator()
    generator.generateBlocks()
    return generator.blockList()


def drawWelcomeText():
    text_surface = font.render("Corsi Block Tapping Task", True, col_black, backgroundColour)
    text_rectangle = text_surface.get_rect()
    text_rectangle.center = (screenSize[0] / 2.0, 150)
    screen.blit(text_surface, text_rectangle)
    text_surface = font_small.render("Press Spacebar to start", True, col_black, backgroundColour)
    text_rectangle = text_surface.get_rect()
    text_rectangle.center = (screenSize[0] / 2.0, 400)
    screen.blit(text_surface, text_rectangle)
    
def drawExplanationText():
    text_surface = font.render("Corsi Block Tapping Task", True, col_black, backgroundColour)
    text_rectangle = text_surface.get_rect()
    text_rectangle.center = (screenSize[0] / 2.0, 150)
    screen.blit(text_surface, text_rectangle)
    text_surface = font_xsmall.render("The Corsi Block-Tapping Test is a psychological test that assesses visuo-spatial short", True, col_black, backgroundColour)
    screen.blit(text_surface, (100, 260))
    text_surface = font_xsmall.render("term working memory. The test involves mimicking a computer generated sequence of ", True, col_black, backgroundColour)
    screen.blit(text_surface, (100, 290))
    text_surface = font_xsmall.render("up to nine identical spatially separated blocks. The sequence starts out simple with", True, col_black, backgroundColour)
    screen.blit(text_surface, (100, 320))
    text_surface = font_xsmall.render("just two blocks, but becomes more complex until you are no longer able to remember", True, col_black, backgroundColour)
    screen.blit(text_surface, (100, 350))
    text_surface = font_xsmall.render("the sequence. This results in the so called Corsi Score.", True, col_black, backgroundColour)
    screen.blit(text_surface, (100, 380))
    screen.blit(image, (400,425))   
    text_surface = font_xsmall.render("press Spacebar to start", True, col_black, backgroundColour)
    text_rectangle = text_surface.get_rect()
    text_rectangle.center = (screenSize[0] / 2.0, 630)
    screen.blit(text_surface, text_rectangle)


def drawReadyText():
    text_surface = font_small.render("Ready?", True, col_black, backgroundColour)
    text_rectangle = text_surface.get_rect()
    text_rectangle.center = (screenSize[0] / 2.0, screenSize[1] / 2.0)
    screen.blit(text_surface, text_rectangle)


def drawGoodbyeText(score):
    text_surface = font_xsmall.render("Close the application or try again!", True, col_black, backgroundColour)
    text_rectangle = text_surface.get_rect()
    text_rectangle.center = (screenSize[0] / 2.0, screenSize[1] / 2.0)
    screen.blit(text_surface, text_rectangle)
    
    text_surface = font_small.render("Your Corsi Score is  %s" % score, True, col_black, backgroundColour)
    text_rectangle = text_surface.get_rect()
    text_rectangle.center = (screenSize[0] / 2.0, screenSize[1] / 3.0)
    screen.blit(text_surface, text_rectangle)


# def pick_coordinates_x(a):
#
#     random_number = random.choice(a)
#     a.remove(random_number)
#     return random_number
#
#
# def pick_coordinates_y(b):
#
#     random_number_1 = random.choice(b)
#     b.remove(random_number_1)
#     return random_number_1
 

def blockGeneration(sequence_length, blocks):

    x = 0
    while x < sequence_length:
        random_number = random.choice(blocks)
        CorrectBlocks.append(random_number)
        blocks.remove(random_number) #avoids duplicates
        CorrectBlocks.sort() #block numbers in ascending order so they all execute during the states
        x += 1
    
def drawButtons(blink_1, blink_2, blink_3, blink_4, blink_5, blink_6, blink_7, blink_8, blink_9, blockList, block_w, block_h, on_spot_1, on_spot_2, on_spot_3, on_spot_4, on_spot_5, on_spot_6, on_spot_7, on_spot_8, on_spot_9):
   
    color_1 = col_green_dim
    color_2 = col_green_dim
    color_3 = col_green_dim
    color_4 = col_green_dim
    color_5 = col_green_dim
    color_6 = col_green_dim
    color_7 = col_green_dim
    color_8 = col_green_dim
    color_9 = col_green_dim
    
    if blink_1:
        color_1 = col_green
    elif blink_2:
        color_2 = col_green
    elif blink_3:
        color_3 = col_green
    elif blink_4:
        color_4 = col_green
    elif blink_5:
        color_5 = col_green
    elif blink_6:
        color_6 = col_green
    elif blink_7:
        color_7 = col_green
    elif blink_8:
        color_8 = col_green
    elif blink_9:
        color_9 = col_green
        
    if on_spot_1:
        color_1 = col_green
    elif on_spot_2:
        color_2 = col_green
    elif on_spot_3:
        color_3 = col_green
    elif on_spot_4:
        color_4 = col_green
    elif on_spot_5:
        color_5 = col_green
    elif on_spot_6:
        color_6 = col_green
    elif on_spot_7:
        color_7 = col_green
    elif on_spot_8:
        color_8 = col_green
    elif on_spot_9:
        color_9 = col_green


    pygame.draw.rect(screen, color_1, (blockList[0].get_x(), blockList[0].get_y(), block_w, block_h))
    pygame.draw.rect(screen, color_2, (blockList[1].get_x(), blockList[1].get_y(), block_w, block_h))
    pygame.draw.rect(screen, color_3, (blockList[2].get_x(), blockList[2].get_y(), block_w, block_h))
    pygame.draw.rect(screen, color_4, (blockList[3].get_x(), blockList[3].get_y(), block_w, block_h))
    pygame.draw.rect(screen, color_5, (blockList[4].get_x(), blockList[4].get_y(), block_w, block_h))
    pygame.draw.rect(screen, color_6, (blockList[5].get_x(), blockList[5].get_y(), block_w, block_h))
    pygame.draw.rect(screen, color_7, (blockList[6].get_x(), blockList[6].get_y(), block_w, block_h))
    pygame.draw.rect(screen, color_8, (blockList[7].get_x(), blockList[7].get_y(), block_w, block_h))
    pygame.draw.rect(screen, color_9, (blockList[8].get_x(), blockList[8].get_y(), block_w, block_h))
     
    
def draw_next():
    
        text_surface = font_small.render("press the spacebar when done", True, col_black, backgroundColour)
        text_rectangle = text_surface.get_rect()
        text_rectangle.center = (screenSize[0] / 2.0, screenSize[1] - 20)
        screen.blit(text_surface, text_rectangle)
    
def draw_feedback(correct): 
    
    if correct:
       
        text_surface = font_small.render("Correct!", True, col_black, backgroundColour)
        text_rectangle = text_surface.get_rect()
        text_rectangle.center = (screenSize[0] / 2.0, screenSize[1] / 2.0)
        screen.blit(text_surface, text_rectangle)
        
    else:
      
        text_surface = font_small.render("Incorrect", True, col_black, backgroundColour)
        text_rectangle = text_surface.get_rect()
        text_rectangle.center = (screenSize[0] / 2.0, screenSize[1] / 2.0)
        screen.blit(text_surface, text_rectangle)

def draw_button2(mouse, on_spot):
    
    if on_spot:
        color = col_green
          
    else:
        color = col_green_dim
        
    pygame.draw.rect(screen, color, (500, 400, 100, 50))
    text_surface = font_xsmall.render("try again", True, col_white)
    text_rectangle = text_surface.get_rect()
    text_rectangle.center = ( (500+(100/2)), 400+(50/2))
    screen.blit(text_surface, text_rectangle)
    
main()
        
        
