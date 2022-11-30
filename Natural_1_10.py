#Natural no 1-10
i=1
while(i<=10):
    print(i)
    i=i+1

#print 1 to n
n=int(input("Enter no:"))
i=1
while(i<=n):
    print(i)
    i=i+1

#Natural no 1-10 Reverse order
i=10
while(i>=1):
     print(i)
     i=i-1

#print 1 to n
n=int(input("Enter no:"))
i=10
while(i>=n):
    print(i)
    i=i-1

#FIND SUM 1 to 10
n=int(input("Enter the number"))
i=1
sum=0
while(i<=n):
    sum=sum+i
    i=i+1
    print(i)
print("Sum",sum)

#Sum of Square 1 to n
n=int(input("Enter the number:"))
i=1
sum=0
while(i<=n):
    sum=sum+(i*i)
    i=i+1
    print(i)
print("Sum",sum)

#Even number between 1 to 10
n=int(input("Enter the no.:"))
i=2
while(i<=n):
    print(i)
    i=i+2

n=int(input("Enter the no.:"))
i=1
while(i<=n):
    if i%2==0:
        print(i)
    i=i+1    

#sum of even no. 1 to 10
n=int(input("Enter the no.:"))
i=1
sum=0
while(i<=n):
    if i%2==0:
        sum=sum+i
    i=i+1  
print("Sum:",sum)  

#Find sum of n even number
n=int(input("Enter the no.:"))
i=1
sum=0
count=0
while(count<n):
    if i%2==0:
        sum=sum+i
        count=count+1
    i=i+1
print("Sum of even no:",sum)