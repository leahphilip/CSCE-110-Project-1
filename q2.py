#File: q2.py
#Author: Leah Philip
#Date: 01/24/2023
#Section: 506
#E-mail: leahephilip@tamu.edu
#Description: This program takes takes the area of a circle as input and prints its circumference as output.
import math
area = int(input('Enter area:\n'))
pi=3.1415
radius= math.sqrt(area/pi)
circumference= 2*pi*radius
print("The circumference of the circle is:", circumference)
