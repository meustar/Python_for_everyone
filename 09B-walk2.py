import turtle as t
import random

t.shape("turtle")
t.speed(0)

for x in range(500):
    a = random.randint(1,360)
    t.setheading(a)
    b = random.randint(10, 40)
    t.fd(b)
