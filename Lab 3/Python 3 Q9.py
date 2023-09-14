#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 22:41:32 2023

@author: prateekgoswami
"""

basic_salary= int(input("Enter the Basic Salary: "))
HRA= basic_salary*(0.2)
DA = basic_salary*(0.1)
Gross_Salary = basic_salary+ HRA+ DA
print("Gross Salary is", Gross_Salary)

if Gross_Salary< 300000:
    print("Income tax will be Rs", Gross_Salary*(0))
elif Gross_Salary<1000000 and Gross_Salary>300000:
    print("Income tax will be Rs", Gross_Salary*(0.1))
elif Gross_Salary>1000000 and Gross_Salary<2500000:
    print("Income tax will be Rs", Gross_Salary*(0.2))
else: 
    print("Income tax will be Rs", Gross_Salary*(0.3))