#Leap year program:
'''year=int(input("enter the year:"))
if (year%4==0 and year%100!=0)or(year%400==0):
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")'''
#largest number between two num
'''a,b=4,5
if a>b:
    print(f"{a} is greater than {b}")
else:
    print(f"{b} is greater than {a}")'''
#prime number
'''import math

n = 5
prime = True

if n > 1:
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            prime = False
            break
else:
    prime = False

if prime:
    print(f"{n} is prime")
else:
    print(f"{n} is not prime")'''

#composite number
'''n=6
composite=True
if n>1:
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            composite=False
            break
else:
    composite=False
if composite:
    print("not composite")
else:
    print("composite")'''

#happy number
'''n=19
s=set()
while n!=1 and n not  in s:
    s.add(n)
    n=sum(int(digit)**2 for digit in str(n))
if n==1:
    print("happy number")
else:
    print("not happy")'''

# largest number between three number
'''a,b,c=1,2,3
if a>b and a>c:
    print("a is greater")
elif b>a and b>c:
    print("b is greater")
else:
    print("c is greater")'''
# check wheather give alphabet is character or not
'''n='s'
if ord(n) in range(65,91):
    print("alphabet")
elif ord(n) in range (90,123):
    print(" alphabet")
else:
    print("not alphabet")'''
#check wheather given number is number or not
'''n='7'
if 'A'<=n<='Z' or 'a'<=n<='z':
    print("alphabets")
else:
    print("not alphabets")'''
#
'''n=10
if 0<=n<=9:
    print("num")
else:
    print("not num")'''
# check wheather specia; char or not
'''n='a'
if ('A'<=n<='Z'or 'a'<=n<='z' or 0<=n<=9):
    print("is not special char")
else:
    print("special char")'''
# check wheather the given number is char or number or special charcter.
'''n='@'
if ('A'<=n<='Z'or 'a'<=n<='z'):
    print("is alpha char")
elif '0'<=n<='9':
    print("num")
else:
    print("special char")'''

# fizzbuzz program that num div by 3 or 5 and (3,5)
'''n=10
if n%5==0 and n%3==0:
    print("fizzbuzz")
elif n%3==0:
    print("buzz")
elif n%5==0:
    print("fizz")
else:
    print("not valid input")'''
# Marks of students:
'''n=40
if n in range (85,100):
    print("A grade")
elif n in range (70,85):
    print("B grade")
elif n in range(60,70):
    print("C grade")
elif n in range(50,60):
    print("d grade")
else:
    print("fail")'''

# if nested loops:

# login in authentication
'''user_name='dinesh'
pass_word='dinesh@123'
u=input("enter the username:")
if u==user_name:
    p=input("enter the password:")
    
    if p==pass_word:
        print("login sucessful")
    else:
        print("not correct credentials")
else:
    print("invalid username")'''


#STUDENTS HAVE TO SCORE IN MORE THAN 35 IN EACH SUBJECT AND TOTAL MORE THAN 150
'''A=40
B=35
C=35
D=45
total=A+B+C+D
if A>=35 and B>=35 and C>=35 and D>=35:
    if total>=150:
        print("pass")
        print(f"{total}")
    else:
        print("fail")
else:
    print("fail")'''

#or
'''A=40
B=35
C=35
D=45
if A>35:
    if B>35:
        if C>35:
            if D>35:
                if A+B+C+D>150:
                    print("pass")
                else:
                    print("fail")
            else:
                print("fail in d")
        else:
                print("fail in c")
    else:
                print("fail in b")
else:
                print("fail in a")'''

                       # or
'''a=80
b=70
c=35
d=35
total=a+b+c+d
mark=True
if a<35:
       print("failed in a")
       mark=False
if b<35:
       print("failed in b")
       mark=False
if c<35:
       print("failed in c")
       mark=False
if d<35:
       print("failed in d")
       mark=False
if total<150:
       print("failed in total")
if mark==True:
       print("pass")
else:
       print("fail")'''

#ATM MONEY WITHDRAW
'''pin=0000
bal=10000
withdraw=2000
if int(input("enter the pin:"))==pin:
       if bal>0 and withdraw<bal:
           result=bal-withdraw
           print(f"{withdraw} amount is debit")
           print(f"{result} is balance")
       else:
        ("Invalid amount or check the balance")
else:
    print("invalid pin")'''
    
       #loops
# while loop:
# write a helloworld program upto n times:


'''mes=1
while mes<=5:
       print("hello! world")
       mes+=1'''


# print 1 to 10 numbers
'''
num=1
while num<=10:
       print(num)
       num+=1'''
# sum of n numbers:
'''n=10
i=1
s=0
while i<=n:
    s+=i
    i+=1
print("sum of first:",n, "total is",s)'''

#factorial
'''n=5
i=1
fact=1
while i<=n:
    fact=fact*i
    i+=1
print(fact)'''

#sum of number:
'''n=1234
s=0
while n>0:
    num=n%10
    s+=num
    n=n//10
print(s)'''


       
       
