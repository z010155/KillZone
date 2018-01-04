import pygame


class Item:
    def __init__(self,xpos,ypos):
        self.xpos = xpos
        self.ypos = ypos



class Block:
    def __init__(self,xpos,ypos,width,height):
        #Item.__init__(self,xpos,ypos)
        self.rect = (xpos,ypos,width,height)
        self.xpos = xpos
        self.ypos = ypos

    def get_rect(self):
        return self.rect

class Node:
    def __init__(self,xpos,ypos,held):
    #held is enumeration for who is holding the node. Where is Enumeration base library?????
        self.rect = (xpos,ypos,8,8) # 8 is diameter of circle hopefully
        self.xpos = xpos
        self.ypos = ypos
        self.held = held



        
        