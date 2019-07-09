# Simple Snake Game
# By @DipadityaDas

import turtle
import time
import random
delay = 0.1

# Setup the screen
window = turtle.Screen()
window.title("Snake Game by @DipadityaDas")
window.bgcolor("white")
window.setup(width=600, height=600)
window.tracer(0)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# Snake Direction Functions
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

def go_up():
    head.direction = "up"
    
def go_down():
    head.direction = "down"

def go_left():
    head.direction = "left"

def go_right():
    head.direction = "right"

# Keybindings
window.listen()
window.onkeypress(go_up, "8")
window.onkeypress(go_down, "2")
window.onkeypress(go_left, "4")
window.onkeypress(go_right, "6")


# Main Game Loop
while True:
    window.update()
    # Check for a collison with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        # Hide the Segments
        for segment in segments:
            segment.goto(1000, 1000)

    # Check for a collision with the food
    if head.distance(food) < 20:
        # Move the food to the random position
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)

        # Add segments
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

    # Move the end segment first 
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    
    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    
    move()
    
    time.sleep(delay)

window.mainloop()