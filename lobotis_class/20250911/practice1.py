import turtle as t
import random

# 기본 설정
t.title("거북이 먹이 게임")
t.shape("turtle")
t.speed(0)

# 먹이 설정
food = t.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(random.randint(-200, 200), random.randint(-200, 200))

# 메시지 출력용
message = t.Turtle()
message.hideturtle()
message.penup()
message.goto(0, 200)

# 움직임 함수
def turn_right():
    t.setheading(0)
    t.forward(20)
    check_eat()

def turn_up():
    t.setheading(90)
    t.forward(20)
    check_eat()

def turn_left():
    t.setheading(180)
    t.forward(20)
    check_eat()

def turn_down():
    t.setheading(270)
    t.forward(20)
    check_eat()

# 먹이 먹었는지 확인
def check_eat():
    if t.distance(food) < 20:
        message.clear()
        message.write("야호! 🐢", align="center", font=("Arial", 16, "bold"))
        food.goto(random.randint(-200, 200), random.randint(-200, 200))

# 키보드 이벤트
t.listen()
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")

t.mainloop()