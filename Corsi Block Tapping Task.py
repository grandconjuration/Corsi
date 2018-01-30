
import pygame
import sys
from time import time
from pygame.locals import *
import random
from pygame.compat import unichr_, unicode_

##### VARIABLES #####
# Colors
col_white  = (255, 255, 255)
col_black = (0, 0, 0)
col_gray = (220, 245, 249)
col_green = (63, 246, 7)
col_green_dim = (0, 60, 0)


# empty list for storing the blocks to be presented during a trial.
response = []
#empty list for storing the input of the user.
trial = []

# Block sizes; width and heigth, you can change them here 
block_w = 75
block_h = 75

BACKGR_COL = col_gray
SCREEN_SIZE = (1100, 680)

pygame.init()
pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Corsi Block Tapping Task")

screen = pygame.display.get_surface()
screen.fill(BACKGR_COL)

image = pygame.image.load("corsi.png")              #loads the image if it is in the same map as the .py code.

font = pygame.font.Font(None, 80)                   #creates font sizes.
font_small = pygame.font.Font(None, 40)
font_xsmall = pygame.font.Font(None, 30)

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
    a = range(5,(SCREEN_SIZE[0]-80), 80)    #sets the range for the coordinates; always 5 pixels from edge of screen and 5 pixels between blocks.
    b = range(5,(SCREEN_SIZE[1]-80), 40)    #sets the range for the coordinates; always 5 pixels from edge of screen and 5 pixels between blocks.
    blocks = range(1,10)
    correct_count = [0,0]
    sequence_length = 2                     #the minimum sequence length is set to two.
    trial_number = 0
    STATE = "welcome"

    while True:
        pygame.display.get_surface().fill(BACKGR_COL)

        mouse = pygame.mouse.get_pos()      #gets the mouse position(x,y).
        
        #ITC
        for event in pygame.event.get():
            if STATE == "welcome":          #When state is "welcome" the welcome screen is shown.
                if event.type == KEYDOWN and event.key == K_SPACE:
                    STATE = "explanation"
                    
            elif STATE == "explanation":    #When state is "explanation", the experiment will be explained.
                if event.type == KEYDOWN and event.key == K_SPACE:
                    STATE = "draw_stimulus"
    
            elif STATE == "wait_for_response":
                if (this_x+block_w > mouse[0] > this_x and this_y+block_h > mouse[1] > this_y): #is the mousecursor 'over' the rect area?
                    if event.type == MOUSEBUTTONUP:
                        on_spot_1 = True
                        time_on_1 = time() 
                        response.append(1)  #appends the number for this block to the empty response list so it can be compared with the trial list.
                elif (this_x_1+block_w > mouse[0] > this_x_1 and this_y_1+block_h > mouse[1] > this_y_1):
                    if event.type == MOUSEBUTTONUP:
                        on_spot_2 = True
                        time_on_2 = time() 
                        response.append(2)
                elif (this_x_2+block_w > mouse[0] > this_x_2 and this_y_2+block_h > mouse[1] > this_y_2):
                    if event.type == MOUSEBUTTONUP:
                        on_spot_3 = True
                        time_on_3 = time() 
                        response.append(3)
                elif (this_x_3+block_w > mouse[0] > this_x_3 and this_y_3+block_h > mouse[1] > this_y_3):
                    if event.type == MOUSEBUTTONUP:
                        on_spot_4 = True
                        time_on_4 = time() 
                        response.append(4)
                elif (this_x_4+block_w > mouse[0] > this_x_4 and this_y_4+block_h > mouse[1] > this_y_4):
                    if event.type == MOUSEBUTTONUP:
                        on_spot_5 = True
                        time_on_5 = time()
                        response.append(5)
                elif (this_x_5+block_w > mouse[0] > this_x_5 and this_y_5+block_h > mouse[1] > this_y_5):
                    if event.type == MOUSEBUTTONUP:
                        on_spot_6 = True
                        time_on_6 = time() 
                        response.append(6)
                elif (this_x_6+block_w > mouse[0] > this_x_6 and this_y_6+block_h > mouse[1] > this_y_6):
                    if event.type == MOUSEBUTTONUP:
                        on_spot_7 = True
                        time_on_7 = time() 
                        response.append(7)
                elif (this_x_7+block_w > mouse[0] > this_x_7 and this_y_7+block_h > mouse[1] > this_y_7):
                    if event.type == MOUSEBUTTONUP:
                        on_spot_8 = True
                        time_on_8 = time() 
                        response.append(8)
                elif (this_x_8+block_w > mouse[0] > this_x_8 and this_y_8+block_h > mouse[1] > this_y_8):
                    if event.type == MOUSEBUTTONUP:
                        on_spot_9 = True
                        time_on_9 = time() 
                        response.append(9)    
                if event.type ==  KEYDOWN and event.key == K_SPACE:
                    this_correctness = (trial == response) 
                    if this_correctness == True:
                        correct_count.append(1)
                    else:
                        correct_count.append(2)
                    time_when_feedback = time()
                    STATE = "feedback" 
            
            elif STATE == "stop":           #When state is "stop" the result is shown.
                if (500+100 > mouse[0] > 500 and 400+50 > mouse[1] > 400):   #Is the mouse on the button spot?
                    on_spot = True
                    if event.type == MOUSEBUTTONUP:   #If button is pressed start the test again.
                        on_spot = False
                        STATE = "draw_stimulus"
                else:
                    on_spot = False
            if event.type == QUIT:
                STATE = "quit"
        
        
        #ATC
        if STATE == "draw_stimulus":      #The nine blocks positions are generated.
            pick_blocks(sequence_length, blocks)
            this_x = pick_coordinates_x(a)
            this_y = pick_coordinates_y(b)
            this_x_1 = pick_coordinates_x(a)
            this_y_1 = pick_coordinates_y(b)
            this_x_2 = pick_coordinates_x(a)
            this_y_2 = pick_coordinates_y(b)
            this_x_3 = pick_coordinates_x(a)
            this_y_3 = pick_coordinates_y(b)
            this_x_4 = pick_coordinates_x(a)
            this_y_4 = pick_coordinates_y(b)
            this_x_5 = pick_coordinates_x(a)
            this_y_5 = pick_coordinates_y(b)
            this_x_6 = pick_coordinates_x(a)
            this_y_6 = pick_coordinates_y(b)
            this_x_7 = pick_coordinates_x(a)
            this_y_7 = pick_coordinates_y(b)
            this_x_8 = pick_coordinates_x(a)
            this_y_8 = pick_coordinates_y(b)
            time_ready = time()
            STATE = "ready"
        
        elif STATE == "ready":              #'ready?' is shown on screen.
            if time() - time_ready > 1:
                time_show_blocks = time()
                STATE = "show_blocks"
        
        elif STATE == "show_blocks":        #The nine blocks are shown on screen.
            if time() - time_show_blocks > 0.5:
                time_block_1 = time()
                STATE = "block_1"
                
        elif STATE == "block_1":
            if 1 in trial:
                blink_1 = True
                if time() - time_block_1 > 1:
                    blink_1 = False
                    STATE = "block_2"
                    time_block_2 = time()
            else:
                if time() - time_show_blocks > 0.01:
                    time_block_2 = time()
                    STATE = "block_2"
        
        elif STATE == "block_2":
            if 2 in trial:
                blink_2 = True
                if time() - time_block_2 > 1:
                    blink_2 = False
                    time_block_3 = time()
                    STATE = "block_3"
            else:
                if time() - time_block_2 > 0.01:
                    time_block_3 = time()
                    STATE = "block_3"
        
        elif STATE == "block_3":
            if 3 in trial:
                blink_3 = True
                if time() - time_block_3 > 1:
                    blink_3 = False
                    time_block_4 = time()
                    STATE = "block_4"
            else:
                if time() - time_block_3 > 0.01:
                    time_block_4 = time()
                    STATE = "block_4"
        
        elif STATE == "block_4":
            if 4 in trial:
                blink_4 = True
                if time() - time_block_4 > 1:
                    blink_4 = False
                    time_block_5 = time()
                    STATE = "block_5"
            else:
                if time() - time_block_4 > 0.01:
                    time_block_5 = time()
                    STATE = "block_5"
        
        elif STATE == "block_5":
            if 5 in trial:
                blink_5 = True
                if time() - time_block_5 > 1:
                    blink_5 = False
                    STATE = "block_6"
                    time_block_6 = time()
            else:
                if time() - time_block_5 > 0.01:
                    time_block_6 = time()
                    STATE = "block_6"
        
        elif STATE == "block_6":
            if 6 in trial:
                blink_6 = True
                if time() - time_block_6 > 1:
                    blink_6 = False
                    time_block_7 = time()
                    STATE = "block_7"
            else:
                if time() - time_block_6 > 0.01:
                    time_block_7 = time()
                    STATE = "block_7"
        
        elif STATE == "block_7":
            if 7 in trial:
                blink_7 = True
                if time() - time_block_7 > 1:
                    blink_7 = False
                    time_block_8 = time()
                    STATE = "block_8"
            else:
                if time() - time_block_7 > 0.01:
                    time_block_8 = time()
                    STATE = "block_8"
        
        elif STATE == "block_8":
            if 8 in trial:
                blink_8 = True
                if time() - time_block_8 > 1:
                    blink_8 = False
                    time_block_9 = time()
                    STATE = "block_9"
            else:
                if time() - time_block_8 > 0.01:
                    time_block_9 = time()
                    STATE = "block_9"
        
        elif STATE == "block_9":
            if 9 in trial:
                blink_9 = True
                if time() - time_block_9 > 1:
                    blink_9 = False
                    STATE = "wait_for_response"
            else:
                if time() - time_block_9 > 0.01:
                    STATE = "wait_for_response"
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
                
        elif STATE == "feedback":
            draw_feedback(this_correctness)
            if time() - time_when_feedback > 1:
                
                    trial_number += 1  
                    a = range(5,(SCREEN_SIZE[0]-80), 80)
                    b = range(5,(SCREEN_SIZE[1]-80), 40)
                    blocks = range(1,10)
                    del trial[:] #emptying the list
                    del response[:] #emptying the list
            
                    if trial_number % 2.0 == 0: #checks if every n amunt of blocks is shown twice
                        if (correct_count[(len(correct_count) - 1)] == 1 or correct_count[(len(correct_count) - 2)] == 1): # checks the last two indcies of the correct count
                            sequence_length += 1
                            del correct_count[2:]
                    
                    STATE = "draw_stimulus"
                   
            elif time () - time_when_feedback > 0.8 and (correct_count[(len(correct_count) - 1)] == 2 and correct_count[(len(correct_count) - 2)] == 2):
        
                score = sequence_length - 1 #stopping criterion is met, so the score is the current (failed) n -1
                trial_number =  0
                a = range(5,(SCREEN_SIZE[0]-80), 80)
                b = range(5,(SCREEN_SIZE[1]-80), 40)
                blocks = range(1,10)
                del trial[:] #emptying the list
                del response[:] #emptying the list
                del correct_count[2:]
                sequence_length = 2
                STATE = "stop"
            
        #drawing to the screen
        if STATE == "welcome":
            draw_welcome()

        if STATE == "explanation":
            draw_explanation()
        
        if STATE == "ready":
            show_ready()
        
        if STATE == "show_blocks":
        
           draw_button( blink_1, blink_2, blink_3, blink_4, blink_5,blink_6, blink_7, blink_8, blink_9, this_x, this_y, this_x_1, this_y_1, this_x_2, this_y_2, this_x_3, this_y_3, this_x_4, this_y_4,
                            this_x_5, this_y_5, this_x_6, this_y_6, this_x_7, this_y_7, this_x_8, this_y_8, block_w, block_h, on_spot_1, on_spot_2, on_spot_3, on_spot_4, on_spot_5, on_spot_6, on_spot_7, on_spot_8, on_spot_9)
             
        if STATE == "block_1":
            draw_button( blink_1, blink_2, blink_3, blink_4, blink_5,blink_6, blink_7, blink_8, blink_9, this_x, this_y, this_x_1, this_y_1, this_x_2, this_y_2, this_x_3, this_y_3, this_x_4, this_y_4,
                            this_x_5, this_y_5, this_x_6, this_y_6, this_x_7, this_y_7, this_x_8, this_y_8, block_w, block_h, on_spot_1, on_spot_2, on_spot_3, on_spot_4, on_spot_5, on_spot_6, on_spot_7, on_spot_8, on_spot_9)
        
        if STATE == "block_2":
            draw_button( blink_1, blink_2, blink_3, blink_4, blink_5,blink_6, blink_7, blink_8, blink_9, this_x, this_y, this_x_1, this_y_1, this_x_2, this_y_2, this_x_3, this_y_3, this_x_4, this_y_4,
                            this_x_5, this_y_5, this_x_6, this_y_6, this_x_7, this_y_7, this_x_8, this_y_8, block_w, block_h, on_spot_1, on_spot_2, on_spot_3, on_spot_4, on_spot_5, on_spot_6, on_spot_7, on_spot_8, on_spot_9)
        
        if STATE == "block_3":
            draw_button( blink_1, blink_2, blink_3, blink_4, blink_5,blink_6, blink_7, blink_8, blink_9, this_x, this_y, this_x_1, this_y_1, this_x_2, this_y_2, this_x_3, this_y_3, this_x_4, this_y_4,
                            this_x_5, this_y_5, this_x_6, this_y_6, this_x_7, this_y_7, this_x_8, this_y_8, block_w, block_h, on_spot_1, on_spot_2, on_spot_3, on_spot_4, on_spot_5, on_spot_6, on_spot_7, on_spot_8, on_spot_9)
        
        if STATE == "block_4":
            draw_button( blink_1, blink_2, blink_3, blink_4, blink_5,blink_6, blink_7, blink_8, blink_9, this_x, this_y, this_x_1, this_y_1, this_x_2, this_y_2, this_x_3, this_y_3, this_x_4, this_y_4,
                            this_x_5, this_y_5, this_x_6, this_y_6, this_x_7, this_y_7, this_x_8, this_y_8, block_w, block_h, on_spot_1, on_spot_2, on_spot_3, on_spot_4, on_spot_5, on_spot_6, on_spot_7, on_spot_8, on_spot_9)
            
        if STATE == "block_5":
            draw_button( blink_1, blink_2, blink_3, blink_4, blink_5,blink_6, blink_7, blink_8, blink_9, this_x, this_y, this_x_1, this_y_1, this_x_2, this_y_2, this_x_3, this_y_3, this_x_4, this_y_4,
                            this_x_5, this_y_5, this_x_6, this_y_6, this_x_7, this_y_7, this_x_8, this_y_8, block_w, block_h, on_spot_1, on_spot_2, on_spot_3, on_spot_4, on_spot_5, on_spot_6, on_spot_7, on_spot_8, on_spot_9)
        
        if STATE == "block_6":
            draw_button( blink_1, blink_2, blink_3, blink_4, blink_5,blink_6, blink_7, blink_8, blink_9, this_x, this_y, this_x_1, this_y_1, this_x_2, this_y_2, this_x_3, this_y_3, this_x_4, this_y_4,
                            this_x_5, this_y_5, this_x_6, this_y_6, this_x_7, this_y_7, this_x_8, this_y_8, block_w, block_h, on_spot_1, on_spot_2, on_spot_3, on_spot_4, on_spot_5, on_spot_6, on_spot_7, on_spot_8, on_spot_9)
        
        if STATE == "block_7":
            draw_button( blink_1, blink_2, blink_3, blink_4, blink_5,blink_6, blink_7, blink_8, blink_9, this_x, this_y, this_x_1, this_y_1, this_x_2, this_y_2, this_x_3, this_y_3, this_x_4, this_y_4,
                            this_x_5, this_y_5, this_x_6, this_y_6, this_x_7, this_y_7, this_x_8, this_y_8, block_w, block_h, on_spot_1, on_spot_2, on_spot_3, on_spot_4, on_spot_5, on_spot_6, on_spot_7, on_spot_8, on_spot_9)
        
        if STATE == "block_8":
            draw_button( blink_1, blink_2, blink_3, blink_4, blink_5,blink_6, blink_7, blink_8, blink_9, this_x, this_y, this_x_1, this_y_1, this_x_2, this_y_2, this_x_3, this_y_3, this_x_4, this_y_4,
                            this_x_5, this_y_5, this_x_6, this_y_6, this_x_7, this_y_7, this_x_8, this_y_8, block_w, block_h, on_spot_1, on_spot_2, on_spot_3, on_spot_4, on_spot_5, on_spot_6, on_spot_7, on_spot_8, on_spot_9)
        
        if STATE == "block_9":
            draw_button(blink_1, blink_2, blink_3, blink_4, blink_5,blink_6, blink_7, blink_8, blink_9, this_x, this_y, this_x_1, this_y_1, this_x_2, this_y_2, this_x_3, this_y_3, this_x_4, this_y_4,
                            this_x_5, this_y_5, this_x_6, this_y_6, this_x_7, this_y_7, this_x_8, this_y_8, block_w, block_h, on_spot_1, on_spot_2, on_spot_3, on_spot_4, on_spot_5, on_spot_6, on_spot_7, on_spot_8, on_spot_9)
        
        if STATE == "wait_for_response":
            draw_button( blink_1, blink_2, blink_3, blink_4, blink_5,blink_6, blink_7, blink_8, blink_9, this_x, this_y, this_x_1, this_y_1, this_x_2, this_y_2, this_x_3, this_y_3, this_x_4, this_y_4,
                            this_x_5, this_y_5, this_x_6, this_y_6, this_x_7, this_y_7, this_x_8, this_y_8, block_w, block_h, on_spot_1, on_spot_2, on_spot_3, on_spot_4, on_spot_5, on_spot_6, on_spot_7, on_spot_8, on_spot_9)
            draw_next()
            
        if STATE == "stop":
            draw_goodbye(score)
            draw_button2(mouse, on_spot)
        
        
        if STATE == "quit":
            pygame.quit()
            sys.exit()
        
        
        pygame.display.update()
        
      
def draw_welcome():
    text_surface = font.render("Corsi Block Tapping Task", True, col_black, BACKGR_COL)
    text_rectangle = text_surface.get_rect()
    text_rectangle.center = (SCREEN_SIZE[0]/2.0,150)
    screen.blit(text_surface, text_rectangle)
    text_surface = font_small.render("Press Spacebar to start", True, col_black, BACKGR_COL)
    text_rectangle = text_surface.get_rect()
    text_rectangle.center = (SCREEN_SIZE[0]/2.0,400)
    screen.blit(text_surface, text_rectangle)
    
def draw_explanation():
    text_surface = font.render("Corsi Block Tapping Task", True, col_black, BACKGR_COL)
    text_rectangle = text_surface.get_rect()
    text_rectangle.center = (SCREEN_SIZE[0]/2.0,150)
    screen.blit(text_surface, text_rectangle)
    text_surface = font_xsmall.render("The Corsi Block-Tapping Test is a psychological test that assesses visuo-spatial short", True, col_black, BACKGR_COL)
    screen.blit(text_surface, (100, 260))
    text_surface = font_xsmall.render("term working memory. The test involves mimicking a computer generated sequence of ", True, col_black, BACKGR_COL)
    screen.blit(text_surface, (100, 290))
    text_surface = font_xsmall.render("up to nine identical spatially separated blocks. The sequence starts out simple with", True, col_black, BACKGR_COL)
    screen.blit(text_surface, (100, 320))
    text_surface = font_xsmall.render("just two blocks, but becomes more complex until you are no longer able to remember", True, col_black, BACKGR_COL)
    screen.blit(text_surface, (100, 350))
    text_surface = font_xsmall.render("the sequence. This results in the so called Corsi Score.", True, col_black, BACKGR_COL)
    screen.blit(text_surface, (100, 380))
    screen.blit(image, (400,425))   
    text_surface = font_xsmall.render("press Spacebar to start", True, col_black, BACKGR_COL)
    text_rectangle = text_surface.get_rect()
    text_rectangle.center = (SCREEN_SIZE[0]/2.0,630)
    screen.blit(text_surface, text_rectangle)


def show_ready():
    text_surface = font_small.render("Ready?", True, col_black, BACKGR_COL)
    text_rectangle = text_surface.get_rect()
    text_rectangle.center = (SCREEN_SIZE[0]/2.0, SCREEN_SIZE[1]/2.0)
    screen.blit(text_surface, text_rectangle)


def draw_goodbye(score):
    text_surface = font_xsmall.render("Close the application or try again!", True, col_black, BACKGR_COL)
    text_rectangle = text_surface.get_rect()
    text_rectangle.center = (SCREEN_SIZE[0]/2.0, SCREEN_SIZE[1]/2.0)
    screen.blit(text_surface, text_rectangle)
    
    text_surface = font_small.render("Your Corsi Score is  %s" % score, True, col_black, BACKGR_COL)
    text_rectangle = text_surface.get_rect()
    text_rectangle.center = (SCREEN_SIZE[0]/2.0, SCREEN_SIZE[1]/3.0)
    screen.blit(text_surface, text_rectangle)


def pick_coordinates_x(a):
    
    random_number = random.choice(a)
    a.remove(random_number)
    return random_number
    

def pick_coordinates_y(b):
    
    random_number_1 = random.choice(b)
    b.remove(random_number_1)
    return random_number_1
 

def pick_blocks(sequence_length, blocks):

    x = 0
    while x < sequence_length:
        random_number = random.choice(blocks)
        trial.append(random_number)
        blocks.remove(random_number) #avoids duplicates
        trial.sort() #block numbers in ascending order so they all execute during the states
        x += 1
    
def draw_button( blink_1, blink_2, blink_3, blink_4, blink_5,blink_6, blink_7, blink_8, blink_9, this_x, this_y, this_x_1, this_y_1, this_x_2, this_y_2, this_x_3, this_y_3, this_x_4, this_y_4,
                this_x_5, this_y_5, this_x_6, this_y_6, this_x_7, this_y_7, this_x_8, this_y_8, block_w, block_h, on_spot_1, on_spot_2, on_spot_3, on_spot_4, on_spot_5, on_spot_6, on_spot_7, on_spot_8, on_spot_9):
   
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


    pygame.draw.rect(screen, color_1, (this_x, this_y, block_w, block_h))
    pygame.draw.rect(screen, color_2, (this_x_1, this_y_1, block_w, block_h))
    pygame.draw.rect(screen, color_3, (this_x_2, this_y_2, block_w, block_h))
    pygame.draw.rect(screen, color_4, (this_x_3, this_y_3, block_w, block_h))
    pygame.draw.rect(screen, color_5, (this_x_4, this_y_4, block_w, block_h))
    pygame.draw.rect(screen, color_6, (this_x_5, this_y_5, block_w, block_h))
    pygame.draw.rect(screen, color_7, (this_x_6, this_y_6, block_w, block_h))
    pygame.draw.rect(screen, color_8, (this_x_7, this_y_7, block_w, block_h))
    pygame.draw.rect(screen, color_9, (this_x_8, this_y_8, block_w, block_h))
     
    
def draw_next():
    
        text_surface = font_small.render("press the spacebar when done", True, col_black, BACKGR_COL)
        text_rectangle = text_surface.get_rect()
        text_rectangle.center = (SCREEN_SIZE[0]/2.0, SCREEN_SIZE[1] - 20)
        screen.blit(text_surface, text_rectangle)
    
def draw_feedback(correct): 
    
    if correct:
       
        text_surface = font_small.render("Correct!", True, col_black, BACKGR_COL)
        text_rectangle = text_surface.get_rect()
        text_rectangle.center = (SCREEN_SIZE[0]/2.0, SCREEN_SIZE[1]/2.0)
        screen.blit(text_surface, text_rectangle)
        
    else:
      
        text_surface = font_small.render("Incorrect", True, col_black, BACKGR_COL)
        text_rectangle = text_surface.get_rect()
        text_rectangle.center = (SCREEN_SIZE[0]/2.0, SCREEN_SIZE[1]/2.0)
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
        
        
