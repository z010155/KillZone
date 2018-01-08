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

    def populateNode(self):
        for i in range(len(self.nodes)):
            for j in range(len(self.blocks)):
                width = 8
                height = 8
                xpos = random.randrange(0, 1280 - width)
                ypos = random.randrange(0, 640 - height)
                #TODO the Node needs to be given a HELD enumeration still
                self.nodes[i] = Node(xpos,ypos,width,height,0)
                if self.blocks[j].rect.colliderect(self.nodes[i].rect):
                    print "COLLISION"




