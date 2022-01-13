# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 17:09:47 2022

@author: User
"""

"""
Here, I used exception handler(try,except) to handle the unexpected input. So if an user give
any other input other other than the required input from the program then the exception 
handler(except) will print the mesaage like "Enter the valid input."

I also used the the fromula of finding the tax amount from income.

"""

print("\nEnter your age:")
while(1):
    try:
        age=int(input())
        break
    except:
         print("\nEnter valid number for selecting age.")

print("\nEnter the corresponding number for selecting special cases:")
print("1.Women\n2.Disabled\n3.Parents of disabled\n4.Wounded freedom fighters\n5.None")
while(1):
    try:
        sp_cas=int(input())
        if (sp_cas>0 and sp_cas<6):
            break
        print("\nEnter valid number for selecting special case.")
    except:
        print("\nEnter valid number for selecting special case.")

print("\nEnter the amount of income in number:")
while(1):
    try:
        income=int(input())
        if (income>0):
            break
        print("\nEnter valid amount of income.")
    except:
         print("\nEnter valid amount of income.")
         

tax_amount=0

"""
Condintions of special cases for Women, Citizen older than 65 and Parents of disabled are same. 
"""
if (age>65 or sp_cas==1 or sp_cas==3):
    if(income<=350000):
        tax_amount=income*0
        
    elif(income<=450000):
        tax_amount=0+ 0.05*(income-350000)
        
    elif(income<=750000):
        tax_amount=0+0.05*(450000-350000)+0.1*(income-450000)

    elif(income<=1150000):
        tax_amount=0+0.05*(450000-350000)+0.1*(750000-450000)+0.15*(income-750000)

    elif(income<=1650000):
        tax_amount=(0+0.05*(450000-350000)+0.1*(750000-450000)+
                    0.15*(1150000-750000)+0.2*(income-1150000))

    else:
        tax_amount=(0+0.05*(450000-350000)+0.1*(750000-450000)+
                    0.15*(1150000-750000)+0.2*(1650000-1150000)+0.25*(income-1650000))

elif (sp_cas==2): 
    """
    Conditions for disabled.
    """
    if(income<=450000):
        tax_amount=income*0
        
    elif(income<=550000):
        tax_amount=0+ 0.05*(income-450000)
        
    elif(income<=850000):
        tax_amount=0+0.05*(550000-450000)+0.1*(income-550000)

    elif(income<=1250000):
        tax_amount=0+0.05*(550000-450000)+0.1*(850000-550000)+0.15*(income-850000)

    elif(income<=1750000):
        tax_amount=(0+0.05*(550000-450000)+0.1*(850000-550000)+
                    0.15*(1250000-850000)+0.2*(income-1250000))

    else:
        tax_amount=(0+0.05*(550000-450000)+0.1*(850000-550000)+
                    0.15*(1250000-850000)+0.2*(1750000-1250000)+0.25*(income-1750000))


elif (sp_cas==4):
    """
    Conditions for Wounded freedom fighters.
    """
    if(income<=475000):
        tax_amount=income*0
        
    elif(income<=575000):
        tax_amount=0+ 0.05*(income-475000)
        
    elif(income<=875000):
        tax_amount=0+0.05*(575000-475000)+0.1*(income-575000)

    elif(income<=1275000):
        tax_amount=0+0.05*(575000-475000)+0.1*(875000-575000)+0.15*(income-875000)

    elif(income<=1775000):
        tax_amount=(0+0.05*(575000-475000)+0.1*(875000-575000)+
                    0.15*(1275000-875000)+0.2*(income-1275000))

    else:
        tax_amount=(0+0.05*(575000-475000)+0.1*(875000-575000)+
                    0.15*(1275000-875000)+0.2*(1775000-1275000)+0.25*(income-1775000))

else:
    """
    Conditions for normal people under 65 years or 65 years old.
    """
    if(income<=300000):
        tax_amount=income*0
        
    elif(income<=400000):
        tax_amount=0+ 0.05*(income-300000)
        
    elif(income<=700000):
        tax_amount=0+0.05*(400000-300000)+0.1*(income-400000)

    elif(income<=1100000):
        tax_amount=0+0.05*(400000-300000)+0.1*(700000-400000)+0.15*(income-700000)

    elif(income<=1600000):
        tax_amount=(0+0.05*(400000-300000)+0.1*(700000-400000)+
                    0.15*(1100000-700000)+0.2*(income-1100000))

    else:
        tax_amount=(0+0.05*(400000-300000)+0.1*(700000-400000)+
                    0.15*(1100000-700000)+0.2*(1600000-1100000)+0.25*(income-1600000))
        
print("\nYour tax amount is",tax_amount,"Tk.")