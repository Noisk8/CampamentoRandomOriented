#Noisk8 \ Medellín / Colombia 



#Intro 
d3 >> jbass(P[0, 2, 3, 5, 7, 8], dur=1/2, lpf=expvar([1000, 5000], 8),
            amp=1/2, oct=4, sus=2, slide=1/2) + (P[0, 2, 3, 5, 7, 8] + 2).every(4, "stutter")


d1 >> dirt([0, 2, 3, 5], oct=6,dur=1/4, amp=expvar([1, 0.3], 1/3)) 

d2 >> pasha([0, 2, 3, 5], dur=1/4, amp=expvar([0.5, 0.3], 0.5/3)) + (0, 7, 3, 5)

d1.stop()

d2.stop()

d3.stop()

nk >> play ("|x4| ", amp=0.8, dur=PDur(4,8))
n1 >> play (" [--]", amp=3)
n2 >> play ("[--]", amp=2, sample=2)

k3 >> play (" |o2|                    |o2|              [|o2||o2|]            ", dur=2/2, amp=1, hpf=600)
