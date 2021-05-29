shopping={'Egg':45,'cheese':200,'Fruit':433,'Vegetable':6666}
# for i,j in shopping.items():
#     print(f"{i}'s price is {j}")

# for i in shopping.keys():
#     print(i)    

# for i in shopping.values():
#     print(i)    


print("_"*30,"Adding elements in shopping cart" )    
shopping['Milk']=577
shopping['Butter']=400
print(shopping)
print("update dict")
shopping['cheese']=300
shopping.popitem()
print(shopping)