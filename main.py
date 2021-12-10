from snake import Snake
from food import Food
from scoreboard import Scoreboard
from turtle import Screen
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My first Snake Game')
screen.tracer(0)

# Creating the instance 
snake = Snake()
food = Food()
score = Scoreboard()
# Listening the input for the movement of snake  
screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')

game_is_on = True
score_num = 0
score.change_num(score_num)

while game_is_on:
  screen.update()
  time.sleep(0.1)
  snake.move()
  
  #Detecting the collision
  if snake.snake_body[0].distance(food)<15:
    food.refresh_food()
    snake.extend_body()
    score_num+=1
    score.clear()
    score.change_num(score_num)
  
  if snake.snake_body[0].xcor()>280 or snake.snake_body[0].xcor()<-280 or snake.snake_body[0].ycor()>280 or snake.snake_body[0].ycor()<-280:
    score.game_over()
    game_is_on=False

  for body in snake.snake_body:
    if body == snake.snake_body[0]:
      pass
    elif snake.snake_body[0].distance(body) <= 10:
      score.game_over()
      game_is_on=False
            
        

screen.exitonclick()