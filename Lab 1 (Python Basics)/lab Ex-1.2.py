# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 20:39:46 2021

@author: User
"""
Number = int(input("Enter the number: "))
if(97<=Number<=100):
    print("Grade: A+")
elif (90<=Number<97):
    print("Grade: A")
elif (87<=Number<90):
    print("Grade: A-")
elif (83<=Number<87):
    print("Grade: B+")
elif (80<=Number<83):
    print("Grade: B")
elif (77<=Number<80):
    print("Grade: B-")
elif (73<=Number<77):
    print("Grade: C+")
elif (70<=Number<73):
    print("Grade: C")
elif (67<=Number<70):
    print("Grade: C-")
elif (63<=Number<67):
    print("Grade: D+")
elif (60<=Number<63):
    print("Grade: D")
else: print("Grade:F")

    