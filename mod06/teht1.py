import random


def noppa():
    return random.randint(1,6)



heitto = 0
while heitto != 6:
    heitto = noppa()
    print(heitto)