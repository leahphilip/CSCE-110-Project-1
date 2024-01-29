#File: q4.py
#Author: Leah Philip
#Date: 01/24/2023
#Section: 506
#E-mail: leahephilip@tamu.edu
#Description: This program computes the Black Friday discount and tax on items.
item1=int(input("Price of item 1:"))
item2=int(input("Price of item 2:"))
subtotal=item1+item2
total=((subtotal)*.6)
tax=(.0825*total)
final=total+tax
print("Your final amount is:",final)
