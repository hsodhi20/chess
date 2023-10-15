"""
Main driver file.
#Responsible for hadling user input and displaying the current GameState
"""
import pygame as p
from Chess import ChessEngine

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = 15  #for animation later on
IMAGES = {}

"""
initialise a global dictionary of images. 
will be called only once
"""

def loadImages():
    pieces = ['wP', 'wR', 'wN', 'wB', 'wQ', 'wK', 'bP', 'bR', 'bN', 'bB', 'bQ', 'bK']
    for piece in pieces:
        IMAGES[pieces] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE,SQ_SIZE)) 

"""
The main driver for our code. This will handle user input and updating graphics
"""
def main():
    p.init()
    screen = p.display.set_mode(WIDTH,HEIGHT)
    clock = p.time.Clock()
    screen.fill(p.color("white"))
    gs = ChessEngine.GameState()
    print(gs.board)

main()