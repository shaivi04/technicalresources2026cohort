num=int(input("Enter range:"))

print("Prime numbers:",end=' ')

for i in range (2,num+1):
    chk = True
    k = 2
    while k<i:                                              #q4
        if i%k == 0:
            chk = False
        k += 1
    if chk:
        print(i,end=' ')
     
