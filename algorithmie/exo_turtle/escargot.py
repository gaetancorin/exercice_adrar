from turtle import *
speed(0)

# Coquille
color('green')
width(5)
rayon = 1
for _ in range(10):
    circle(rayon,180)
    rayon += 5

# Escargot
# Body
color('blue')  
for _ in range(12):
    seth(90)
    fd(4)
    seth(0)
    fd(6)
seth(90)
fd(40)

for _ in range(6):
    seth(180)
    fd(4)
    seth(90)
    fd(4)
# Eyes1
seth(180)
circle(-10,160)
circle(-10,160)

for _ in range(6):
    seth(0)
    fd(4)
    seth(270)
    fd(4)
#Eyes_center
seth(0)
fd(10)

for _ in range(6):
    seth(90)
    fd(4)
    seth(0)
    fd(4)
# Eyes2
seth(180)
circle(-10,160)
circle(-10,160)

seth(270)
fd(2)
for _ in range(7):
    seth(270)
    fd(4)
    seth(180)
    fd(4)

# Body
seth(270)
fd(10)
seth(180)
fd(8)
seth(0)
fd(8)
seth(270)
fd(40)

circle(-50,140)






input()
