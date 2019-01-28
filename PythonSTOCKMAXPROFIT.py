# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 09:14:54 2019

@author: Osman Ali Yardım

Stock Maximum Profit (A Google's Interview Question)
"""

"""
Question: You will be given a list of stock prices for a given day and your goal is to return the maximum profit
that could have been made by buying a stock at the given price and then selling the stock later on.
For example, if the input is: [45, 24, 35, 31, 40, 38, 11] then your program should return 16 
because if you bought the stock at dolar 24 and sold it at dolar 40, a profit of dolar 16 was made
and this is the largest profit that could be made. If no profit could have been made, return -1.
"""

def maxProfit(list):
    max = -1
    min = 99999
    
    for i in list:
        if i > max:
            max = i
        if i < min:
            min = i
        
    maxProfit = max - min
    
    print ("buy_price = ",min,", sell_price = ",max,", max_profit = ",maxProfit)


#Demo for maxProfit
maxProfit([45,24,35,31,40,38,11])
maxProfit([1,45,6,64,34,22,89,99])