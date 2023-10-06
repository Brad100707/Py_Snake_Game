from tkinter import *
import random

Game_Width=700
Game_Height=700
Speed=50
Space_Size = 50
Body_Parts = 3
Snake_Color="#00FF00"
Food_Color="#FF0000"
BackGround_Color="#000000"

class Snake:
    def __init__(self):
        self.body_size = Body_Parts
        self.coordinates = []
        self.squares = []

        for i in range(0,Body_Parts):
            self.coordinates.append([0,0])



        for x,y in self.coordinates:
            square = canvas.create_rectangle(x,y,x+Space_Size,y+Space_Size, fill=Snake_Color,tag="snake")
            self.squares.append(square)

class Food:
    def __init__(self):
        x = random.randint(0, (Game_Width/Space_Size)-2) *Space_Size
        y = random.randint(0, (Game_Height / Space_Size) - 2) * Space_Size

        self.coordinate = [x,y]

        canvas.create_rectangle(x,y,x+Space_Size-10,y+Space_Size-10, fill="red", tag="food")
def change_direction(new_direction):
    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = 'left'
    elif new_direction == 'right':
        if direction != 'left':
            direction =new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction =new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction =new_direction

def next_turn(snake,food):
    x, y = snake.coordinates[0]

    if direction == "up":
        y -= Space_Size
    elif direction == "down":
        y += Space_Size
    elif direction == "left":
        x -= Space_Size
    elif direction == "right":
        x += Space_Size

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x + Space_Size, y + Space_Size, fill=Snake_Color)

    snake.squares.insert(0, square)

    if x == food.coordinate[0] and y == food.coordinate[1]:

        global score

        score+=1

        label.config(text="Score:{}".format(score))

        canvas.delete("food")

        food = Food()

    else:
        print(snake.coordinates)

        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

        print(snake.coordinates)

    if collision(snake):
        Game_Over()
    else:
        window.after(100, next_turn, snake,food)

def collision(snake):
    x,y = snake.coordinates[0]

    if x > Game_Width or x<0:
        return True
    elif y > Game_Height or y<0:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False

def Game_Over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2,canvas.winfo_height()/2,text="Game Over", fill="red",font=("consolas",70))

window = Tk()

window.title("New Snake Game")


score = 0
direction = "down"

window.geometry(f"{Game_Width}x{Game_Height}+{int(window.winfo_screenwidth()/2-window.winfo_screenwidth()/4)}+{0}")



label = Label(window, text="Score:{}".format(score),font=("consolas",40))
label.pack()

canvas = Canvas(bg="black",height=Game_Height, width=Game_Width)
canvas.pack()

window.bind('<Left>', lambda event : change_direction('left'))
window.bind('<Right>', lambda event : change_direction('right'))
window.bind('<Up>', lambda event : change_direction('up'))
window.bind('<Down>', lambda event : change_direction('down'))


snake = Snake()
food = Food()

next_turn(snake,food)

window.mainloop()
