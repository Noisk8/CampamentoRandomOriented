p1 >> play('ff{lt}',
    rate=P[1, 1, 1, var([1, 0.85], 8),  1, var([1, 1.15, 0.9], 32), 1, 1] * var([1, 2, 1, 1.5], [[64, 32]]),
    pan=PWhite(-0.5, 0.5),
    room=PRand([1, 0.5, 0.25, 0.75]), mix=0.1,
    cut=0.5,
    drive=P[0.15, 0.25, var([0, 0.1, 0.2, 0.3], [32, 8]), var([0, 0.2], 16)] * var([1, 0.5, 1.25], [8, 4]),
    slide=P[1, 0.75, 1, 0.25], sus=1, chop=[[4, var([4, 2], [128, 64])], 4, 4, var([4, 2], 64)],
    dur=P[var([0.25, 0.5], [56, 8]), 0.25, 0.25],
)



var.kamp = var([1, 0], [28, 4])
k1 >> play('X', rate=P[1, 0.98, 1, 0.95], dur=1, hpf=P[80, 85, 80, 79], hpr=0.25, amp=var([1.5, 0], [256, 64]) * var.kamp)


k2 >> play('X', sample=1, dur=0.25, delay=0, amp=P[0, P[var([0.25, 0.75], [128, 64, 32, 32]), 0.25], P[0.5, var([0.5, 0, 0.25, 0.75, 0], 64)], 0.75] * (k1.amp * 0.85) * var.kamp)

h1 >> play('-', sample=2, dur=1, delay=0.5, amp=var([1.5, 0], [128, 64, [64, 128], 32]))

rc >> play('~', pan=PWhite(-0.5, 0.5), dur=0.25, amp=expvar([0, 0, 1], [[32, 64, 128], 64, 0]) * 2.5)

bs >> bass(dur=0.25, sus=1, chop=var([4, 2], [56, 8]), drive=var([0.15, 0.3], [28, 4]),
    hpf=P[var([400, 600, 800, 200], 32), P[var([800, 200], 64), 200], var([200, 400, 600, 800], [32, 16]), expvar([200, 600], [32, 0])],
    hpr=0.25, amp=var([1, 1], [256, 128, 128, 64, 64, 32])
)

rs >> play('u', sample=1, room=1, mix=0.25, dur=2, amp=var([0, 2], [[32, 64], 32, 64, 128]))

