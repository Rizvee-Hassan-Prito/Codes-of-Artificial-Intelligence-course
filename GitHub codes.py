# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 02:30:52 2021

@author: User
"""

"""
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
"""
numbers=[]
for i in range(2000,3200):
    if(i%7==0 and i%5!=0):
        numbers.append(str(i))
print (','.join(numbers))

"""
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320
"""
fact=1
print()
ipt=int(input("Give a number:"))
for i in range(ipt,1,-1):
    fact=fact*i
print("Factorial:",fact)

"""
With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
"""
n=int(input("Give a number:"))
d=dict()
for i in range(1,n+1):
    d[i]=i*i
print("Dictionary:",d)

"""
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
"""
s=input()
l=[]
l=s.split(",")
print(l)
k=tuple(l)
print(k)

"""
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
"""

class stringPrinting(object):
    def __init__(self):
        self.st =""
    def getString(self):
        self.st = input()
    def printString(self):
        print(self.st.upper())
Obj = stringPrinting()
Obj.getString()
Obj.printString()

"""
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
"""
import math
C=50
H=30
D=input()
D2=[]
D2=D.split(",")
result=[]
for i in range(0,len(D2)):
    M=int(D2[i])
    Q=int(math.sqrt((2*C*M)/H))
    result.append(str(Q))
print(",".join(result))

"""
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 
"""
list1=[]
r=int(input("Enter row number:"))
c=int(input("Enter column number:"))
for i in range(0,r):
    list2=[]
    for j in range(0,c):
        list2.append(i*j)
    list1.append(list2)
print(list1)

"""
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world
"""
st1=input()
st1=st1.split(",")
st1.sort()
st2=",".join(st1)
print(st2)

"""
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT
"""

line = []
while True:
    l = input().upper()
    if l:
        line.append(l)
    else:
        break
for i in range(0,len(line)):
    print(line[i])

"""
Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world
"""
st=input()
st=st.split()
st1=list(set(st))
st1.sort()
print(" ".join(st1))


"""
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.

"""
line=input()
n=line.split(",")
l=[]
for i in range(0,len(n)):
    it=int(n[i],2)
    if it%5==0:
        l.append(str(it))
l=",".join(l)
print(l)

"""
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
"""
numbers=[]
for i in range(1000,3001):
        n=str(i)
        n.split()
        if(int(n[0])%2==0 and int(n[1])%2==0 and int(n[2])%2==0 and int(n[3])%2==0):
            numbers.append(n)
print(','.join(numbers))

"""
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
"""
st=input()
d=0;l=0
for i in range(0,len(st)):
    if st[i].isdigit():
        d+=1
    elif st[i].isalpha():
        l+=1
        
print("LETTERS ",l)
print("DIGITS ",d)

"""
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
"""
st=input()
u=0;l=0
for i in range(0,len(st)):
    if st[i].isupper():
        u+=1
    elif st[i].islower():
        l+=1
        
print("UPPER CASE ",u)
print("LOWER CASE ",l)

"""
Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9
"""
num=input()
n=num.split(',')
odd=[]
for i in range(0,len(n)):
    if(int(n[i])%2!=0):
        odd.append(n[i])
print(','.join(odd))

"""
Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500
"""
lines=[]
while True:
    ln=input()
    if ln:
        lines.append(ln)
    else:
        break
sum=0
for i in range(0,len(lines)):
    st=lines[i].split(" ")
    if(st[0]=="D"):
        sum+=int(st[1])
    elif (st[0]=="W"):
        sum-=int(st[1])
print(sum)

"""
A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1
"""
import re
ps=input()
pw=ps.split(',')
passwords=[]
for i in range(0,len(pw)):
    psw=pw[i]
    if len(psw)>=6 and len(psw)<=12:
        if not re.search( "[A-Z]", psw):
            continue
        elif not re.search( "[a-z]", psw):
            continue
        elif not re.search( "[0-9]", psw):
            continue
        elif not re.search( "[$#@]", psw):
            continue
        else:
            passwords.append(psw)
print(",".join(passwords))

#### Alternative
"""
ps=input()
pw=ps.split(',')
passwords=[]
for i in range(0,len(pw)):
    psw=pw[i].split().pop()
    cd1=0;cd2=0;cd3=0;cd4=0
    if len(psw)>=6 and len(psw)<=12:
        for j in range(0,len(psw)):
            if psw[j].isupper():
                cd1+=1
            elif psw[j].islower():
                cd2+=1
            elif psw[j].isdigit():
                cd3+=1
            elif psw[j]=="#" or psw[j]=="$" or psw[j]=="@":
                cd4+=1
        if(cd1>0 and cd2>0 and cd3>0 and cd4>0):
                passwords.append(pw[i])
print(",".join(passwords))
"""
"""
You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.
If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
We use itemgetter to enable multiple sort keys.
"""
from operator import itemgetter
l = []
while True:
    s = input()
    if not s:
        break
    l.append(tuple(s.split(",")))

print (sorted(l, key=itemgetter(0,1,2)))

#### Alternative
"""
l=[]
while True:
    ln=input()
    if ln:
        l.append(ln)
    else:
        break
dc={}
lne=[]
for i in range(0,len(l)):
    m=l[i].split(",")
    dc[m[0]]=i
    lne.append(m[0])
lne.sort() 
final=[]
for i in range(0,len(lne)):
    final.append(l[dc[lne[i]]])
    final[i]=final[i].split(",")
    final[i]=tuple(final[i])
print(final)   
"""
