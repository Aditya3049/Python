import random
print("roll a  on the dice")
print("-"*30)
tries=0
while True:
    dice=random.randint(1,6)
    tries=tries+1
    if dice == 6:
        break
    else:
        print(f"You rolled {dice} in {tries} tries")
print(f'you rolled {dice} after {tries} tries')       
