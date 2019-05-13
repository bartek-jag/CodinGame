import sys

"""Write a program which, using a given number of strengths, identifies 
the two closest strengths and shows their difference with an integer 
(≥ 0).
Input:
Line 1: Number N of horses
The N following lines: the strength Pi of each horse. Pi is an integer.

Output:
The difference D between the two closest strengths. D is an integer 
greater than or equal to 0.
"""

numberOfHorses = int(input())
diff = sys.maxsize
strengthList = [int(input()) for i in range(numberOfHorses)]
strengthList.sort()

for i in range(numberOfHorses-1):
    diff = min(diff, strengthList[i+1]-strengthList[i])
print(diff)
