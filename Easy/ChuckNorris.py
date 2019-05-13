"""Rules
Here is the encoding principle:

The input message consists of ASCII characters (7-bit)
The encoded output message consists of blocks of 0
A block is separated from another block by a space
Two consecutive blocks are used to produce a series of same value bits
(only 1 or 0 values):
- First block: it is always 0 or 00. If it is 0, then the series
contains 1, if not, it contains 0
- Second block: the number of 0 in this block is the number of bits
in the series

input:
Line 1: the message consisting of N ASCII characters
(without carriage return)
output: The encoded message
"""
ret = ""
lastBit = 2  # last inicated bit is not known when first bit is read
for i in input():
    k = 64  # 01000000 char 'i' will be read bit by bit from left to right
    i = ord(i)
    while k:
        bit = int(i) & int(k) == k
        if lastBit == bit:
            ret += "0"
        else:
            ret += " "
            if bit:
                ret += "0 0"
            else:
                ret += "00 0"
        lastBit = bit
        k = k >> 1
print(ret[1:])
