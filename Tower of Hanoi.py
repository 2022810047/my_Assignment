import turtle

def move_tower(height, from_pole, to_pole, with_pole):
    if height >= 1:
        move_tower(height - 1, from_pole, with_pole, to_pole)
        
        move_disk(from_pole, to_pole)                           # 탑 원판 옮기기
        
        move_tower(height - 1, with_pole, to_pole, from_pole)


def move_disk(from_p, to_p):
    print("{0}에서 {1}로 탑 원판 옮기기".format(from_p, to_p))
    moving(from_p, to_p)


def moving(from_p, to_p):
  pole_dict = {"A":-50, "B":50, "C":150}
  for i in [disk3, disk2, disk1]:
    the_pos = list(i.position())
    
    if from_p == "A":
      if the_pos[0] == -50:
        i.goto(pole_dict[to_p], the_pos[1])
        break
        
    elif from_p == "B":
      if the_pos[0] == 50:
        i.goto(pole_dict[to_p], the_pos[1])
        break
    
    elif from_p == "C":
      if the_pos[0] == 150:
        i.goto(pole_dict[to_p], the_pos[1])
        break


disk1, disk2, disk3 = turtle.Turtle(), turtle.Turtle(), turtle.Turtle()
def setting_player(i, y):
  i.shape("circle")
  i.up()
  i.goto(-50, y)
setting_player(disk1, 0)
setting_player(disk2, 30)
setting_player(disk3, 60)

def setting_map(x,alpabet):
  line = turtle.Turtle()
  line.up()
  line.goto(x,-30)
  line.write(alpabet)
  line.left(90)
  line.down()
  line.color("brown")
  line.forward(100)
  line.hideturtle()
setting_map(-50, "--A")
setting_map(50, "--B")
setting_map(150, "--C")

my_win = turtle.Screen()
move_tower(3, "A", "B", "C")
my_win.exitonclick()
