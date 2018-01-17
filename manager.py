import pygame
import numpy
from items import Block,Node
import random


class Manager:
    def __init__(self, node_cap,block_cap):
        # self.nodes = [None] * node_cap
        # self.blocks = [None] * block_cap
        self.nodes = [Node(0, 0, 0, 0, 0)] * node_cap
        self.blocks = [Block(0, 0, 0, 0)] * block_cap


    def populateBlocks(self):
        for i in range(len(self.blocks)):
            if self.blocks[i] == Block(0,0,0,0):
                placed = False
                while (not placed):
                    width = random.randrange(100, 200)
                    height = random.randrange(100, 200)
                    xpos = random.randrange(0, 1280 - width)
                    ypos = random.randrange(0, 640 - height)
                    proposed_rect = pygame.Rect(xpos,ypos,width,height)
                    for j in range(len(self.blocks)):
                        if not proposed_rect.colliderect(self.blocks[j]):
                            self.blocks[i] = Block(xpos,ypos,width,height)
                            placed = True
                            print 'Blocks created with dimensions w: %d h: %d and position x: %d y: %d' % (width, height,xpos,ypos)
                            break

    def testing(self):
        for i in range (len(self.blocks)):
            print self.blocks[i].get_rect()

    def populateNode(self):
        for i in range(len(self.nodes)):
            for j in range(len(self.blocks)):
                placed = False
                width = 8
                height = 8
                while (not placed):
                    xpos = random.randrange(0, 1280 - width)
                    ypos = random.randrange(0, 640 - height)
                    planned_rect = pygame.Rect(xpos,ypos,width,height)
                    if not self.blocks[j].rect.colliderect(planned_rect):
                        print 'Node created with dimensions w: %d h: %d' % (width, height)
                        self.nodes[i] = Node(xpos, ypos, width, height, 0)
                        placed = True




