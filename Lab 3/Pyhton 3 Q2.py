#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 09:27:54 2023

@author: prateekgoswami
"""
#1
weight= float(input("Enter your weight in kilograms: "))
height= float(input("Enter your height in meters: "))
BMI= weight/(height**2)
print("Body mass index according to the weight and height is:", BMI)



#2
weight = float(input("Enter your weight in pounds: "))
height= float(input("Enter your height in inches: "))
BMI = (weight*0.453)/(height*0.0254)**2