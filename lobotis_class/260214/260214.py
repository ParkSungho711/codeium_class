import flet as ft

def main(page: ft.Page):
    # 안내 문구
    todo = ft.TextField(label="하고 싶은 것을 추가해보세요! : ")

    # 입력한 항목을 세로로 쌓아서 보여주는 거
    list_view = ft.Column()

    # 추가 버튼을 누르면 내가 입력한게 쌓여야겟지?
    def add(e):
        list_view.controls.append(ft.Text(todo.value))
        # 변수값은 초기화
        todo.value = ""
        page.update()
    
    page.add(
        todo,
        ft.ElevatedButton("추가하기", on_click=add),
        list_view
    )

ft.app(main)
    
