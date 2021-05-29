print("Welcome to Tony's Pizza")
name=input("What is your name?: ")
phone=input(f"{name} what is your contact number? : ")
item=input("What is your favourite item from our menu? : ")
add=input("What would you like to add to our menu? : ")
quantity=int(input("Rate the food quantity on the scale of 1 to 5 : "))
quality=int(input("Rate the food quality on the scale of 1 to 5 : "))
service=int(input("Rate the service on the scale of 1 to 5 : "))
if quantity < 3 and quality < 3 and service < 3:
    print("Thank you for valuable feedback, well'l be definatley raise our scale ")
else:
    print("Thank you for your positive feedback...")

