import turtle as t

n = 10
t.color("purple")
t.begin_fill()

for x in range(n):
    t.fd(50)
    t.lt(360/n)
t.end_fill()
