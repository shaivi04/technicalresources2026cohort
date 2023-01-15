def findhcf(num1,num2):
    hcf = 1
    for i in range(1,num1+1):                                                    #q9
     
        if num1%i == 0 and num2%i == 0:
            hcf=i
    return hcf

num1=int(input("enter number 1:"))
num2=int(input("enter number 2:"))
print('HCF is',findhcf(num1,num2))
print('LCM is',num1*num2/findhcf(num1,num2))
