from turtle import Turtle

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.hideturtle()
    self.color('white')
    self.penup()

  def game_over(self):
    self.goto(0,0)
    self.write('Game Over', move=False, align="center",  font=("Arial", 20, "normal"))

  def change_num(self, num):
    self.goto(-20,270)
    self.write(f'Score = {num}', move=False, align="center",  font=("Arial", 16, "normal"))