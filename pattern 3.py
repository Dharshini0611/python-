n=8
m=0
for k in range(n,0,-1):
    m+=1
    for n in range(1,k+1):
        print(m,end="")
    print("")