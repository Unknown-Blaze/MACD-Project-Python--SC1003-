import time
import random

score = 0
max_time = 5

tpp = []

t0 = time.time()
t1 = time.time()

while True:
    a = random.randint(0, 10)
    b = random.randint(0, 10)

    t1 = time.time()
    print(f"{a} + {b} =                                                   time = {round(t1-t0, 2)}")
    if t1-t0 > max_time:
        break
    c = int(input())
    if c == a+b:
        score += 1

    
print(f"Final score = {score}")

