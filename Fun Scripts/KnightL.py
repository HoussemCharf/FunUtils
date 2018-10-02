#!/bin/python
# Script for Chess matrix exploration using Knight piece moves (L) and determining the best combination.
import sys

n = int(raw_input().strip())
for i in range(1, n)  :
    if i>1 :
        print 
    for j in range(1, n) :
        notreached = True
        nonew = True
        oldset = [(n - 1, n - 1)]
        currentset=[]
        cpt = 0
        while notreached and nonew:
            nonew = False
            cpt=cpt+1
            for (x, y) in oldset:
                if not (x + i, y + j) in oldset and x + i < n and y + j < n and not (x + i, y + j) in currentset:
                    currentset.append((x + i, y + j))
                    nonew = True

                if not (x - i, y + j) in oldset and -1 < x - i  and y + j < n and not (x - i, y + j) in currentset:
                    currentset.append((x - i, y + j))
                    nonew = True
                if not (x + i, y - j) in oldset and x + i < n and -1 < y - j and not (x + i, y - j) in currentset:
                    currentset.append((x + i, y - j))
                    nonew = True
                if not (x - i, y - j) in oldset and -1 < x - i and -1 < y - j and not (x - i, y - j) in currentset:
                    currentset.append((x - i, y - j))
                    nonew = True
                if not (x + j, y + i) in oldset and x + j < n and y + i < n and not (x + j, y + i) in currentset:
                    currentset.append((x + j, y + i))
                    nonew = True
                if not (x - j, y + i) in oldset and y + i < n and -1 < x - j and not (x - j, y + i) in currentset:
                    currentset.append((x - j, y + i))
                    nonew = True
                if not (x + j, y - i) in oldset and x + j < n and -1 < y - i and not (x + j, y - i) in currentset:
                    currentset.append((x + j, y - i))
                    nonew = True
                if not (x - j, y - i) in oldset and -1 < x - j and -1 < y - i and not (x - j, y - i) in currentset:
                    currentset.append((x - j, y - i))
                    nonew = True
            
            oldset.extend(currentset)
            if (0, 0) in currentset:
                print cpt,
                notreached = False
            currentset = []
        if not nonew :
            print -1,
