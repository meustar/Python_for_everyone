import turtle as t

n = 50
t.bgcolor("green")
t.color("black")
t.speed(0)

for x in range(n):
    t.circle(x*2)
    t.lt(360/n)

