"""
Write a program to input electricity unit charge and calculate the total electricity bill according to the given condition:

	For first 50 units -> Rs. 0.50/unit    0 - 50
	For next 100 units -> Rs. 0.75/unit    51 - 150
	For next 100 units -> Rs. 1.20/unit    151 - 250
	For unit above 250 -> Rs. 1.50/unit    251 and above

	300 
	50 - 0.50 = 25
	100 - 0.75=75
	100 - 1.20 = 120
	50 - 1.50  = 75   total - 295
 
 
"""


units = float(input("Enter the number of units: "))


if units <= 50:
    bill = units * 0.50
    
elif units <= 150:
    bill = (50 * 0.50) + ((units - 50) * 0.75)
elif units <= 250:
    bill = (50 * 0.50) + (100 * 0.75) + ((units - 150) * 1.20)
else :
    bill = (50 * 0.50) + (100 * 0.75) + (100 * 1.20) + ((units - 250) * 1.50)
    
    
print("Total Bill = %.2f" % bill)