#find sum of digit given number - 243=2+4+3=9
i=int(input("Enter the no:"))
sum=0
while(i>0):
    sum=sum+i%10
    i=i//10
print("Sum:",sum)

#find sum of square of digit given number - 243=2_4_3=4+16+9=29
i=int(input("Enter the no:"))
sum=0
while(i>0):
    sum=sum+(i%10)*(i%10)
    i=i//10
print("Sum:",sum)

#find sum of cube of digit given number - 243=2_4_3=8+64+27=83
i=int(input("Enter the no:"))
sum=0
while(i>0):
    sum=sum+(i%10)*(i%10)*(i%10)
    i=i//10
print("Sum:",sum)
