# Timothy Rutkowski 01/24/2024 timothyRutkowski_lab2-1.py

# This program will calculate and output the amount of vines 
# that can fit in a vineyard row based on:
# the length of the row in meters,
# the space of the trellis end-post assembly in meters,
# and the space between the vines in meters as entered by the user.

#Gets math functions
import math

#Displays input prompts and defines variables
R = float(input('Please enter the length of the row in meters: '))
E = float(input('Please enter the space of the trellis end-post assembly in meters: '))
S = float(input('Please enter the space between vines in meters: '))

#Calculates the amount of vines that can fit in a row and rounds down result
V = max(0, math.floor((R - 2*E) / S))

#Displays the final result
print('The amount of vines that can fit in a row is',V,'vines')