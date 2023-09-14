#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 10:03:56 2023

@author: prateekgoswami
"""

a = int(input("Enter the three digit number: "))
b= a//100
c= (a - (b*100))//10
d= ((a- b*100)- (c*10))
SUM= b+c+d
print("Sum of the numbers is: ", SUM)
if SUM%3==0:
    print("Sum of the numbers is divisible by 3")
else:
    print("Sum of the numbers is not divisible by 3")