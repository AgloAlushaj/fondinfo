#!/usr/bin/env python3
'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import game2d

grays = []
val = int(input('gray? '))
while 0 <= val < 256:
    grays.append(val)
    val = int(input('gray? '))

m = int(input('repetitions? '))

side = 400.0
delta = side / (len(grays) * m)

game2d.canvas_init((int(side), int(side)))

for i in range(m):
    for val in grays:
        game2d.draw_rect((val, val, val),
                         (0, 0, int(side), int(side)))
        side -= delta
