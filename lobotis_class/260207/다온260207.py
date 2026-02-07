# name = "Alice"
# age = 25
# height = 165.5
# print(f"""{name}은(는) {age}세 이며,
#       키는 {height:.1f}cm입니다""")

# def calc(a,b):
#     return a * 2 + b


# x = calc(2,3)
# # 7

# y = calc(1,4)
# #6
# print(x + y)
# 13


# start = 1.25
# elapsed = 2.80
# end = start + elapsed
# print(round(end - start))
#다 더하고 뺀 값을 내림하여 소수가아닌 값으로 만든다

# num = "123.456"
# x = len(num.split(".")[0])
# y = round(float(num),2)
# print(x + y)


# def my_func(x,y):
#     return x + y , x - y
# result = my_func(5,3)
# print(type(result))

# a = [1,2,3]
# a.append(4)
# print(a)

# t1 = (0,1,2,3,4)
# t2 = sorted(t1[1:])
# result = len(t2)
# print(result,t2)

# d = {'apple': 1, 'banana': 2}
# d['apple'] = 3
# print(d['apple'] + d['banana'])

# result = 0
# for i in range(1,10):
#     if i % 3 == 0 :
#         result += 1
#         print(result)

# x = 2
# y = 3
# z = 5
# print(x**y + z %(y + 1)* 2)

# result = []
# for i in range(5):
#     if i % 2 == 0:
#         result.append(i)
#     else:
#         for j in range(2):
#             result.append(i)
#             print(result)

# 일_리 = 0.4
# 천_리 = 400.0
# print("천리의 길이는 ", 천_리,"km이다.")

# kait = ['한국','정보','통신','진흥','협회']
# for i in kait:
#     print(i)

# def 사각형_넓이(가로,세로):
#     return 가로 * 세로

# 가로 = 10
# 세로 = 5

# 넓이 = 사각형_넓이(가로,세로)
# print("사각형의 넓이:",넓이)

import turtle
t = turtle.Turtle()
t.shape('turtle')

t.left(60)
t.forward(100)
