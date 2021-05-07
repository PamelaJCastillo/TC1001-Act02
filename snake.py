"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to arrow keys.

"""

from turtle import *
from random import randrange
from random import shuffle
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-20, 20) * 10
        food.y = randrange(-20, 20) * 10
    else:
        snake.pop(0)
        p=[1,2]
        shuffle (p)
        if p[0]==1:
            delay(2000)
            m=[-2,2]
            shuffle(m)
            food.x = food.x + m[0]
        else:
            delay (2000)
            m=[-2,2]
            shuffle(m)
            food.y = food.y + m[0]

    clear()

    for body in snake:
        square(body.x, body.y, 9, bodyColor)

    square(food.x, food.y, 9,foodColor)
    update()
    ontimer(move, 100)

#Se crea una lista con los colores a asignar aleatoriamente.
colorList = ["orange", "green", "purple", "blue", "black"]
#Se obtiene un numero random, y se obtiene un color aleatorio de la lista
#Color de la serpiente
randNum = randrange(0, 4)
bodyColor = colorList[randNum]
#Color de la comida
randNum2 = randrange(0,4)
foodColor = colorList[randNum2]

#Un while para que no se repita el color
while bodyColor == foodColor:
    randNum2 = randrange(0,4)
    foodColor = colorList[randNum2]

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
