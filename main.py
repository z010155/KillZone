import pygame
import numpy as np
import argparse
from manager import Manager


if __name__ == "__main__":
    print "Initializing"

    #Arguement parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-n','--node', type=int, default = 20, help='Number of nodes to create on the screen. \n Maximum of 25')
    parser.add_argument('-b','--block', type=int, default = 6, help='Number of blocks to create on the screen. \n Maximum of 10')

    args = parser.parse_args()

    #Initializing pygame screen
    pygame.init()
    width,height = 1280,640
    screen = pygame.display.set_mode((width,height))
    screen_colour = (255,255,255) #White
    clock = pygame.time.Clock()
    clock.tick(60) #FPS
    terminate = False

    manager = Manager(args.node,args.block)
    manager.populateBlocks()
    manager.testing()
    while(not terminate):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate = True

        #Fill screen with colour
        #Make sure blip is after this
        screen.fill(screen_colour)


        for i in range(len(manager.blocks)):
            pygame.draw.rect(screen, (125, 125, 125), manager.blocks[i].rect)

        pygame.display.flip()
        pygame.display.update()
