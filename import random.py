import random
 
def randomlist(lenght):
    randlist = []
    for i in range (1, lenght+1):
        n =random.randint(1,10)
        randlist.append(n)
    return randlist
 
r = randomlist(6)
print(r)
 