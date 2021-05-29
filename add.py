# def add(i,j):
#     i=i+j
#     print(i)

# add(40,20)

# def S(a,b):
#     g=a-b 
#     print(g)

# S(40,20)


# def M(c,d):
#     h=c=d
#     print(h)

# M(40,20)

def tables(num):
    for i in range(1,11):
        print(f"{num} X {i} = {num*i}")




n=int(input("which table you want to display?"))

tables(n)