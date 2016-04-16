import turtle

def draw_square(elf):
    counter1= 0
    while counter1 <= 3:
        elf.forward(100)
        elf.left(90)
        counter1= counter1+1
def draw_shapes():
    window = turtle.Screen()
    window.bgcolor('red')
    brad = turtle.Turtle()
    brad.shape('turtle')
    for i in range (1,360):
        brad.left(1)
        draw_square(brad)
        i=i+1
    
    window.exitonclick()



draw_shapes()