#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

from game2d import *
from random import randrange

def draw_tile(color: (int, int, int), pos: (int, int)):
    x, y = pos
    draw_rect(color, (x * TILE, y * TILE, TILE - 1, TILE - 1))

def keydown(code):
    global player
    if player != monster and player != gold:
        draw_tile(color_old, player)
        x, y = player
        if code == "ArrowUp" and y > 0:
            player = x, y - 1
        elif code == "ArrowLeft" and x > 0:
            player = x - 1, y
        elif code == "ArrowDown" and y < H - 1:
            player = x, y + 1
        elif code == "ArrowRight" and x < W - 1:
            player = x + 1, y

        if player == monster:
            draw_tile(color_monster, player)
            alert('Monster!')
        elif player == gold:
            draw_tile(color_gold, player)
            alert('Gold!')
        else:
            draw_tile(color_now, player)

color_now = (0, 0, 0)
color_old = (127, 127, 127)
color_gold = (0, 255, 0)
color_monster = (255, 0, 0)

W, H = 5, 5
TILE = 20
canvas_init((W * TILE, H * TILE))

player = 0, 0
monster = player
while monster == player:
    monster = randrange(W), randrange(H)
gold = player
while gold == player or gold == monster:
    gold = randrange(W), randrange(H)    
print('Monster:', monster)
print('Gold:', gold)
draw_tile((0, 0, 0), player)

handle_keyboard(keydown, None)
