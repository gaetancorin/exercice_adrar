# ////\\\\IMPORTANT  Les consignes de l'exercices sont sur le site suivant:  IMPORTANT/////\\\\
    
# //////\\\\\IMPORTANT   https://pcoupechoux.fr/exercices_p5.html  IMPORTANT/////\\\\\

########## EX 1 CERCLE SOURIS-----------

# def setup():   
#     size(950,1000)   
#     background(0)   
#     stroke(255) 
#     strokeWeight(5)   
# # def draw():   
# #     print (mouseX,mouseY)    
# def mouseClicked():    
#     noFill()     
#     circle(mouseX,mouseY,50)

############### EX 2 CERCLE SOURIS 2---------------

# def setup():
#     size(800,600)
#     background(0)
#     stroke(255)
#     strokeWeight(1)
    
# def draw():
#     circle(mouseX,mouseY, 50)
#     noFill()

########  EX 3 CHANGEMENT FORME------------------

# def setup():
#     size(800,600)
#     background(0)
#     stroke(255)
#     strokeWeight(3)
#     noFill()

# def draw():
#     if mouseY > 300:
#         background(0)
#         circle(400,300,100)
#     else:
#         background(0)
#         square(360,260,80)
        
# EX 4 CHANGEMENT TAILLE------------------------

# def setup():
#     size(800,600)
#     background(0)
#     stroke(255)
#     strokeWeight(3)
#     noFill()

# def draw():
#     a = mouseX
#     if mouseY > 300:
#         background(0)
#         circle(400,300,a)
#     else:
#         background(0)
#         square(400-a/2,300-a/2,a)
        
# EX 5 CHangement couleur--------------------------

# def setup():
#     size(800,600)
#     background(0)
#     stroke(255)
#     fill(0,0,0)
#     strokeWeight(3)
#     global b
#     b = 5
# def draw():
#     global b
#     a = mouseX
#     background(0)
#     if mouseY > 300:
#         circle(400,300,a)
#     else:
    
#         square(400-a/2,300-a/2,a)
#     fill(0,b,0)
#     b = (b +1)%255
    
# EX 6 differente couleur-----------------------

# def setup():
#     size(800,600)
#     background(0)
#     stroke(255)
#     fill(0,0,0)
#     strokeWeight(3)
#     global b
#     global c
#     b = 5
#     c = 0
# def draw():
#     global b
#     a = mouseX
#     background(0)
#     if mouseY > 300:
#         circle(400,300,a)
#     else:
#         square(400-a/2,300-a/2,a)
        
#     global c
#     if c ==0:
#         fill(0,b,0)
#     elif c ==1:
#         fill(b,0,0)
#     else:
#         fill(0,0,b)
#     b = (b +1)%255

# def mouseClicked():
#         global c
#         c = (c+1)%3

# EX 7 FORME COMPLIQUER------------------------

# def setup():
#     size(800,600)
#     background(0)
#     stroke(255)
#     strokeWeight(2)
#     noFill()
    
# def draw():
#     ellipse(400,300,50,50)
#     ellipse(400,300,100,100)
#     ellipse(400,300,50,100)
#     ellipse(400,300,100,50)

# EX 8 FORME COMPLIQUEES-------------------------

# def setup():
#     size(800,600)
#     background(0)
#     stroke(255)
#     strokeWeight(2)
#     noFill()
    
# def ellip(a,b):
#     ellipse(a,b,50,50)
#     ellipse(a,b,100,100)
#     ellipse(a,b,50,100)
#     ellipse(a,b,100,50)
    
# def draw():
#     background(0)
#     ellip(200,500)
#     ellip(600,500)
#     ellip(200,150)
#     ellip(600,150)
#     ellip(400,300)
#     ellip(mouseX,mouseY)

# EX 9 FORME COMPLIQUEES COULEUR--------------------

# def setup():
#     size(800,600)
#     background(0)
#     stroke(255)
#     strokeWeight(2)
#     noFill()
    
# def ellip(a,b,c):
#     stroke(255,0,0)
#     ellipse(a,b,c/2,c/2)
#     stroke(255)
#     ellipse(a,b,c,c)
#     ellipse(a,b,c/2,c)
#     ellipse(a,b,c,c/2)
    
# def draw():
#     background(0)
#     ellip(200,500,100)
#     ellip(600,500,100)
#     ellip(200,150,100)
#     ellip(600,150,100)
#     ellip(400,300,200)
#     ellip(mouseX,mouseY,50)

# EX 10 POINTS BLANCS---------------------------

# def setup():
#     size(800,600)
#     background(0)
#     stroke(255)
#     strokeWeight(3)

                     
# def draw():
#     for _ in range(500):
#         point(random(800),random(600))

# EX 11 POINTS COULEURS RANDOM--------------------

# def setup():
#     size(800,600)
#     background(0)
#     stroke(255)
#     strokeWeight(3)

                     
# def draw():
#     for _ in range(500):
#         stroke(random(255),random(255),random(255))
#         point(random(800),random(600))

# EX 12 POINTS COLORES BIEN ORGANISES-----------------

# def setup():
#     size(800,600)
#     background(0)
#     stroke(255)
#     strokeWeight(3)
                                          
# def draw():
#     for _ in range(1000):
#         b = random(800)
#         a = (b/800)*255
#         stroke(a,0,255)
#         point(b,random(600))
        
# EX 13 POINTS COLORES 4 COULEURS---------------------

# def setup():
#     size(800,600)
#     background(0)
#     stroke(255)
#     strokeWeight(3)
                                          
# def draw():
#     for _ in range(1000):
#         b = random(800)
#         a = (b/800)*255
#         d = random(600)
#         c = (d/600)*255
#         stroke(a,0,c)
#         point(b,d)
        
# EX 13 TOUR EQUATEUR-------------------------------

# def setup():
#     size(800,600)
#     background(0,0,255)
#     stroke(255,0,0)
#     strokeWeight(1)
#     fill(255,0,0)
#     global x
#     x = 1

# def draw():
#     background(0,0,255)
#     global x
#     circle(x,300,25)
#     x += 5
#     x = x%800
    
# EX 14 LE TOUR DU MONDE---------------------------

# def setup():
#     size(800,600)
#     background(0,0,255)
#     stroke(255,0,0)
#     strokeWeight(1)
#     fill(255,0,0)
#     global x
#     global y
#     x = 1
#     y = 1

# def draw():
#     background(0,0,255)
#     global x
#     global y
#     circle(x,y,25)
#     x += 7
#     x = x%800
#     y +=7
#     y = y%600
    
# EX 15 SBOING---------------------------------------

# def setup():
#     size(800,600)
#     background(0,0,255)
#     stroke(255,0,0)
#     strokeWeight(1)
#     fill(255,0,0)
#     global x
#     global y
#     x = 1
#     y = 0

# def draw():
#     background(0,0,255)
#     global x
#     global y
#     circle(x,300,25)
#     if x < 1 or x > 800:
#         y = (1 + y)%2
    
#     if y == 0:
#         x += 5
#     else:
#         x -= 5
        
################
# def setup():
#     size(800,600)
#     background(0,0,255)
#     stroke(255,0,0)
#     strokeWeight(1)
#     fill(255,0,0)
#     global a
#     global b
#     a = 1
#     b = +5

# def draw():
#     background(0,0,255)
#     global a
#     global b
#     circle(a,300,25)
#     if a < 1 or a > 800:
#         b *= -1 
#     a += b    

# EX 16 SBOING SBOING---------------------------------

# def setup():
#     size(800,600)
#     background(0,0,255)
#     stroke(255,0,0)
#     strokeWeight(1)
#     fill(255,0,0)
#     global x
#     global b
#     x = 1
#     b = +5
#     global y
#     global d
#     y = 1
#     d = +5

# def draw():
#     background(0,0,255)
#     global x
#     global b
#     global y
#     global d
#     circle(x,y,25)
#     if x < 1 or x > 800:
#         b *= -1 
#     x += b 
    
#     if y < 1 or y > 600:
#         d *= -1
#     y += d
    
# EX 17 BALLE ACCELERE-------------------------------

# def setup():
#     size(800,600)
#     background(0,0,255)
#     stroke(255,0,0)
#     fill(255,0,0)
#     global x, vx, y, vy
#     x = 5
#     vx = 25
#     y = 5
#     vy = 25
   
    
# def draw():
#     background(0,0,255)
#     global x, vx, y, vy
#     circle(x, y,50)
#     x = x + vx
#     if x > width or x < 0:
#         vx *= -1
#     y = y + vy
#     if y > height or y < 0:
#         vy *= -1
#     vx = vx*0.995
#     vy = vy*0.995
#     print(vx, vy)
    
# def mouseClicked():
#     global x, vx, y, vy
#     vx = vx*5
#     vy = vy*5
    
    
    
# EX 18 LIGNE DE CARRES-----------------------------

# def setup():
#     size(800,600)
#     background(255,255,255)
#     fill(0,0,0)
#     global x
#     x = 100
#     for _ in range(10):
#         square(x,100,40)
#         x = x + 50

# EX 19 GRILLE DE CARRES------------------------------

def setup():
    size(800,600)
    background(255,255,255)
    fill(0,0,0)
    global x, y
    x = 100
    y = 100
    for _ in range(10):
        square(x,y,40)
        for _ in range(7):
            square(x, y, 40)
            y = y + 50
        x = x + 50
        y = 100
