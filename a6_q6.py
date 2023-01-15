number = int(input("enter number:"))
revnum=0
position = 1
while number>0:                                                               #q6
    
    digit = number%10                                                          #extracting last digit of number
    
    revnum=revnum*10+digit                                       
    
    number = number//10
    
print(revnum)
