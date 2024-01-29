#File: q3.py
#Author: Leah Philip
#Date: 01/24/2023
#Section: 506
#E-mail: leahephilip@tamu.edu
#Description: This program takes takes the number of days and computes it into years, months, and days.
totalDays = int(input("Enter the number of days:"))
years = totalDays//365
months = (totalDays%365)//30
days = (totalDays%365)%30
print(totalDays,"days=", years,"years", months,"months and", days,"days")

