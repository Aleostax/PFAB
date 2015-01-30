#Prompt the user to input price,sales tax rate, and calculate the total cost of the item.
item = input("What is the cost of the item?\t")
tax = input("What is the sales tax rate?\t")
print "Total cost of the item is:\t",item*(1+tax)
