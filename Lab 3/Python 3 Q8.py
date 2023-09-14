#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 22:08:24 2023

@author: prateekgoswami
"""

basic_salary= int(input("Enter the Basic Salary: "))
HRA= basic_salary*(0.2)
DA = basic_salary*(0.1)
Gross_Salary = basic_salary+ HRA+ DA
print("Gross Salary is", Gross_Salary)