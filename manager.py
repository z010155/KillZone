import pygame
import numpy
from items import Block,Node
import random


class Manager:
    def __init__(self, node_cap,block_cap):
        self.nodes = [None] * node_cap
        self.blocks = [None] * block_cap
        self.is_full = False


    def populateBlocks(self):
        for i in range(len(self.blocks)):
            xpos = random.randrange(0,1280)
            ypos = random.randrange(0,640)
            width = random.randrange(10,90)
            height = random.randrange(10,90)
            self.blocks[i] = Block(xpos,ypos,width,height)




