num=int(input("enter number:"))
half=num//2                                      #q3
for i in range(2,half,1):
    if num%i == 0:
        print("Not prime")
        break
else:
        print("prime")
