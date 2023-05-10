import pygame
from djitellopy import tello
from time import sleep
from pygame.locals import *

def init():
    pygame.init()
    window = pygame.display.set_mode((400,400))

def getKey(keyName):
    ans = False
    for eve in pygame.event.get(): pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame,'K_{}'.format(keyName))
    if keyInput[myKey]:
        ans = True
    pygame.display.update()
    return ans

def getKeyboardInput():
    #左右，前后，上下，旋转
    lr,fb,ud,yv = 0,0,0,0
    speed = 50
    if getKey("LEFT"): yv = -speed
    elif getKey("RIGHT"): yv = speed

    if getKey("UP"): ud = speed
    elif getKey("DOWN"): ud = -speed

    if getKey("w"): fb = speed
    elif getKey("s"): fb = -speed

    if getKey("a"): lr = -speed
    elif getKey("d"): lr = speed

    if getKey("q"):me.land()
    if getKey("e"):me.takeoff()

    return [lr,fb,ud,yv]

def run():
    while True:
        vals = getKeyboardInput()
        me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
        sleep(0.05)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
