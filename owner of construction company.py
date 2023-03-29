#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'maxProfit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER costPerCut
#  2. INTEGER salePrice
#  3. INTEGER_ARRAY lengths
#

def maxProfit(costPerCut, salePrice, lengths):
    max_profit = 0
    
    for sale_length in range(1, max(lengths) + 1):
        sale_price_per_rod = salePrice * sale_length
        profit = 0

        for rod_length in lengths:
            uniform_rods = rod_length // sale_length
            
            if uniform_rods > 0:
                extra_cut = 1 if rod_length % sale_length > 0 else 0
                total_cuts = uniform_rods - 1 + extra_cut
                
                costs = total_cuts * costPerCut
                revenues = uniform_rods * sale_price_per_rod
                
                if revenues > costs:
                    profit += revenues - costs
        if profit > max_profit:
            max_profit = profit
    
    return max_profit
    # Write your code here
if _name_ == '_main_':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    costPerCut = int(input().strip())

    salePrice = int(input().strip())

    lengths_count = int(input().strip())

    lengths = []

    for _ in range(lengths_count):
        lengths_item = int(input().strip())
        lengths.append(lengths_item)

    result = maxProfit(costPerCut, salePrice, lengths)

    fptr.write(str(result) + '\n')

    fptr.close()