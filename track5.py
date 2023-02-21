p1 >> keys(([3,4,5,4],7,[9,9,9,10]), dur=PDur(5,8), spin=8, tremolo=4, room=1, amp=4)

p5 >> keys(([3,4,5,4],7,[9,9,9,10]), dur=PDur(8,8), spin=8, tremolo=2, oct=var([7,6]), room=1, amp=3)

p3 >> dirt((P[0,0,-1,0,-2,0,0,-2,-1,0]), dur=PDur(5,8), sus=1, oct=5, amp=1.2)


cr >> play("#", dur=32, room=1, amp=2).spread()

c1 >> play("#", rate=-1/2, hpf=1000, dur=4, amp=4, room=1, coarse=16).spread()

jk >> play (" |o2|", amp=1, dur=2/2, mix=.5, room=.6)


c8 >> play("@", dur=1/4, sample=P[:8].rotate([0,1,3]), rate=4, pan=-0.5)


bu >> play ("|x4| ")



