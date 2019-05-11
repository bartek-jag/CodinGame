import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
h = int(input())
t = input()
#t = list(t)
for i in range(h):
    row = input()
    ret = ""
    for j in range(t.__len__()):
        letterVal = ord(t[j])
        if letterVal in range(65,91):
            letIdx = l*(letterVal-65)
            ret += row[letIdx:letIdx+l]
        elif letterVal in range(97,123):
            letIdx = l*(letterVal-97)
            ret += row[letIdx:letIdx+l]
        else:
            ret += row[row.__len__()-l:row.__len__()] 
    print(ret)