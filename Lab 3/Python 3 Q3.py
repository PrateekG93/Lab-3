#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 09:33:53 2023

@author: prateekgoswami
"""

a = float(input("Enter length of one side: "))
b= float(input("Enter length of second side: "))
c= float(input("Enter length of third side: "))
if a<b+c and b<a+c and c<b+a: 
    print("Triangle with these sides can exist")
else:
    print("Triangle with these sides can not exist")