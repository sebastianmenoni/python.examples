import turtle

def draw_square(some_turtle):
    
    for i in range(4):

        some_turtle.forward(100)
        some_turtle.right(90)
        
def draw_art():

    window = turtle.Screen()
    window.bgcolor("blue")
    
    giva = turtle.Turtle()
    giva.color("white")
    giva.speed(0)

    for i in range(360):
  
        draw_square(giva)
        giva.seth(i)
        

    turtle.exitonclick()

draw_art()

