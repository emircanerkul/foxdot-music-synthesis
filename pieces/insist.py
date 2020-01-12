'''
Name of piece: Insist
Source of inspiration: Improvisation
Date of discovery: 12.01.2020 09:00 UTC+3
SoundCloud: https://soundcloud.com/emircanerkul/insist
'''

from FoxDot import *

p1 = Player("p1")
p2 = Player("p2")
p3 = Player("p3")
p4 = Player("p4")

p1 >> pads(P[1, 2, 3, 4, 5, 6, 5, 4, 3, 2].stutter([2, 3]), dur=[.5], amp=[0, 0.2, 0.3, 0.5, 0.8, 1])
p2 >> pluck([0, 2, 4], dur=[1, .5, .5], amp=0.35)
p3 >> play("(x[--])xo{-[--][-x]}", amp=0.55)
p4 >> blip([8, 2, 3, 4, 5], dur=[3, .5, .5, 4], sus=2, root=var([0, 2], 8), amp=0.75)

Go()
