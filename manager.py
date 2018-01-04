import pygame
import numpy
from items import Block,Node
import random


class Manager:
    def __init__(self, node_cap,block_cap):
        self.nodes = [None] * node_cap
        self.blocks = [None] * block_cap


    def populateBlocks(self):
        for i in range(len(self.blocks)):
            width = random.randrange(100, 200)
            height = random.randrange(100, 200)
            xpos = random.randrange(0,1280 - width)
            ypos = random.randrange(0,640 - height)
            print 'Blocks created with dimensions w: %d h: %d' % (width,height)
            self.blocks[i] = Block(xpos,ypos,width,height)

    def testing(self):
        for i in range (len(self.blocks)):
            print self.blocks[i].get_rect()
    #Todo, each node should check if it's inside a block before being generated
    def populateNode(self):
        for i in range(len(self.nodes)):
            print"hold"



