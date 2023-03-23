k = 0
for a in range(220000,320000):
    M = 0
    dl = []
    for i in range(2,a-1):
        if a % i == 0:
            dl.append(i)
    if len(dl) > 1:
        M = max(dl) + min(dl)
    if M % 10 == 4 and M > 0:
        print(a, M)
        k += 1
        if k == 5:
            break
        
            
    
        

    

