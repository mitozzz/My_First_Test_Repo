k = 0
for i in range(800000,850000):
    dl = []
    for j in range(2,i-1):
        if i % j == 0:
            dl.append(j)
    if len(dl) > 1:
        hatat = max(dl) + min (dl)
        if hatat % 138 == 0:
            print(i, hatat)
            k+=1
            if k == 5:
                break

