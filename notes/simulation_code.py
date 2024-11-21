import numpy as np
np.random.seed(1)
up = 0
n = 1000
for i in range(n):
    U = np.random.uniform(1, 15)
    up += (U < 13)
up / n

n = 1000
results = np.random.uniform(1, 15, n)
results.sum() / n

A = [2, 2, 4, 4, 9, 9]
B = [1, 1, 6, 6, 8, 8]
C = [3, 3, 5, 5, 7, 7]

n = 10000

ab = 0
for i in range(n):
    ab += np.random.choice(A) < np.random.choice(B)
ab / n

bc = 0
for i in range(n):
    bc += np.random.choice(B) < np.random.choice(C)
bc / n

ca = 0
for i in range(n):
    ca += np.random.choice(C) < np.random.choice(A)
ca / n

def play(a, b, n = 1000):
    ab = 0
    for i in range(n):
        ab += np.random.choice(a) < np.random.choice(b)
    return ab / n

play(A, B)
play(B, C)
play(A, C)

# Version 1
n_gold_coin = 0
n_both_gold = 0
n = 1000
for i in range(n):
    boxes = [['g', 'g'], ['s', 's'], ['g', 's']]
    box_id = np.random.choice(range(len(boxes)))
    box = boxes[box_id]
    coin = np.random.choice(box)
    if coin == 'g':
        n_gold_coin = n_gold_coin + 1
        if box == ['g', 'g']:
            n_both_gold += 1
n_both_gold / n_gold_coin 

# version 2
def bert():
    boxes = [['g', 'g'], ['s', 's'], ['g', 's']]
    box_id = np.random.choice(range(len(boxes)))
    box = boxes[box_id]
    coin = np.random.choice(box)
    return box, coin

n_gold_coin = 0
n_both_gold = 0
N = 1000
np.random.seed(1)
for i in range(N):
    box, coin = bert()
    if coin == 'g':
        n_gold_coin = n_gold_coin + 1
        if box == ['g', 'g']:
            n_both_gold += 1
n_both_gold / n_gold_coin 

bert()

def birth(n_people, n_days):
    days = np.arange(n_days)
    room = np.random.choice(days, n_people, replace=True)
    common_birthday = len(room) > len(set(room))
    return common_birthday

def play(n_people, n_days, n):
    common = 0
    for i in range(n):
        common += birth(n_people, n_days)
    return common / n

play(500, 2400000, 1000)

def mont():
    car = np.random.choice([1, 2, 3])
    choice = 1
    if car == 1:
        host_open = np.random.choice([2, 3])
    if car == 2:
        host_open = 3
    if car == 3:
        host_open = 2
    return host_open, car 

mont()

n = 1000
open3 = 0
car1 = 0
car2 = 0
for i in range(n):
    o, c = mont()
    if o == 3:
        open3 += 1
        if c == 1:
            car1 += 1
        else:
            car2 += 1

car1 / open3
car2 / open3
