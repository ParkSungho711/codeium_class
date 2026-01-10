# #num = 0

# while num < 30:
#     num = num + 1
#     print(num)

#     if num == 30:
#         break

# print(num)


# rr = ['문자',11,1.1,True]
# for i in rr:
#     # print(type(i))
#     # print(i , '의 타입은' , type(i) , '입니다.')
#     print(f'{i}  의 타입은  {type(i)}  입니다.')

# 1
# print(i , '의 타입은' , type(i) , '입니다.')
# 2
# print(f'{i}  의 타입은  {type(i)}  입니다.')

# 1초마다 출력 (sleep) 
# 카트라이더 자동차 속도가 10 입니다.
# 카트라이더 자동차 속도가 20 입니다.
# 100 입니다.

import time
cart = 10
while cart < 100:
    cart = cart + 10
    time.sleep(1)
    print(f'카트라이더의 속도는{cart}입니다')
    
    if cart == 100:
        break