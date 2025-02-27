import turtle
import random

wn = turtle.Screen()
player_name = ["t1","t2","t3","t4","t5","t6","t7","t8","t9","t10"]
player_list = []
start_y = 150
player_num = 1

for player in player_name:
  player = turtle.Turtle()
  player.speed(0)
  player.penup()
  player.shape("turtle")
  player.goto(-150,start_y)
  player.write("t{0}".format(player_num))
  player_num += 1
  player.right(90)
  player.forward(10)
  player.left(90)
  start_y -= 30
  player.speed(1)
  player.pendown()
  player_list.append(player)
  
line = turtle.Turtle()
line.speed(0)
line.color("red")
line.penup()
line.goto(150,300)
line.right(90)
line.pendown()
line.forward(600)
line.hideturtle()

game_end = 0
while game_end == 0:
  for t in player_list:
    Die = [1,2,3,4,5,6]
    die_num = 20 * random.choice(Die)
    t.forward(die_num)
    if t.xcor() >= 150:
      t.color("red")
      game_end = 1
      break
