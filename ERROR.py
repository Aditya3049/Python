print("division")
while True:
    try:
        d=int(input("Enter a divendend:\n"))
        d1=int(input("Enter a diviser:\n "))
    except:
        print("sorry enterr a number")    
    else:
        try:
            i=d/d1

          
        except ZeroDivisionError:
            print("divdend cannot be zero") 
        else:
            print(i)
