import random
for i in range(10):
    print(f'Round {i+1}:     ')
    
    player1 = random.randint(1,6)
    player2=random.choice([1,2,3,4,5,6])
    if player2 > player1:
      print("Player 2 is winner")
      print(player1)
      print(player2)
      print('/'*30)   
    elif player1 == player2:
       print("tie")
       print(player1)
       print(player2) 
       print('/'*30)
    else:
       print("Player 1 is winner")
      
       print(player1)
       print(player2)
       print('/'*30)   
       
    

