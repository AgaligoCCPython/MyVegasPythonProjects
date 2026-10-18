import turtle
screen = turtle.Screen()
screen.setup(width=800, height=600)

t = turtle.Turtle()
t.speed(0)

def draw_line(x0, y0, x1, y1 ):
    t.penup()
    t.goto(x0, y0)
    t.pendown()
    t.goto(x1, y1)

def draw_rectagle(x0, y0, len, hgt, clr):
    t.fillcolor(clr)
    t.begin_fill()
    draw_line(x0, y0, x0+len, y0)
    draw_line(x0+len, y0, x0+len, y0+hgt)
    draw_line(x0+len, y0+hgt, x0, y0+hgt)
    draw_line(x0, y0+hgt, x0, y0)
    t.end_fill()


#row 0
x_val = -300
y_val = 0

draw_rectagle(x_val,y_val,20,20,'dark green')
x_val = x_val + 20
draw_rectagle(x_val,y_val,20,20,'GreenYellow')
x_val = x_val + 20
draw_rectagle(x_val,y_val,20,20,'black')
x_val = x_val + 20
draw_rectagle(x_val,y_val,20,20,'GreenYellow')
x_val = x_val + 20
draw_rectagle(x_val,y_val,20,20,'dark green')
x_val = x_val + 20
for jj in range(9):
    draw_rectagle(x_val,y_val,20,20,'GreenYellow')
    x_val = x_val + 20
draw_rectagle(x_val,y_val,20,20,'dark green')
x_val = x_val + 20
draw_rectagle(x_val,y_val,20,20,'dark green')
x_val = x_val + 20
draw_rectagle(x_val,y_val,20,20,'GreenYellow')
x_val = x_val + 20
draw_rectagle(x_val,y_val,20,20,'dark green')
x_val = x_val + 20
draw_rectagle(x_val,y_val,20,20,'dark green')
x_val = x_val + 20
for jj in range(6):
    draw_rectagle(x_val,y_val,20,20,'GreenYellow')
    x_val = x_val + 20
draw_rectagle(x_val,y_val,20,20,'dark green')
x_val = x_val + 20.

#row1
x_val = -280
y_val = 20

for jj in range(3):
    draw_rectagle(x_val,y_val,20,20,'dark green')
    x_val = x_val + 20
x_val = x_val + 20
draw_rectagle(x_val,y_val,20,20,'dark green')
x_val = x_val + 20
for jj in range(6):
    draw_rectagle(x_val,y_val,20,20,'GreenYellow')
    x_val = x_val + 20
draw_rectagle(x_val,y_val,20,20,'dark green')
x_val = x_val + 20
for jj in range(7):
    draw_rectagle(x_val,y_val,20,20,'GreenYellow')
    x_val = x_val + 20
for jj in range(3):
    draw_rectagle(x_val,y_val,20,20,'dark green')
    x_val = x_val + 20
draw_rectagle(x_val,y_val,20,20,'GreenYellow')
x_val = x_val + 20
draw_rectagle(x_val,y_val,20,20,'GreenYellow')
x_val = x_val + 20
draw_rectagle(x_val,y_val,20,20,'dark green')
x_val = x_val + 20

#row 2 
x_val = -180
y_val = 40

draw_rectagle(x_val,y_val,20,20,'dark green')
x_val = x_val + 20
draw_rectagle(x_val,y_val,20,20,'GreenYellow')
x_val = x_val + 20
draw_rectagle(x_val,y_val,20,20,'white')
x_val = x_val + 20
draw_rectagle(x_val,y_val,20,20,'black')
x_val = x_val + 20
draw_rectagle(x_val,y_val,20,20,'GreenYellow')
x_val = x_val + 20
draw_rectagle(x_val,y_val,20,20,'GreenYellow')
x_val = x_val + 20
draw_rectagle(x_val,y_val,20,20,'dark green')
x_val = x_val + 20
draw_rectagle(x_val,y_val,20,20,'dark green')
x_val = x_val + 20
for jj in range(3):
    draw_rectagle(x_val,y_val,20,20,'GreenYellow')
    x_val = x_val + 20
    draw_rectagle(x_val,y_val,20,20,'dark green')
    x_val = x_val + 20
x_val = x_val + 60
draw_rectagle(x_val,y_val,20,20,'dark green')
x_val = x_val + 20
draw_rectagle(x_val,y_val,20,20,'GreenYellow')
x_val = x_val + 20
draw_rectagle(x_val,y_val,20,20,'GreenYellow')
x_val = x_val + 20
draw_rectagle(x_val,y_val,20,20,'dark green')
x_val = x_val + 20

#row 3
x_val = -180
y_val = 60

draw_rectagle(x_val,y_val,20,20,'dark green')
x_val = x_val + 20
draw_rectagle(x_val,y_val,20,20,'GreenYellow')
x_val = x_val + 20
draw_rectagle(x_val,y_val,20,20,'black')
x_val = x_val + 20
draw_rectagle(x_val,y_val,20,20,'black')
x_val = x_val + 20
draw_rectagle(x_val,y_val,20,20,'GreenYellow')
x_val = x_val + 20
draw_rectagle(x_val,y_val,20,20,'dark green')
x_val = x_val + 20
x_val = x_val + 40
for jj in range(3):
    draw_rectagle(x_val,y_val,20,20,'dark green')
    x_val = x_val + 40
x_val = x_val + 80
draw_rectagle(x_val,y_val,20,20,'dark green')
x_val = x_val + 20
draw_rectagle(x_val,y_val,20,20,'GreenYellow')
x_val = x_val + 20
draw_rectagle(x_val,y_val,20,20,'dark green')
x_val = x_val + 20

#row 4

x_val = -160
y_val = 80

draw_rectagle(x_val,y_val,20,20,'dark green')
x_val = x_val + 20
draw_rectagle(x_val,y_val,20,20,'GreenYellow')
x_val = x_val + 20
draw_rectagle(x_val,y_val,20,20,'GreenYellow')
x_val = x_val + 20
draw_rectagle(x_val,y_val,20,20,'dark green')
x_val = x_val + 20
x_val = x_val + 260
draw_rectagle(x_val,y_val,20,20,'dark green')
x_val = x_val + 20
draw_rectagle(x_val,y_val,20,20,'GreenYellow')
x_val = x_val + 20
draw_rectagle(x_val,y_val,20,20,'dark green')
x_val = x_val + 20

#row 5

x_val = -140
y_val = 100

draw_rectagle(x_val,y_val,20,20,'dark green')
x_val = x_val + 20
draw_rectagle(x_val,y_val,20,20,'dark green')
x_val = x_val + 20
x_val = x_val + 300
draw_rectagle(x_val,y_val,20,20,'dark green')
x_val = x_val + 20
y_val = y_val + 20
draw_rectagle(x_val,y_val,20,20,'dark green')
x_val = x_val + 20

#row -1

x_val = -300
y_val = -20

draw_rectagle(x_val,y_val,20,20,'dark green')
x_val = x_val + 20
for jj in range(6):
    draw_rectagle(x_val,y_val,20,20,'GreenYellow')
    x_val = x_val + 20
draw_rectagle(x_val,y_val,20,20,'dark green')
x_val = x_val + 20
for jj in range(16):
    draw_rectagle(x_val,y_val,20,20,'GreenYellow')
    x_val = x_val + 20
draw_rectagle(x_val,y_val,20,20,'dark green')
x_val = x_val + 20

#row -2

x_val = -280
y_val = -40

for jj in range(6):
    draw_rectagle(x_val,y_val,20,20,'dark green')
    x_val = x_val + 20
for jj in range(5):
    draw_rectagle(x_val,y_val,20,20,'GreenYellow')
    x_val = x_val + 20
draw_rectagle(x_val,y_val,20,20,'dark green')
x_val = x_val + 20
for jj in range(10):
    draw_rectagle(x_val,y_val,20,20,'GreenYellow')
    x_val = x_val + 20
draw_rectagle(x_val,y_val,20,20,'dark green')
x_val = x_val + 20

#row -3

x_val = -260
y_val = -60

draw_rectagle(x_val,y_val,20,20,'dark green')
x_val = x_val + 20
for jj in range(8):
    draw_rectagle(x_val,y_val,20,20,'GreenYellow')
    x_val = x_val + 20
draw_rectagle(x_val,y_val,20,20,'dark green')
x_val = x_val + 20
for jj in range(10):
    draw_rectagle(x_val,y_val,20,20,'GreenYellow')
    x_val = x_val + 20
draw_rectagle(x_val,y_val,20,20,'dark green')
x_val = x_val + 20

#row -4

x_val = -240
y_val = -80

for jj in range(8):
    draw_rectagle(x_val,y_val,20,20,'dark green')
    x_val = x_val + 20
draw_rectagle(x_val,y_val,20,20,'white')
x_val = x_val + 20
for jj in range(4):
    draw_rectagle(x_val,y_val,20,20,'dark green')
    x_val = x_val + 20
draw_rectagle(x_val,y_val,20,20,'GreenYellow')
x_val = x_val + 20
for jj in range(4):
    draw_rectagle(x_val,y_val,20,20,'dark green')
    x_val = x_val + 20
draw_rectagle(x_val,y_val,20,20,'GreenYellow')
x_val = x_val + 20
draw_rectagle(x_val,y_val,20,20,'GreenYellow')
x_val = x_val + 20
draw_rectagle(x_val,y_val,20,20,'dark green')
x_val = x_val + 20

#row -6

x_val = -80
y_val = -100

draw_rectagle(x_val,y_val,20,20,'dark green')
x_val = x_val + 20
draw_rectagle(x_val,y_val,20,20,'GreenYellow')
x_val = x_val + 20
draw_rectagle(x_val,y_val,20,20,'dark green')
x_val = x_val + 20
x_val = x_val + 20
draw_rectagle(x_val,y_val,20,20,'dark green')
x_val = x_val + 20
draw_rectagle(x_val,y_val,20,20,'GreenYellow')
x_val = x_val + 20
draw_rectagle(x_val,y_val,20,20,'dark green')
x_val = x_val + 20
draw_rectagle(x_val,y_val,20,20,'dark green')
x_val = x_val + 20
draw_rectagle(x_val,y_val,20,20,'GreenYellow')
x_val = x_val + 20
draw_rectagle(x_val,y_val,20,20,'dark green')
x_val = x_val + 20
draw_rectagle(x_val,y_val,20,20,'GreenYellow')
x_val = x_val + 20
draw_rectagle(x_val,y_val,20,20,'GreenYellow')
x_val = x_val + 20
draw_rectagle(x_val,y_val,20,20,'dark green')
x_val = x_val + 20

#row -7

x_val = -60
y_val = -120

draw_rectagle(x_val,y_val,20,20,'dark green')
x_val = x_val + 20
draw_rectagle(x_val,y_val,20,20,'dark green')
x_val = x_val + 20
x_val = x_val + 40
for jj in range(4):
    draw_rectagle(x_val,y_val,20,20,'dark green')
    x_val = x_val + 20
x_val = x_val + 20
draw_rectagle(x_val,y_val,20,20,'dark green')
x_val = x_val + 20
draw_rectagle(x_val,y_val,20,20,'dark green')
x_val = x_val + 20

#grass

x_val = -400
y_val = -140

for jj in range(20):
    draw_rectagle(x_val,y_val,20,20,'green4')
    x_val = x_val + 20
    draw_rectagle(x_val,y_val,20,20,'green1')
    x_val = x_val + 20

x_val = -400
y_val = -160

for jj in range(20):
    draw_rectagle(x_val,y_val,20,20,'green1')
    x_val = x_val + 20
    draw_rectagle(x_val,y_val,20,20,'green4')
    x_val = x_val + 20

#soil

x_val = -400
y_val = -180
for jj in range(2):
    for jj in range(20):    
        draw_rectagle(x_val,y_val,20,20,'chocolate1')
        x_val = x_val + 20
        draw_rectagle(x_val,y_val,20,20,'dark goldenrod')
        x_val = x_val + 20
    x_val = -400
    y_val = y_val - 20
    for jj in range(20):    
        draw_rectagle(x_val,y_val,20,20,'dark goldenrod')
        x_val = x_val + 20
        draw_rectagle(x_val,y_val,20,20,'chocolate1')
        x_val = x_val + 20
y_val = -220

for jj in range(2):
    for jj in range(20):    
        draw_rectagle(x_val,y_val,20,20,'DarkGoldenrod1')
        x_val = x_val + 20
        draw_rectagle(x_val,y_val,20,20,'DarkGoldenrod3')
        x_val = x_val + 20
    x_val = -400
    y_val = y_val - 20
    for jj in range(20):    
        draw_rectagle(x_val,y_val,20,20,'DarkGoldenrod3')
        x_val = x_val + 20
        draw_rectagle(x_val,y_val,20,20,'DarkGoldenrod1')
        x_val = x_val + 20
x_val = -400
y_val = -260
for jj in range(2):
    for jj in range(20):    
        draw_rectagle(x_val,y_val,20,20,'DarkGoldenrod1')
        x_val = x_val + 20
        draw_rectagle(x_val,y_val,20,20,'DarkGoldenrod3')
        x_val = x_val + 20
    x_val = -400
    y_val = y_val - 20
    for jj in range(20):    
        draw_rectagle(x_val,y_val,20,20,'DarkGoldenrod3')
        x_val = x_val + 20
        draw_rectagle(x_val,y_val,20,20,'DarkGoldenrod1')
        x_val = x_val + 20

turtle.mainloop()