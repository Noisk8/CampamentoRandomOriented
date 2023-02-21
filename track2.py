k3 >> play (" |o0|", dur=2/2, amp=1, hpf=100)
k4 >> play ("[|o0||o0|]", dur=1/2, amp=1, hpf=3000)

k5 >> dbass (dur=PDur(5,8).reverse(),  pan=(1,-1), amp=.6, formant=0)

k6 >> star (P[5,7,8,5,4,8,0].reverse(),dur=PDur(8,8)*1, pan=(1,-1), oct=5, amp=1)+0
      
nk >> play ("|x4| ", amp=0.7, dur=PDur(4,8))

y1 >> keys(
    dur=PDur(8,8),
    amp=[3,2,4,1],oct=(7,6),
    drive=0.3,
    sus=linvar([0.4,0.1],8),
    formant=linvar([0.5,2],4),
    room=0.7,
    mix=0.7,
    hpf=3500,
    pan=[0,[1,-1]]
    )
