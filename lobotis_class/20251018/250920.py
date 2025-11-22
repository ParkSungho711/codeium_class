import turtle as t

# 삼각형 거북이
# t.home()
# t.shape("turtle")
# t.color('green')
# t.begin_fill()
# for i in range(3):
#     t.forward(100)
#     t.left(120)
#     t.color('blue')
# t.end_fill()

# 그래픽 동그라미
# t.home()
# t.shape('turtle')
# n = 50
# t.bgcolor('black')
# t.color('green')
# t.speed(0)
# for i in range(n):
#     t.circle(80)
#     t.right(360/n)

# 그래픽 네모
# t.home()
# t.shape('turtle')
# a = 89
# t.bgcolor('black')
# t.color('green')
# t.speed(3)
# for i in range(200):
#     t.forward(i)
#     t.left(a)

# t.hideturtle()

# 색깔 바꾸면서 원
# t.home()
# t.shape()
# t.pensize(3)
# t.speed(1)
# t.bgcolor('black')

# colors = ['red','orange','yellow','green',
#           'blue', 'indigo', 'violet' ]
# for i in range(50,200,20):
#     t.penup()
#     t.goto(0,-i)
#     t.pendown()
#     t.color(colors[(i//20) % len(colors)])
#     t.circle(i)

# 무작위 원 그리기
t.home()
t.shape()
t.pensize(3)
t.speed(0)
t.bgcolor('black')

colors = ['red','orange','yellow','green',
          'blue', 'indigo', 'violet' ]

for i in range(0, 360, 15):
    t.penup()
    t.right(i)
    t.forward(50)
    t.goto(0,-i)
    t.pendown()
    t.color(colors[(i//20) % len(colors)])
    t.circle(50)

t.done()