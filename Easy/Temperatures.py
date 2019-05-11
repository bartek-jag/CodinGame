import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

    
n = int(input())  # the number of temperatures to analyse
if n == 0:
    print(0)
else:
    closest = 10000
    for i in input().split():
        i = int(i)
        if abs(closest) > abs(i):
            closest = i
        elif closest + i == 0:
            closest = abs(i)
    print(closest)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)



#print("result")