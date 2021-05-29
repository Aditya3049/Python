from datetime import datetime, timedelta
def today():
    return datetime.now().strftime('%d-%b-%Y') 

def past1():

    today=datetime.now()
    past=today - timedelta(days=10)
    print(past)

def add(x,y):
    x=x+y
    print(x)

def S(a,b):
    g=a-b 
    print(g)




def M(c,d):
    h=c=d
    print(h)


