import turtle

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor('red')
    brad = turtle.Turtle()
    brad.shape('turtle')
    for i in range(1,37):  
        brad.left(35)
        brad.forward(50)
        brad.right(35)
        brad.forward(50)
        brad.right(145)
        brad.forward(50)
        brad.right(35)
        brad.forward(50)
        brad.right(10)
    
    window.exitonclick()

draw_shapes()