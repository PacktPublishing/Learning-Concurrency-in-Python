import turtle

turtle.setup(500,500)                
window = turtle.Screen()              
window.title("Event Handling 101!")     
window.bgcolor("lightblue")             
nathan = turtle.Turtle()  

def moveForward():
    nathan.forward(50)

def moveLeft():
    nathan.left(30)

def moveRight():
    nathan.right(30)

def start():  
    window.onkey(moveForward, "Up")
    window.onkey(moveLeft, "Left")
    window.onkey(moveRight, "Right")
    window.listen()
    window.mainloop()

if __name__ == '__main__':
    start()