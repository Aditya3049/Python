# Steps
# Create your own Menu Choices
# Take the Customer Order along with Quantity of each item
# Customer should 
# have the choice of ordering more than 1 dish.
# Print the Final Bill for the customer
rows=int(input("Enter number of rows: "))
for i in range(rows):
    for j in range(i+1):
        print('*',end ="")
    print("\n")