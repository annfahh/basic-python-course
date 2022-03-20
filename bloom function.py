import turtle
t=turtle.Pen()
t.shape('turtle')

def bloomL():
    '''to draw plot of flowers'''
    for i in range(12):
        t.circle(20)
        t.left(30)

def bloomM():
    '''to draw plot of flowers'''
    for i in range(12):
        t.circle(12)
        t.left(30)

def bloomS():
    '''to draw plot of flowers'''
    for i in range(6):
        t.circle(8)
        t.left(60)

def GO(x,y):
    '''to move turtle w penup'''
    t.penup()
    t.goto(x,y)
    t.pendown()

bloomL()
GO(250,100)
bloomL()
GO(80,130)
bloomL()
GO(-30,150)
bloomL()
GO(-150,80)
bloomL()
GO(-70,-60)
bloomL()
GO(50,-120)
bloomS()
GO(200,60)
bloomS()
GO(20,90)
bloomS()
GO(-30,15)
bloomS()
GO(-80,50)
bloomS()
GO(-100,-150)
bloomS()
GO(30,-60)
bloomS()
GO(90,-100)
bloomM()
GO(120,180)
bloomM()
GO(-60,90)
bloomM()
GO(-120,75)
bloomM()
