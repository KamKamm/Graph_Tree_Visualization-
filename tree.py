from django.conf import _DjangoConfLazyObject
import pygame
pygame.init()

# Window dimension 
width=800
height=600

# Create the pygame window 
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("Binary Tree")

# Define the node structure 

class Node:
    def __init__(self,value):
        self.value =value
        self.left=None
        self.right=None