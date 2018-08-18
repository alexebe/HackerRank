#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    #Closest obstacles on each direction
    cObsLeft = [r_q, 0]
    cObsRight = [r_q, n + 1]
    cObsBottom = [0, c_q]
    cObsTop = [n + 1, c_q]
    
    #Rows converge towards n + 1 while columns converge towards 0
    #Do rows reach n + 1 before columns reach 0 or vice versa ?
    cObsDiagLeftTop = [r_q + min(n + 1 - r_q, c_q),
                      c_q - min(n + 1 - r_q, c_q)]
    
    #Both rows and columns converge towards 0
    #Which of both dimensions reach 0 first ?
    cObsDiagLeftBottom = [r_q - min(r_q, c_q), c_q - min(r_q, c_q)]
    
    #Rows converge towards 0 while columns converge towards n + 1
    #Do rows reach 0 before columns reach n + 1 or vice versa ?
    cObsDiagRightBottom = [r_q - min(r_q, n + 1 - c_q),
                          c_q + min(r_q, n + 1 - c_q)]

    #Both rows and columns converge towards n + 1
    #Which of both dimensions reaches n + 1 first ?
    cObsDiagRightTop = [r_q + min(n + 1 - r_q, n + 1 - c_q),
                        c_q + min(n +1 - r_q, n +  1- c_q)]

    for obs in obstacles:
        if(obs[0] == r_q and obs[1] < c_q and obs[1] > cObsLeft[1]):
            cObsLeft = obs
        elif(obs[0] == r_q and obs[1] > c_q and obs[1] < cObsRight[1]):
            cObsRight = obs
        elif(obs[0] < r_q and obs[0] > cObsBottom[0] and obs[1] == c_q):
            cObsBottom = obs
        elif(obs[0] > r_q and obs[0] < cObsTop[0] and obs[1] == c_q):
            cObsTop = obs
		#Equation of NW diagonal is: Given a square situated a row r and column c,
		#r - r_q = c_q - c and r - r_q > 0 and c_q - c > 0
        elif(((obs[0] - r_q) == (c_q - obs[1])) and obs[0] - r_q > 0 
             and c_q - obs[1] > 0 and cObsDiagLeftTop[0] > obs[0]):
            cObsDiagLeftTop = obs
		#Equation of SW diagonal is: Given a square situated a row r and column c,
		#r_q - r = c_q - c and r_q - r > 0 and c_q - c > 0
        elif(((r_q - obs[0]) == (c_q - obs[1])) and r_q - obs[0] > 0 
             and c_q - obs[1] > 0 and cObsDiagLeftBottom[0] < obs[0]):  
            cObsDiagLeftBottom = obs
		#Equation of SE diagonal is: Given a square situated a row r and column c,
		#r_q - r = c - c_q and r_q - r > 0 and c - c_q > 0
        elif(((r_q - obs[0]) == (obs[1] - c_q)) and r_q - obs[0] > 0 
             and obs[1] - c_q > 0 and cObsDiagRightBottom[0] < obs[0]):
            cObsDiagRightBottom = obs
		#Equation of NE diagonal is: Given a square situated a row r and column c,
		#r - r_q = c - c_q and r - r_q > 0 and c - c_q > 0
        elif(((obs[0] - r_q) == (obs[1] - c_q)) and obs[0] - r_q > 0 
             and obs[1] - c_q > 0 and cObsDiagRightTop[0] > obs[0]):
            cObsDiagRightTop = obs
            
    
    count = 0
    count += cObsRight[1] - cObsLeft[1] - 2
    count += cObsTop[0] - cObsBottom[0] - 2
    count += cObsDiagLeftTop[0] - cObsDiagLeftBottom[0] - 2
    count += cObsDiagRightTop[0] - cObsDiagRightBottom[0] - 2
    return count
