import flet as ft   # Flet 라이브러리를 ft라는 이름으로 가져옴

# 프로그램이 시작될 때 실행되는 메인 함수
# def main(page: ft.Page):

#     page.title = "클릭 카운터"   # 프로그램 창 제목 설정
#     page.window_width = 300      # 창 가로 크기
#     page.window_height = 200     # 창 세로 크기
#     page.padding = 20            # 창 내부 여백

#     count = 0   # 클릭 횟수를 저장할 변수

#     # 화면에 표시할 텍스트 (현재 숫자를 보여줌)
#     text = ft.Text("0", size=40)

#     # "증가" 버튼을 눌렀을 때 실행되는 함수
#     def add_click(e):
#         nonlocal count      # 바깥 함수에 있는 count 변수를 사용하겠다는 의미
#         count += 1          # 숫자 1 증가
#         text.value = str(count)  # 화면에 표시할 값 변경
#         page.update()       # 화면을 다시 그려서 변경사항 반영

#     # "초기화" 버튼을 눌렀을 때 실행되는 함수
#     def reset_click(e):
#         nonlocal count
#         count = 0           # 숫자를 0으로 초기화
#         text.value = "0"
#         page.update()       # 화면 업데이트

#     # 화면에 UI 요소 추가
#     page.add(

#         text,   # 숫자를 보여주는 텍스트

#         # 버튼들을 가로로 배치하는 Row
#         ft.Row([

#             # 증가 버튼
#             ft.ElevatedButton(
#                 "증가",              # 버튼에 표시될 글자
#                 on_click=add_click   # 클릭 시 실행될 함수
#             ),

#             # 초기화 버튼
#             ft.ElevatedButton(
#                 "초기화",
#                 on_click=reset_click
#             )

#         ])
#     )

# # Flet 앱 실행
# ft.app(target=main)





#=======================================================



import flet as ft   # Flet 라이브러리 불러오기

# 프로그램 시작 함수
def main(page: ft.Page):

    page.title = "Calculator"  # 창 제목
    page.window.width = 300    # 창 가로 크기
    page.window.height = 400   # 창 세로 크기

    # 계산 결과를 표시할 텍스트
    result = ft.Text("0", size=40)

    # 버튼을 눌렀을 때 실행되는 함수
    def click(e):

        v = e.control.data   # 어떤 버튼이 눌렸는지 값 가져오기

        # C 버튼 (초기화)
        if v == "C":
            result.value = "0"

        # = 버튼 (계산 실행)
        elif v == "=":
            try:
                # 문자열 계산 실행
                result.value = str(eval(result.value))
            except:
                result.value = "Error"

        # 숫자나 연산자 버튼
        else:
            if result.value == "0":
                result.value = v
            else:
                result.value += v

        page.update()   # 화면 업데이트

    # 계산기 버튼을 만드는 함수
    def btn(t):

        return ft.ElevatedButton(
            t,            # 버튼에 표시될 문자
            data=t,       # 버튼 값 저장
            expand=True,  # 버튼을 가로로 꽉 채움
            on_click=click  # 클릭 이벤트 연결
        )

    # 화면 UI 구성
    page.add(

        # 결과 표시
        result,

        # 버튼들을 가로로 배치
        ft.Row([btn("7"), btn("8"), btn("9"), btn("/")]),
        ft.Row([btn("4"), btn("5"), btn("6"), btn("*")]),
        ft.Row([btn("1"), btn("2"), btn("3"), btn("-")]),
        ft.Row([btn("C"), btn("0"), btn("="), btn("+")]),
    )

# 프로그램 실행
ft.app(target=main)