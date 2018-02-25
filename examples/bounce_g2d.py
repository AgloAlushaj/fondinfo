#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import game2d as g2d

from bounce import Arena, Ball, Ghost, Turtle


def update():
    arena.move_all()  # Game logic

    g2d.fill_canvas((255, 255, 255))
    for a in arena.actors():
        g2d.draw_image_clip(sprites, a.rect(), a.symbol())    

def keydown(code):
    #print(code + " dn")
    if code == "ArrowUp":
        turtle.go_up()
    elif code == "ArrowDown":
        turtle.go_down()
    elif code == "ArrowLeft":
        turtle.go_left()
    elif code == "ArrowRight":
        turtle.go_right()

def keyup(code):
    #print(code + " up")
    turtle.stay()

def main():
    global arena, turtle, sprites

    arena = Arena(320, 240)
    Ball(arena, 40, 80)
    Ball(arena, 80, 40)
    Ghost(arena, 120, 80)
    turtle = Turtle(arena, 80, 80)

    g2d.init_canvas(arena.size())
    sprites = g2d.load_image("sprites.png")

    g2d.handle_keyboard(keydown, keyup)
    g2d.main_loop(update, 1000 // 30)
    
main()