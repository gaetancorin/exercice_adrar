from turtle import *

# current_color = 0
# def shift_color(n):
#     global current_color
#     current_color += n
#     current_color %= 1
#     t = [(1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(1,0,0)]
#     n1 = int(6*current_color)
#     n2 = n1+1
#     w1 = 6*current_color-n1
#     w2 = 1-w1
#     color(t[n1][0]*w2+t[n2][0]*w1,t[n1][1]*w2+t[n2][1]*w1,t[n1][2]*w2+t[n2][2]*w1)

# B1
color('green')
width(5)
for _ in range(4):
    fd(50)
    seth(270)
    fd(50)
    seth(0)

# B2
# color('red')
# width(5)
# for _ in range(4):
#     seth(90)
#     fd(50)
#     seth(0)
#     fd(50)
#     seth(270)
#     fd(50)
#     seth(0)
#     fd(50)

# B3
# color('purple')
# width(5)
# for _ in range(4):
#     fd(100)
#     right(90)

# B4
# color('cyan')
# width(5)
# for _ in range(3):
#     fd(100)
#     left(120)

# B5
# color('orange')
# width(5)
# seth(90)
# fd(100)
# color('red')
# for _ in range(3):
#     fd(50)
#     right(120)

# B6
# color('red')
# width(5)
# for _ in range(2):
#     fd(50)
#     seth(90)
#     fd(50)
#     seth(0)
# color('green')
# for _ in range(3):
#     seth(0)
#     fd(50)
#     seth(270)
#     fd(50)

# B7
# color('orange')
# width(5)
# for _ in range(3):
#     fd(100)
#     left(120)
# for _ in range(4):
#     fd(100)
#     right(90)

# B8
# color('yellow')
# width(5)
# for _ in range(8):
#     fd(200)
#     right(180-45)

# B9
# color('purple')
# width(5)
# fd(50)
# up()
# fd(50)
# down()
# for _ in range(3):
#     fd(100)
#     right(120)

# B10
# width(5)
# color('cyan')
# for _ in range(8):
#     fd(100)
#     right(135)
# up()
# fd(200)
# down()
# color('yellow')
# for _ in range(8):
#     fd(200)
#     left(135)
# up()
# seth(270)
# fd(100)
# down()
# color('purple')
# for _ in range(8):
#     fd(100)
#     right(135)

# B11
# width(5)
# color('red')
# for _ in range(4):
#     fd(50)
#     left(90)
#     fd(50)
#     right(90)
#     fd(50)
#     right(90)

# B12
# width(5)
# color('purple')
# for _ in range(3):
#     right(90)
#     forward(50)
# up()
# fd(50)
# down()
# color('green')
# for _ in range(3):
#     fd(50)
#     right(90)

# B13
# color('green')
# width(5)
# for _ in range(8):
#     fd(50)
#     left(135)
#     fd(25)
#     right(90)
#     fd(25)
#     right(90)

# B14
# color('yellow')
# width(5)
# for _ in range(5):
#     fd(50)
#     right(120)
#     fd(100)
#     left(120)
#     fd(50)

#B15
# color('red')
# width(5)
# for _ in range(4):
#     fd(100)
#     circle(100,90)

#B16
# color('green')
# width(5)
# circle(200,90)
# seth(180)
# for _ in range(4):
#     circle(25,90)
#     circle(-25,90)

#B17
# color('blue')
# width(5)
# for _ in range(8):
#     circle(50,180)
#     left(120)

#B18
# color('yellow')
# width(5)
# for _ in range(8):
#     fd(200)
#     left(90)
#     fd(50)
#     left(45)

#B19
# color('cyan')
# width(5)
# for _ in range(4):
#     circle(50,180)
#     seth(0)
# up()
# seth(90)
# fd(50)
# down()
# for _ in range(4):
#     seth(180)
#     circle(50,180)

#B20
# color('cyan')
# width(5)
# seth(270)
# for _ in range(2):
#     fd(100)
#     circle(50,90)
# fd(50)
# for _ in range(2):
#     fd(100)
#     circle(50,90)
# fd(50)
# seth(0)
# fd(200)
# seth(270)
# fd(25)
# up()
# seth(180)
# fd(100)
# down()
# circle(50,180)
# circle(50,180)

#B21
# width(5)
# shift_color(0.5)
# for _ in range(6):
#     fd(100)
#     left(120)
#     fd(50)
#     left(120)
#     fd(100)
#     right(60)
#     fd(50)
#     right(120)
#     fd(50)
#     right(120)
#     up()
#     fd(100)
#     down()
#     shift_color(0.13)

# B22
# color('yellow')
# width(5)
# left(30)
# for _ in range(6):
#     fd(100)
#     left(60)
# right(150)
# color('red')
# for _ in range(3):
#     fd(100)
#     left(120)
# color('green')
# for _ in range(4):
#     fd(100)
#     right(90)
# left(60)
# for _ in range(6):
#     fd(100)
#     left(90)

#B23
# color('purple')
# width(5)
# left(45)
# for _ in range(2):
#     for _ in range(3):
#         fd(50)
#         right(90)
#         fd(50)
#         left(90)
#     right(135)
#     fd(50)
#     right(45)

#B24
# color('red')
# width(5)
# for _ in range(8):
#     fd(100)
#     left(135)
# fd(50)
# color('green')
# for _ in range(3):
#     right(135)
#     fd(100)
#     left(135)
#     fd(50)
# fd(50)
# right(90)
# fd(25)
# for _ in range(2):
#     left(90)
#     fd(25)
# right(90)
# fd(50)
# for _ in range(3):
#     fd(50)
#     left(135)
#     fd(100)
#     right(135)






input()