# 오늘의 예제
# 신 년 운 세 뽑 기 ~
import random
import flet as ft

def main(page: ft.Page):
    year = [
        '음식 복이 있는 한해가 되겠네요~^^',
        '재물 운이 좋은 한해가 될 것 입니다~^^',
        '건강에 유의 해야하는 한 해가 될 것 입니다!',
        '친구와 더 깊은 우정을 쌓는 한해가 될 것 입니다!',
        '공부를 열심히 하면 좋은 성적을 얻을 한 해 입니다.',
        '진행하시는 사업이 잘 풀릴 것 입니다~',
        '사랑하는 사람과 사랑이 더 깊어질 것 입니다~!',
        '하는 일이 모두 잘 될 것 입니다~~~~!!^^'
    ]

    text = ft.Text("버튼을 눌러보세요")

    def show(e):
        text.value = random.choice(year)
        page.update()
    
    page.add(
        text,
        ft.ElevatedButton("명언 보기", on_click=show)
    )

ft.app(main)


#print(year)

# for i in year:
#     print(i)

# print(random.choice(year))

