from random import randrange

def setup():
    global all_x, all_vx, all_y, all_vy, all_color_r, all_color_g, all_color_b, super_ball
    size(1000, 800)
    stroke(255, 0, 0)
    strokeWeight(1)
    ball= randrange(1,3)
    super_ball = []
    all_x = []
    all_vx = []
    all_y = []
    all_vy = []
    all_color_r = []
    all_color_g = []
    all_color_b = []
    for i in range(ball):
        super_ball.append(i)
        all_x.append(randrange(5,(width-5)))
        all_vx.append(randrange(-5,10))
        all_y.append(randrange(5,(height-5)))
        all_vy.append(randrange(-5,10))
        all_color_r.append(randrange(0,255))
        all_color_g.append(randrange(0,255))
        all_color_b.append(randrange(0,255))
    

# x = 50
# vx = 3
# y = 225
# vy = 10

# x2 = 150
# vx2 = 3
# y2 = 325
# vy2 = 10



def draw():
    background(0, 0, 255)
    
    # global x,y, vx, vy
    # point(x, y)
    # x += vx
    # if x >= 400 or x < 0:
    #     vx = -vx
    # y += vy
    # if y >= 550 or y < 0:
    #     vy = -vy
        
    # global x2,y2, vx2, vy2
    # point(x2, y2)
    # x2 += vx2
    # if x2 >= 400 or x2 < 0:
    #     vx2 = -vx2
    # y2 += vy2
    # if y2 >= 550 or y2 < 0:
    #     vy2 = -vy2
    
    global all_x, all_y, all_vx, all_vy, all_color_r, all_color_g, all_color_b, super_ball
    for i in range(len(all_x)):

        circle(all_x[i], all_y[i],50)
        fill(all_color_r[i],all_color_g[i],all_color_b[i])
        stroke(all_color_r[i],all_color_g[i],all_color_b[i])
        all_x[i] += all_vx[i]
        if all_x[i] >= width or all_x[i] < 0:
            all_vx[i] = -all_vx[i]
        all_y[i] += all_vy[i]
        if all_y[i] >= height or all_y[i] < 0:
            all_vy[i] = -all_vy[i]
        for ALL in range(len(all_x)):
            if all_x[i]-50 or all_y[i]+50 < all_x[ALL] or all_x[ALL] < all_x[i]+50 or all_y[i]+50:
                print('aie')
            else:
                pass
                
