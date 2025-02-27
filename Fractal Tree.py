import turtle
import random

def tree(branch_len, branch_size, dec_list, num, t):
    if branch_len >= 15:
        t.pensize(branch_size)
        branch_color(branch_len, t)
        
        t.down()
        t.forward(branch_len)
        
        angle = random.randint(15,45)
        t.right(angle)
        
        tree(branch_len - dec_list[num+1], branch_size - 5, dec_list, num, t)
        
        t.down()
        t.left(angle*2)
        
        tree(branch_len - dec_list[num+1], branch_size - 5, dec_list, num, t)
        
        t.right(angle)
        t.up()
        t.backward(branch_len)

def branch_color(branch_len, t):
  color = ["#53ff00","#53cb00","#53a900","#608e00","#677400","#6f6500","#744f00","#803900"]
  t.pencolor(color[int(branch_len/10)])

#조건4: 같은 높이의 가지는 길이가 같아야 한다. 가지의 길이는 적당한 범위 내여야 한다.
dec_list = [random.randint(10,15),random.randint(10,15),random.randint(10,15),
random.randint(10,15),random.randint(10,15),random.randint(10,15),random.randint(10,15)]

t = turtle.Turtle()
my_win = turtle.Screen()
t.left(90)
t.up()
t.backward(100)
t.down()

tree(75, 30, dec_list, 1, t)

t.hideturtle()
my_win.exitonclick()
