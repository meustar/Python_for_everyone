import turtle as t
import random

t.shape("turtle")
t.speed(0)

for x in range(500):
    a = random.randint(1,500)
    t.setheading(a)
    t.fd(10)
