#Check odd and even
a=int(input("Enter number to check: "))
if(a%2==0):
    print("The number is Even")
else:
    print("The number is odd")

#Check Age 18+ the vote right
a=int(input("Enter your age: "))
if(a>=18):
    print("Eligible to vote")
else:
    print("Not Eligible to vote")

#Max between two no.
a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
if a>b:
    print("1st max number")
else:
    print("2nd max number")

#Max between three no.
a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
c=int(input("Enter 3rd number: "))
if a>b and a>c:
    print("1st max number")
elif b>a and b>c:
    print("2nd max number")
else:
    print("3rd max number")

#Given no. positive,negative or zero
a=int(input("Enter your number: "))
if a>0:
    print("Your number positive")
elif a<0:
    print("Your number negative")
else:
    print("Your number zero")

#Middle no. in group three
a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
c=int(input("Enter 3rd number: "))
if (a>b and a<c) or (a<b and a>c):
    print("1st middle number")
elif (b>a and b<c) or (b<a and b>c):
    print("2nd middle number")
else:
    print("3rd middle number")

#5 subject , total,percentage,grade
a=int(input("Enter math number: "))
b=int(input("Enter hist number: "))
c=int(input("Enter geo number: "))
d=int(input("Enter eng number: "))
e=int(input("Enter chem number: "))
total=a+b+c+d+e
percentage=(total/500)*100
print("Total Marks=",total,"Percentage=",percentage)
if percentage>=80:
    print("You have got grade A")
elif percentage>=60:
    print("You have got grade B")
elif percentage>=40:
    print("You have got grade C")
else:
    print("You have got grade D")

