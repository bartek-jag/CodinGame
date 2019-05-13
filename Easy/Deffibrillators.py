import sys
import math
import re

"""The city of Montpellier has equipped its streets with defibrillators
to help save victims of cardiac arrests. The data corresponding to the
position of all defibrillators is available online.

Based on the data we provide in the tests, write a program that will
allow users to find the defibrillator nearest to their location using
their mobile phone.

	Rules
The input data you require for your program is provided in text
format. This data is comprised of lines, each of which represents a
defibrillator.
Each defibrillator is represented by the following fields:
A number identifying the defibrillator
Name
Address
Contact Phone number
Longitude (degrees)
Latitude (degrees)
These fields are separated by a semicolon (;).

Beware: the decimal numbers use the comma (,) as decimal separator.
Remember to turn the comma (,) into dot (.) if necessary in order to
use the data in your program.

The program will display the name of the defibrillator located the
closest to the user’s position. This position is given as input to
the program.

Input
Line 1: User's longitude (in degrees)
Line 2: User's latitude (in degrees)
Line 3: The number N of defibrillators located in the streets of
Montpellier
N next lines: a description of each defibrillator

Output
The name of the defibrillator located the closest to the user’s
position.
"""

user_lon = float(re.sub(",", ".", input()))  user longitude
user_lat = float(re.sub(",", ".", input()))  # user latitude
number_or_defibrillators = int(input())
closest_dist = sys.maxsize
closest_name = ""
for i in range(number_or_defibrillators):
    defibrillator = input()  # read defibrillator data
    idx, name, address, phone, def_lon, def_lat = defibrillator.split(";")
    def_lon = float(re.sub(",", ".", def_lon))
    def_lat = float(re.sub(",", ".", def_lat))
    def_dist = math.sqrt(
        math.pow((user_lon - def_lon)*math.cos((user_lat + def_lat)/2), 2)
        + math.pow(user_lat - def_lat, 2))
    if def_dist < closest_dist:
        closest_name = name
        closest_dist = def_dist
print(closest_name)
