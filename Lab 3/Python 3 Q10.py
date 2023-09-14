#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 22:47:59 2023

@author: prateekgoswami
"""

n1= int(input("Enter any number: "))
n2= int(input("Enter any number: "))
n3= int(input("Enter any number: "))
if n1>n2:
    if n1>n3:
        print(n1,"is the largest numbers")
    else:
        print(n3,"is the largest numbers")
else:
    if n2>n3:
        print(n2,"is the largest numbers")
    else:
        print(n3,"is the largest numbers")
