
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

    def __init__(self, x, y, block_nr):
        # Block sizes; width and heigth, you can change them here
        self._width = 75
        self._height = 75
        self._x = x
        self._y = y
        self._block_nr = block_nr
        self._blink = False
        self._clicked = False
        self._block_time = None
        self._click_time = None

    def is_cursor_over(self, mouse):
        mouse_x = mouse[0]
        mouse_y = mouse[1]
        if (self._x + self.get_width() > mouse_x > self.get_x() and self.get_y() +
                self.get_height() > mouse_y > self.get_y()):
            return True
        else:
            return False

    def click(self):
        self._clicked = True
        self._click_time = time()

    def unclick(self):
        self._clicked = False

    def is_clicked(self):
        return self._clicked

    def get_click_time(self):
        return self._click_time

    def set_block_time(self, time):
        self._block_time = time

    def get_block_time(self):
        return self._block_time

    def set_blink(self, value):
        self._blink = value

    def get_blink(self):
        return self._blink

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

def main():

    on_spot = False
    a_range = range(5, (screenSize[0] - 80), 80)    #sets the range for the coordinates; always 5 pixels from edge of screen and 5 pixels between blocks.
    b_range = range(5, (screenSize[1] - 80), 40)    #sets the range for the coordinates; always 5 pixels from edge of screen and 5 pixels between blocks.
    blocks = range(1,10)
    correct_count = [0,0]
    sequence_length = 2                     #the minimum sequence length is set to two.
    trial_number = 0
    GameState = "welcome"

    blockList = []


    while True:
        pygame.display.get_surface().fill(backgroundColour)

        mouse = pygame.mouse.get_pos()      #gets the mouse position(x,y).
        
        #ITC
        for event in pygame.event.get():
            if GameState == "welcome":          #When state is "welcome" the welcome screen is shown.
                blockList = generateBlockPositions()
                if event.type == KEYDOWN and event.key == K_SPACE:
                    GameState = "explanation"
                    
            elif GameState == "explanation":    #When state is "explanation", the experiment will be explained.
                if event.type == KEYDOWN and event.key == K_SPACE:
                    GameState = "draw_stimulus"
    
            elif GameState == "wait_for_response":
                if (blockList[0].is_cursor_over(mouse)):
                    if event.type == MOUSEBUTTONUP:
                        blockList[0].click()
                        drawButtons(blockList, blockList[0].get_width(), blockList[0].get_height())
                        UserInput.append(1)  #appends the number for this block to the empty response list so it can be compared with the trial list.
                elif (blockList[1].is_cursor_over(mouse)):
                    if event.type == MOUSEBUTTONUP:
                        blockList[1].click()
                        drawButtons(blockList, blockList[0].get_width(), blockList[0].get_height())
                        UserInput.append(2)
                elif (blockList[2].is_cursor_over(mouse)):
                    if event.type == MOUSEBUTTONUP:
                        blockList[2].click()
                        drawButtons(blockList, blockList[0].get_width(), blockList[0].get_height())
                        UserInput.append(3)
                elif (blockList[3].is_cursor_over(mouse)):
                    if event.type == MOUSEBUTTONUP:
                        blockList[3].click()
                        drawButtons(blockList, blockList[0].get_width(), blockList[0].get_height())
                        UserInput.append(4)
                elif (blockList[4].is_cursor_over(mouse)):
                    if event.type == MOUSEBUTTONUP:
                        blockList[4].click()
                        drawButtons(blockList, blockList[0].get_width(), blockList[0].get_height())
                        UserInput.append(5)
                elif (blockList[5].is_cursor_over(mouse)):
                    if event.type == MOUSEBUTTONUP:
                        blockList[5].click()
                        drawButtons(blockList, blockList[0].get_width(), blockList[0].get_height())
                        UserInput.append(6)
                elif (blockList[6].is_cursor_over(mouse)):
                    if event.type == MOUSEBUTTONUP:
                        blockList[6].click()
                        drawButtons(blockList, blockList[0].get_width(), blockList[0].get_height())
                        UserInput.append(7)
                elif (blockList[7].is_cursor_over(mouse)):
                    if event.type == MOUSEBUTTONUP:
                        blockList[7].click()
                        drawButtons(blockList, blockList[0].get_width(), blockList[0].get_height())
                        UserInput.append(8)
                elif (blockList[8].is_cursor_over(mouse)):
                    if event.type == MOUSEBUTTONUP:
                        blockList[8].click()
                        drawButtons(blockList, blockList[0].get_width(), blockList[0].get_height())
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
            #blockList = generateBlockPositions()
            blockGeneration(sequence_length, blocks)
            time_ready = time()
            GameState = "ready"
        
        elif GameState == "ready":              #'ready?' is shown on screen.
            if time() - time_ready > 1:
                time_show_blocks = time()
                GameState = "show_blocks"
        
        elif GameState == "show_blocks":        #The nine blocks are shown on screen.
            if time() - time_show_blocks > 0.5:
                blockList[0].set_block_time(time())
                GameState = "block_1"
                
        elif GameState == "block_1":
            if 1 in CorrectBlocks:
                blockList[0].set_blink(True)
                if time() - blockList[0].get_block_time() > 1:
                    blockList[0].set_blink(False)
                    GameState = "block_2"
                    blockList[1].set_block_time(time())
            else:
                if time() - time_show_blocks > 0.01:
                    blockList[1].set_block_time(time())
                    GameState = "block_2"
        
        elif GameState == "block_2":
            if 2 in CorrectBlocks:
                blockList[1].set_blink(True)
                if time() - blockList[1].get_block_time() > 1:
                    blockList[1].set_blink(False)
                    blockList[2].set_block_time(time())
                    GameState = "block_3"
            else:
                if time() - blockList[1].get_block_time() > 0.01:
                    blockList[2].set_block_time(time())
                    GameState = "block_3"
        
        elif GameState == "block_3":
            if 3 in CorrectBlocks:
                blockList[2].set_blink(True)
                if time() - blockList[2].get_block_time() > 1:
                    blockList[2].set_blink(False)
                    blockList[3].set_block_time(time())
                    GameState = "block_4"
            else:
                if time() - blockList[2].get_block_time() > 0.01:
                    blockList[3].set_block_time(time())
                    GameState = "block_4"
        
        elif GameState == "block_4":
            if 4 in CorrectBlocks:
                blockList[3].set_blink(True)
                if time() - blockList[3].get_block_time() > 1:
                    blockList[3].set_blink(False)
                    blockList[4].set_block_time(time())
                    GameState = "block_5"
            else:
                if time() - blockList[3].get_block_time() > 0.01:
                    blockList[4].set_block_time(time())
                    GameState = "block_5"
        
        elif GameState == "block_5":
            if 5 in CorrectBlocks:
                blockList[4].set_blink(True)
                if time() - blockList[4].get_block_time() > 1:
                    blockList[4].set_blink(False)
                    blockList[5].set_block_time(time())
                    GameState = "block_6"
            else:
                if time() - blockList[4].get_block_time() > 0.01:
                    blockList[5].set_block_time(time())
                    GameState = "block_6"
        
        elif GameState == "block_6":
            if 6 in CorrectBlocks:
                blockList[5].set_blink(True)
                if time() - blockList[5].get_block_time() > 1:
                    blockList[5].set_blink(False)
                    blockList[6].set_block_time(time())
                    GameState = "block_7"
            else:
                if time() - blockList[5].get_block_time() > 0.01:
                    blockList[6].set_block_time(time())
                    GameState = "block_7"
        
        elif GameState == "block_7":
            if 7 in CorrectBlocks:
                blockList[6].set_blink(True)
                if time() - blockList[6].get_block_time() > 1:
                    blockList[6].set_blink(False)
                    blockList[7].set_block_time(time())
                    GameState = "block_8"
            else:
                if time() - blockList[6].get_block_time() > 0.01:
                    blockList[7].set_block_time(time())
                    GameState = "block_8"
        
        elif GameState == "block_8":
            if 8 in CorrectBlocks:
                blockList[7].set_blink(True)
                if time() - blockList[7].get_block_time() > 1:
                    blockList[7].set_blink(False)
                    blockList[8].set_block_time(time())
                    GameState = "block_9"
            else:
                if time() - blockList[7].get_block_time() > 0.01:
                    blockList[8].set_block_time(time())
                    GameState = "block_9"
        
        elif GameState == "block_9":
            if 9 in CorrectBlocks:
                blockList[8].set_blink(True)
                if time() - blockList[8].get_block_time() > 1:
                    blockList[8].set_blink(False)
                    GameState = "wait_for_response"
            else:
                if time() - blockList[8].get_block_time() > 0.01:
                    GameState = "wait_for_response"
        #Unclicking of the blocks after 0.2 seconds (changed to 3)
        elif blockList[0].is_clicked() and time()- blockList[0].get_click_time() > 0.2:
                blockList[0].unclick()
        elif blockList[1].is_clicked() and time()- blockList[1].get_click_time() > 0.2:
                blockList[1].unclick()
        elif blockList[2].is_clicked() and time()- blockList[2].get_click_time() > 0.2:
                blockList[2].unclick()
        elif blockList[3].is_clicked() and time()- blockList[3].get_click_time() > 0.2:
                blockList[3].unclick()
        elif blockList[4].is_clicked() and time()- blockList[4].get_click_time() > 0.2:
                 blockList[4].unclick()
        elif blockList[5].is_clicked() and time()- blockList[5].get_click_time() > 0.2:
                blockList[5].unclick()
        elif blockList[6].is_clicked() and time()- blockList[6].get_click_time() > 0.2:
                blockList[6].unclick()
        elif blockList[7].is_clicked() and time()- blockList[7].get_click_time() > 0.2:
                blockList[7].unclick()
        elif blockList[8].is_clicked() and time()- blockList[8].get_click_time() > 0.2:
                blockList[8].unclick()
                
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
        
           drawButtons(blockList, blockList[0].get_width(), blockList[0].get_height())
             
        if GameState == "block_1":
            drawButtons(blockList, blockList[0].get_width(), blockList[0].get_height())
        
        if GameState == "block_2":
            drawButtons(blockList, blockList[1].get_width(), blockList[0].get_height())
        
        if GameState == "block_3":
            drawButtons(blockList, blockList[2].get_width(), blockList[1].get_height())
        
        if GameState == "block_4":
            drawButtons(blockList, blockList[3].get_width(), blockList[2].get_height())
            
        if GameState == "block_5":
            drawButtons(blockList, blockList[4].get_width(), blockList[3].get_height())
        
        if GameState == "block_6":
            drawButtons(blockList, blockList[5].get_width(), blockList[4].get_height())
        
        if GameState == "block_7":
            drawButtons(blockList, blockList[6].get_width(), blockList[5].get_height())
        
        if GameState == "block_8":
            drawButtons(blockList, blockList[7].get_width(), blockList[6].get_height())
        
        if GameState == "block_9":
            drawButtons(blockList, blockList[8].get_width(), blockList[7].get_height())
        
        if GameState == "wait_for_response":
            drawButtons(blockList, blockList[0].get_width(), blockList[0].get_height())
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


def blockGeneration(sequence_length, blocks):

    x = 0
    while x < sequence_length:
        random_number = random.choice(blocks)
        CorrectBlocks.append(random_number)
        blocks.remove(random_number) #avoids duplicates
        CorrectBlocks.sort() #block numbers in ascending order so they all execute during the states
        x += 1
    
def drawButtons(blockList, block_w, block_h):
   
    color_1 = col_green_dim
    color_2 = col_green_dim
    color_3 = col_green_dim
    color_4 = col_green_dim
    color_5 = col_green_dim
    color_6 = col_green_dim
    color_7 = col_green_dim
    color_8 = col_green_dim
    color_9 = col_green_dim
    
    if blockList[0].get_blink():
        color_1 = col_green
    elif blockList[1].get_blink():
        color_2 = col_green
    elif blockList[2].get_blink():
        color_3 = col_green
    elif blockList[3].get_blink():
        color_4 = col_green
    elif blockList[4].get_blink():
        color_5 = col_green
    elif blockList[5].get_blink():
        color_6 = col_green
    elif blockList[6].get_blink():
        color_7 = col_green
    elif blockList[7].get_blink():
        color_8 = col_green
    elif blockList[8].get_blink():
        color_9 = col_green
        
    if blockList[0].is_clicked():
        color_1 = col_green
    elif blockList[1].is_clicked():
        color_2 = col_green
    elif blockList[2].is_clicked():
        color_3 = col_green
    elif blockList[3].is_clicked():
        color_4 = col_green
    elif blockList[4].is_clicked():
        color_5 = col_green
    elif blockList[5].is_clicked():
        color_6 = col_green
    elif blockList[6].is_clicked():
        color_7 = col_green
    elif blockList[7].is_clicked():
        color_8 = col_green
    elif blockList[8].is_clicked():
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
        
        
