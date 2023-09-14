#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 10:34:38 2023

@author: prateekgoswami
"""

a = int(input("Enter the five digit number: "))
b= a//10000
c= (a%10000)//1000
d= (a%1000)//100
e= (a%100)//10
f= (a%10)
num= f*10000+e*1000+d*100+c*10+b
if a==num:
    print("Number is a Palintrom")
else:
    print("Number is not a Palintrom")