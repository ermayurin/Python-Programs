#Assignment
a=6
b=2
print("Addition=",a+b)
print("Substraction=",a-b)
print("Multiply=",a*b)
print("Division=",a/b)
print("Modulus=",a%b)
print("Exponent=",a**b)
print("Floor Division=",a//b)
#---------------------------------------------

#Relation/Comparison
print("Greater than=",a>b)
print("Greater than equal to=",a>=b)
print("Less than=",a<b)
print("Less than equal to=",a<=b)
print("Equal to=",a==b)
print("Not equal to=",a!=b)
#---------------------------------------------

#Assignment
a+=b #a=a+b
print("Add and assign=",a)
a-=b #a=a-b
print("Sub and assign=",a)
a*=b #a=a*b
print("Mul and assign=",a)
a/=b #a=a/b
print("Div and assign=",a)
a%=b #a=a%b
print("Modulus and assign=",a)
#---------------------------------------------

#Logical Operators
#Logical AND
a=5
b=6
c=6
print((a>b)and(a>c))
#Logical OR
a=5
b=6
c=6
print((a>b)and(a>c))
#Logical NOT
a=5
b=6
c=6
print(not(a>c))
#---------------------------------------------

#Identity
x=5.5
print(type(x) is int) #is
print(type(x) is not int) #is not
#---------------------------------------------

#Membership
a=10
list=[1,2,3,5,10]
if(a in list): #in
    print("Yes a is present in list")
else:
    print("No a is present in list")



