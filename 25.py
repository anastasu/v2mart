for i in range(289123456,389123456+1):
    k=0
    d=2
    maxd=0
    if int(i**0.5) == i**0.5:
        while d * d < i:
            if i%d == 0:
                k += 2
                if maxd == 0:
                    maxd = i // d
            d += 1
        if k == 2:
            print(maxd)


