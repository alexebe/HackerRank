#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    left = [(r_q,c) for c in range(c_q - 1, 0, -1)]
    right = [(r_q,c) for c in range(c_q + 1, n + 1 , 1)]
    bottom = [(r,c_q) for r in range(r_q - 1, 0, -1)]
    top = [(r,c_q) for r in range(r_q + 1, n + 1, 1)]
    diag_left_bottom = list(zip(range(r_q - 1, 0, -1), range(c_q - 1, 0, -1)))
    diag_left_top = list(zip(range(r_q + 1, n + 1, 1), range(c_q - 1, 0, -1)))
    diag_right_bottom = list(zip(range(r_q - 1, 0, -1), range(c_q + 1, n + 1, 1)))
    diag_right_top = list(zip(range(r_q + 1, n + 1, 1), range(c_q + 1, n + 1, 1)))
    
    listOfSquare = [left,right,bottom,top,diag_left_bottom,diag_left_top,diag_right_bottom,
                   diag_right_top]
    count = 0
    for ls in listOfSquare:
        count += attackableSquare(ls, obstacles)
    return count    
        
def attackableSquare(listOfSquare, obstacles):
    nb = 0
    for s in listOfSquare:
        if([s[0],s[1]] not in obstacles):
            nb += 1
        else:
            break;
    return nb        
