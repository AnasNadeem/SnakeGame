from turtle import Turtle

class Snake:
  def __init__(self):
    # Snake body list 
    self.snake_body = []
    self.starting_positions = [(0,0),(-20,0),(-40,0)]
    self.create_snake()

  def create_snake(self):
    # Creating the body 
    # for i in range(1,4):
    for position in self.starting_positions:
      self.create_body(position)            

  def create_body(self, position):
    t =Turtle('square')
    t.penup()
    t.fillcolor('white')
    # x_axis = 20-(20*i)
    # t.goto(x=x_axis,y=0)
    t.goto(position)
    self.snake_body.append(t)

  def extend_body(self):
    # self.create_body(len(self.snake_body))
    self.create_body(self.snake_body[-1].position())

  def move(self):
    for body_num in range(len(self.snake_body)-1, 0, -1):
      body_bef_x_axis = self.snake_body[body_num-1].xcor()
      body_bef_y_axis = self.snake_body[body_num-1].ycor()
      self.snake_body[body_num].goto(body_bef_x_axis,body_bef_y_axis)
    self.snake_body[0].forward(20)

  def up(self):
    if self.snake_body[0].heading() == 270:
      pass
    else:
      self.snake_body[0].setheading(90)

  def down(self):
    if self.snake_body[0].heading() == 90:
      pass
    else:
      self.snake_body[0].setheading(270)

  def right(self):
    if self.snake_body[0].heading() == 180:
      pass
    else:
      self.snake_body[0].setheading(0)

  def left(self):
    if self.snake_body[0].heading() == 0:
      pass
    else:
      self.snake_body[0].setheading(180)