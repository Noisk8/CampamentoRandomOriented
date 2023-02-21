
var.switch = var([1,1],[32])


p8 >> glass(oct=6, rate=linvar([-2,2],16), shape=0.5, amp=1, amplify=var([1,var.switch],64), room=0.5)



b1 >> dirt([0,0,0.5], dur=PDur(5,8), sus=.4, amp=1, chop=.5, drive=0.2, formant=1, oct=(5), room=0.2).spread()

p3 >> pasha (var([0,2,0.5],[3,1/2,1/2]), dur=PDur(5,8), amp=1, oct=5, sus=2, pan=PWhite(-1,1)).every(4, "dur.shuffle")

n2 >> play ("[--]", amp=2, sample=0)

nk >> play ("|x4| ", amp=0.7, dur=PDur(4,8))

c1 >> play (" |o2|", dur=2/2, amp=.7)

ce >> play (" |o3|", dur=2/2, delay=4, mix=.6, room=.5, amp=2)
