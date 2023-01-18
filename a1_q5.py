number=int(input("enter number:"))
count=0
while number>0:                                                         #q5
    d=number%10
    count+=1
    number=number//10
print(count)
