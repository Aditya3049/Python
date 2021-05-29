nums = [1,4,2,17,3,111,0,13,27,14,0,23,11,25,12,19]

even = []
odd = []
for i in nums:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)  

print("*"*30)
print(even) 
print("*"*30)
print(odd)         