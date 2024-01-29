#File: q5.py
#Author: Leah Philip
#Date: 01/24/2023
#Section: 506
#E-mail: leahephilip@tamu.edu
#Description: This program asks the user for input and calculates the answer to a specific equation utilizing the input.
import math
n = int(input("Enter the value of n:"))
part1=((n**2)+((n+1)**2))/2
part2= math.sqrt(part1)
final=part2*n
print("The result is:", final)
