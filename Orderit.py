# -*- coding: utf-8 -*-
"""
Created on Sat Nov  1 10:36:46 2025

@author: keert
"""

def min_moves():
    n=int(input());input()
    shuffled=[input().strip()for _ in range(n)]
    input();original=[input().strip()for _ in range(n)]
    pos={original[i]:i for i in range(n)}
    order=[pos[x]for x in shuffled]
    count,max_seq=1,1
    for i in range(1,n):
        if order[i]==order[i-1]+1: count+=1
        else: count=1
        if count>max_seq: max_seq=count
    print(n-max_seq if n>0 else 0)

min_moves()


