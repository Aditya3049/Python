import random
Cscore=0
Pscore=0
for x in range (5):
    S=int(input("enter a number (1-5)"))
    print(f"Round {x+1} ")
    S1=int(input("PLease guess any number between 1 to 5"))
    if S1 == S:
        print("player 1 won!!!!!!")
        Pscore += 1

    else:
        Cscore += 1
        print("player 2  won.. ")

print("final score")
print("*"*30)
print(f"Player Score= {Pscore} ")
print("//////////////////////////////////////////////////////////////////////////////////////")
print(f"Computer Score= {Cscore}")
if Pscore > Cscore:
    print("Player Won!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
else:
    print("Computer Won!")
    
print("--------------------------------------------------------------------------------------")