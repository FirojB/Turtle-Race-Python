import turtle as t
import random

screen = t.Screen()
screen.setup(width = 500, height = 400)
screen.title('Turtle Race')
colors_list = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]
my_turtle = ['']

def colors():
    colours = random.choice(colors_list)
    colors_list.remove(colours)
    return colours

my_turtle[0] = t.Turtle('turtle')

def no_of_tutrle(n):
    for i in range(1,n):
        my_turtle.append(i)
        my_turtle[i] = t.Turtle('turtle')
        my_turtle[i].color(colors())
        my_turtle[i].penup()
        my_turtle[i].goto(-240,i*20)
        my_turtle[i].pendown()
        my_turtle[i].clear()

def race(choice):
    flag = True
    while flag:
        for i in range(0, len(my_turtle)):
            my_turtle[i].penup()
            my_turtle[i].forward(random.randint(0,20))
            my_turtle[i].pendown()
            if my_turtle[i].xcor()>=225:
                if my_turtle[i].pencolor() == choice:
                    print( '**** You are Winner ***** ')
                else:
                    print(f" You loose!!!, but {my_turtle[i].pencolor()} - is Winner")
                flag = False
choice = screen.textinput(title= ' Enter your choice ', prompt= 'Which colour you choose').lower()
qty = int(screen.textinput(title= ' Enter your choice ', prompt= "how many Turtles\n (max -6"))

my_turtle[0].color(choice)
colors_list.remove(choice)
my_turtle[0].penup()
my_turtle[0].goto(-240, 0)
no_of_tutrle(qty)
race(choice)

screen.exitonclick()
