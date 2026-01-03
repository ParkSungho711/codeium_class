import flet as ft
import random

# 앱이 시작될 때 제일 먼저 실행되는 함수
def main(page: ft.Page):

    # 새해 인사를 list에 저장하기
    happy_new_year = [
        '26년에는 행복한 일만 가득하세요.',
        '26년에는 건강한 한해 보내세요',
        '26년에는 소망하는 일 모두 이루어지세요',
        '26년에는 좋은 성적을 기대할게요',
        '26년에는 친구들과 사이좋게 지낼거에요',
        '26년에는 코딩 공부를 더 잘하게 될 거에요',
        '26년에는 자격증 취득이 가능할 거에요'
    ]
    # flet 별명이 ft
    # ft의 Text라는 아이템을 사용하기위해서
    # . 을썼지
    text = ft.Text("버튼을 눌러보세요")

    # 맨 위에서 import 로 랜덤 사용한다 했지
    # happy_new_year 안에 있는 걸 랜덤으로 출력
    def show(e):
        text.value = random.choice(happy_new_year)
        page.update()

    page.add(
        text,
        ft.ElevatedButton("새해인사 보기", 
                          on_click=show)
    )



# for i in happy_new_year:
#     print(i)