num=int(input("enter number:"))                                     #q7  
new_num=0
cnt=len(str_)
for i in str_:
    k=int(i)
    new_num=new_num+cnt*10**(k-1)      # k-1 is position of the digit in the new number
    cnt-=1
    print(k,cnt)
print(new_num)
