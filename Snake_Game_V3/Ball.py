
class Ball:

    def __init__(self,canvas,x,y,diameter,xVelocity,yVelocity,color):
        self.canvas = canvas
        self.ball_picture = canvas.create_oval(x,y,diameter,diameter,fill=color)
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity

    def move(self):
        coordinate = self.canvas.coords(self.ball_picture)
        if coordinate[2] >= (self.canvas.winfo_width()) or coordinate[0] <= 0:
            self.xVelocity = -self.xVelocity
        if coordinate[3] >= (self.canvas.winfo_width()) or coordinate[1] <= 0:
            self.yVelocity = -self.yVelocity
        self.canvas.move(self.ball_picture,self.xVelocity,self.yVelocity)



    def close_enough(self,snake):
        coordinate = self.canvas.coords(self.ball_picture)
        x, y = snake.coordinates[0]
        print(snake.coordinates[0])
        print(coordinate)
        if abs(x - coordinate[0]) <= 3 or abs(x - coordinate[2]) <= 3 or abs(y - coordinate[1]) <= 3 or abs(
                y - coordinate[3]) <= 3:
            return True