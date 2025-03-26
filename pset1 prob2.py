# -*- coding: utf-8 -*-
"""
Created on Tue Mar 25 21:23:16 2025

For MIT OCW Intro to CS with Python
Problem Set 1, Problem 2
Taking problem set 1, but adding a feature to incorporate semi-annual raises
    
@author: ralenjor
"""

# request input from user to define variables

print("Enter your annual salary in whole dollars, without commas.")
annual_salary = float(input())

print("Enter your semi-annual raise, as a decimal.")
semi_annual_raise = float(input())

print("In decimal form, enter the percentage of your salary that you will save.")
portion_saved = float(input())

print("Enter the cost of your dream home.")
total_cost = float(input())

portion_down_payment = (float(total_cost * .25))

current_savings = 0

annual_return = .04

monthly_return = annual_return / 12

counter = 0
  
while current_savings < portion_down_payment:
   monthly_savings = portion_saved * (annual_salary / 12) * (1 + monthly_return)
   current_savings += monthly_savings
   counter += 1
   
   if counter % 6 == 0:
      annual_salary = annual_salary * (1 + semi_annual_raise)
   
   if current_savings >= portion_down_payment:
       print("You will have enough for your down payment in "+ str(counter) +" months.")
       break
   else:
       continue
