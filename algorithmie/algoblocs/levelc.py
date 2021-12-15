from turtle import *
speed(9)
current_color = 0
def shift_color(n):
    global current_color
    current_color += n
    current_color %= 1
    t = [(1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(1,0,0)]
    n1 = int(6*current_color)
    n2 = n1+1
    w1 = 6*current_color-n1
    w2 = 1-w1
    color(t[n1][0]*w2+t[n2][0]*w1,t[n1][1]*w2+t[n2][1]*w1,t[n1][2]*w2+t[n2][2]*w1)

# C1
# color('cyan')
# width(5)
# for _ in range(4):
#     for _ in range(3):
#         fd(100)
#         right(120)
#     fd(100)

# C2
# color('purple')
# width(5)
# seth(90)
# for _ in range(5):
#     for _ in range(4):
#         fd(50)
#         right(90)
#     up()
#     fd(100)
#     down()

# C3
# width(5)
# shift_color(0.4)
# for _ in range(3):
#     for _ in range(8):
#         fd(100)
#         left(135)
#     up()
#     fd(200)
#     down()
#     shift_color(0.1)

# C4
# color('red')
# width(5)
# for _ in range(5):
#     for _ in range(3):
#         fd(50)
#         left(120)
#     color('orange')
#     for _ in range(4):
#         fd(50)
#         right(90)
#     up()
#     fd(100)
#     down()
#     color('red')

# C5
# width(5)
# shift_color(0.2)
# for _ in range(4):
#     for _ in range(8):
#         fd(200)
#         left(135)
#     right(90)
#     shift_color(0.2)

# C6
# width(5)
# color('yellow')
# for _ in range(3):
#     for _ in range(5):
#         fd(100)
#         left(120)
#     right(120)

# C7
# color('orange')
# width(5)
# for _ in range(8):
#     for _ in range(3):
#         fd(50)
#         right(120)
#     fd(50)
#     left(45)

# C8
# width(5)
# color('green')
# seth(90)
# fd(200)
# right(45)
# for _ in range(4):
#     color('red')
#     for _ in range(3):
#         fd(100)
#         right(120)
#     color('yellow')
#     fd(100)
#     left(90)

# C9
# color('green')
# width(5)
# for _ in range(3):
#     for _ in range(3):
#         for _ in range(4):
#             right(90)
#             fd(50)
#         fd(50)
#         right(120)
#     left(120)
#     fd(200)

# C10
# color('red')
# width(5)
# seth(270)
# for _ in range(4):
#     for _ in range(4):
#         fd(50)
#         for _ in range(4):
#             left(90)
#             fd(25)
#         right(90)
#     fd(100)

# C11
# width(5)
# shift_color(0.5)
# for _ in range(6):
#     for _ in range(6):
#         for _ in range(4):
#             fd(50)
#             left(120)
#         right(60)
#     up()
#     fd(100)
#     right(60)
#     down()
#     shift_color(0.13)

# C12
# color('yellow')
# width(5)
# for _ in range(4):
#     for _ in range(2):
#         circle(50,90)
#         fd(50)
#         left(90)
#     circle(-50,45)
# color('blue')
# circle(-50,180)
# left(120)
# circle(100,300)










input()