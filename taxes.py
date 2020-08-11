#taxes.py
#Mr Powers
#11 Aug 2020
#
#Modified by:
#Homeroom:      
#Date:          
#
#This program will calculate the final price for most items in NYC.
#It does so by adding the various taxes. Source:
#https://www1.nyc.gov/site/finance/taxes/business-nys-sales-tax.page#:~:text=The%20City%20Sales%20Tax%20rate,Use%20Tax%20of%208.875%20percent.
#
#input:     user enters an integer or decimal number from keyboard
#output:    prints final cost to screen

NYC_TR = 0.04500    #NYC tax rate is 4.5%
NYS_TR = 0.04000    #NY State TR is 4%
MCT_TR = 0.00375    #NY Metro Comm. Transp. TR is 0.375%
total_tr =  NYC_TR + NYS_TR + MCT_TR   #add up the three tax rates

itemPrice = float(input("Enter the item price: "))   #get user input from keyboard decimal or integer
totalTax = total_tr * itemPrice     #calculate the amount of tax for the item
totalCost = itemPrice + totalTax    #add the tax to the original price to get the final cost

#print the final cost – format to 2 decimal places because you don't pay 1/2 pennies!
print("{:.2f}".format(totalCost))   
