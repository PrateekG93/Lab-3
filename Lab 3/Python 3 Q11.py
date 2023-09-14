#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 23:04:39 2023

@author: prateekgoswami
"""

a= int(input("Enter a three digit number: "))
if a>999 and a<99:
    print("Invalid input")
else:
    b= a//100
    c= (a%100)//10
    d= a%10
    if b**3+c**3+d**3==a:
        print(a,"is an Armstrong number")
    else:
        print(a,"is not an Armstrong number")