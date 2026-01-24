# 숫자 맞추기 게임
# 랜덤을 활용할거야
# range -> 범위
# for문을 쓸때는 list 안에있는걸
# 뽑아와서 한바퀴씩 돌리는건데
# 범위를 지정할수가 있다.
# 함수 뒤에는 항아리가 붙는다!
# for i in range(5):
#     print(i)

#                 -1 
# for i in range(1, 11, 2):
#     print(i)

# import random
# #               range
# answer = random.randint(1, 21)
# chance = 5
# print('===== 숫자 맞추기 게임 (1~20) ====')
# print(f'기회는 총 {chance}번 입니다.')
# #                    6   => 1, 6-1  => 1~5
# for i in range(1, chance+1):
#     guess = int(input(f'{i}번째 시도 - 숫자를 입력하세요~ : '))
#     if guess < answer:
#         print('정답이 더 높습니다! (UP)')
#     elif guess > answer:
#         print('정답이 더 낮습니다! (DOWN)')
#     else:
#         print(f'''축하합니다~ {i}번만에 맞췄습니다
#                 정답은 {answer} 였습니다~''')
#         break
# else:
#     print(f'''아쉽네요. 기회를 다 썼습니다.
#             정답은 {answer} 였습니다 ㅠㅠ!''')

# alias

# py -3.12 -m pip install flet

import flet as ft
import random

answer = random.randint(1, 20)
# 사용자 입력하는 창 만들기
input_num = ft.Textfield()
# 눈으로 보여주는 텍스트
msg = ft.Text()

def check(e):
    # input은 문자잖아?
    # 앞에 int를 붙여줬지?
    # 똑같다
    n = int(input_num.value)

    if n > answer:
        msg.value = '낮습니다!(DOWN)'
    elif n < answer:
        msg.value = '큽니다!(UP)'
    else:
        msg.value = '축하합니다~ 정답입니다~~!!><'
    # 변경된 메세지를 화면에 보여준다
    page.update()

page.add(
    input_num,
    ft.ElevatedButton('확인', on_click=check),
    msg
)
ft.app(main)