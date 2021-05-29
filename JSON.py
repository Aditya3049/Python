import json
# name="Aditya"
# Age=11
# with open("students.json","w") as file:
#     json.dump({name:Age},file,indent=2)
with open('students.json','r') as file1:
    students=json.load(file1)
    students['ABCS'] =22
with open("students.json","w") as file:
    json.dump(students,file,indent=2)
