import flet as ft   # Flet 라이브러리 불러오기

# 프로그램 시작 함수
def main(page: ft.Page):

    page.title = "Calculator"  # 창 제목
    page.window.width = 300    # 창 가로 크기
    page.window.height = 400   # 창 세로 크기

    # 계산 결과를 표시할 텍스트
    result = ft.Text("0", size=40)

    def click(e):
        v = e.control.data

        if v == "C":
            result.value = "0"
        elif v == "=":
            try:
                result.value = str(eval(result.value))
            except:
                result.value = "Error"
        else:
            if result.value == "0":
                result.value = v
            else:
                result.value += v
            
        page.update()

    def btn(t):
        return ft.ElevatedButton(
            t,            # 버튼에 표시될 문자
            data=t,       # 버튼 값 저장
            expand=True,  # 버튼을 가로로 꽉 채움
            on_click=click  # 클릭 이벤트 연결
        )

    page.add(
        result,
        ft.Row([btn("7"), btn("8"), btn("9"), btn("/")]),
        ft.Row([btn("4"), btn("5"), btn("6"), btn("*")]),
        ft.Row([btn("1"), btn("2"), btn("3"), btn("-")]),
        ft.Row([btn("C"), btn("0"), btn("="), btn("+")]),
    )

ft.app(target=main) 















# def main(page: ft.Page):
#     page.title = "클릭 카운터"
#     page.window_width = 300
#     page.window_heignt = 200
#     page.padding = 20

#     count = 0

#     text = ft.Text("0", size=40)

#     def add_click(e):
#         nonlocal count
#         count += 1
#         text.value = str(count)
#         page.update()

#     def minus_click(e):
#         nonlocal count
#         count -= 1
#         text.value = str(count)
#         page.update()

#     def reset_click(e):
#         nonlocal count
#         count = 0           # 숫자를 0으로 초기화
#         text.value = "0"
#         page.update()


#     page.add(
#         text,
        
#         ft.Row([

#             ft.ElevatedButton(
#                 "증가",
#                 on_click=add_click
#             ),

#             ft.ElevatedButton(
#                 "감소",
#                 on_click=minus_click
#             )

#         ])
#     )

# ft.app(target=main)