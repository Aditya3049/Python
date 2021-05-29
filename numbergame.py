nums=[1,4,-2,17,3,11,10,13,27,-14,0,27,0,-14,50,44,-12,-1000,0,0,0,0,0,1234567890,-523677839,35827390,3645839380,0,3454,-50]
pos=0
neg=0
zeros=0
for num in nums:
    if num >0:

       pos +=1
    elif num <0:
        neg += 1
    else:
        zeros += 1

print(f"Positive ----------------{pos}")    
print(f"Negative ----------------{neg}")
print(f"Zeros--------------------{zeros}")           