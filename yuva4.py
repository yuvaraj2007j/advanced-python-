year=int(input("enter the year:"))
if year%4==0 and year%100!=0:
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")
""
sum=(input("enter a number:"))
total=0
for i in sum:
    total=total+int(i)  
print("sum of digits is:",total)
""
age=int(input("enter your age:"))
if age>=18:
    print("you are eligable to vote")
else:
    print("you are not eligable to vote")
""
def fact(n):
   if(n==1 or n==0):
       return 1
   else:
        return(n*fact(n-1))
num=int(input("enter the nuber:"))
print("factorial value is:",fact(num))
""
num=int(input("enter the nuber:"))
temp=num
sum=0       
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
if num==sum:
    print(num,"is an armstrong number") 
else:
    print(num,"is not an armstrong number")
    ""
a,b=0,1
n=int(input("enter the range:"))
for i in range(n):
    print(a)
    a,b=b,a+b
