import pygame
import sys
import note
import random
import record_note
from pygame.locals import *

pygame.init()




#Variables
speed = 2               #Set speed of moving notes
x_vline = 100           #Set where end point is
speed_repeat = 50      #Set repeat speed

#Load images
screen = pygame.display.set_mode((640, 213))
background = pygame.image.load('images/treble640x213.png').convert()
note_image = pygame.image.load('images/note100.png').convert_alpha()
vline_image = pygame.image.load('images/vline.png').convert_alpha()

#Init
screen.blit(background, (0, 0))
notes = []
heights = {78: 'D4', 65: 'E4',52: 'F4',38: 'G4',24: 'A4',10: 'B4'}
count = 0

rec = record_note.Threading()  #activate threaded recording
recorded_note = 'none'

while 1:

    if (count % speed_repeat) == 0:
        # print('count: ' + str(count))

        picked_height = random.choice(list(heights.keys())) #Make random note
        o = note.note(note_image, picked_height, speed) # TODO remove speed?
        notes.append(o)
        # print('Note: ' + str(heights[picked_height]))

    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()

    screen.blit(background, (0, 0))    #Redraw background
    screen.blit(vline_image, (x_vline, 0))


    for o in notes:
        o.xpos -=  speed
        screen.blit(o.image, (o.xpos,o.ypos))
        if o.xpos < x_vline-20:
            print('Game Over')
            sys.exit()

    # recorded_note = 'none'
    recorded_note = rec.note
    # if (count % 100) == 0:
    #     recorded_note = input("Please enter something: ")
    #
    # print('rec: ' + recorded_note)


    if len(notes) > 0:
        current_note = heights[notes[0].ypos]
        if current_note == recorded_note:
            print('done')
            del notes[0]
            current_note = 'none'

    end = 1






    # print(current_note)




    pygame.display.update()
    pygame.time.delay(100)
    count = count + 1