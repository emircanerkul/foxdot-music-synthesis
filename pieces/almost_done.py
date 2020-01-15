'''
Name of piece: Almost Done
Source of inspiration: Improvisation
Date of discovery: 12.01.2020 09:00 UTC+3
SoundCloud: https://soundcloud.com/emircanerkul/almost-done
'''

from FoxDot import *

p1 = Player("p1")
p2 = Player("p2")
p3 = Player("p3")
p4 = Player("p4")

p1 >> pluck(P[0, 2, 0, 4].stutter(3), dur=1/4, amp=.20) + (0, 2, 4)
p2 >> pluck(P[0, 2, 0, 4].stutter(3), dur=1/2, slide=1, slidedelay=0.5, amp=.20) + (0, 2, 4)
p3 >> pluck([4, 2, 6, 4, 8, 6], dur=[4, 3/4, 3/2, 2], glide=[7, -7], amp=2)
p4 >> pasha(P[0, 2, 3, 4, 7, 9].stutter([1, 2, 3, 2, 1]), dur=1/4, amp=var([0.5, 1], 8))

Go()
