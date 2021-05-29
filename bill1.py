brownie =5
chococookie=15
croissant= 3
print(f'''       Menu
------------------------------
Brownie           - $ {brownie}
Croissant         - $ {croissant}
chococookie      - $ {chococookie}''')   
print('/'*30)
bill =0
order=input("Kindly place your Order:\n").lower()

if order =='brownie':
    bill += brownie
    print(f"Thanks for ordering {order}")
elif order == 'chococookie': 
    bill += chococookie
    print(f"Thanks for ordering {order}") 
elif order == 'croissant': 
    bill += croissant
    print(f"Thanks for ordering {order}") 
else:
    print(f'Sorry wrong order !! we do not sell {order}') 
    exit()  
quantity = int(input(f'how many {order}s do you wish to Order?\n'))

print('_'*30)

print(f"The Total Bill Amount is ${bill*quantity}")


