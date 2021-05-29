party_planner = ['Prepare a Guest List',
'Order a Cake']

print("To Do List")
while True:
  todo = input(">: ")
  party_planner.append(todo)
  # Add your to-do list item here
  
  quit = input("Press q to Quit").lower()
  if quit == 'q':
      break
  else:
      print("list added")  
print(party_planner)

