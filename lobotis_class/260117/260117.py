# click = 0
# click2 = '클릭'

# while True:
#     write = input('단어를 입력하세요 : ')
#     if write == click2:
#         click +=  1
#         print(click)

import flet as ft

def main(page: ft.Page):
    count = 0
    txt = ft.Text(f'현재 값 : {count}', size=20)
    def plus(e):
        nonlocal count
        count += 1
        txt.value = f'현재 값 : {count}'
        page.update()
    
    def minus(e):
        nonlocal count
        count -= 1
        txt.value = f'현재 값 : {count}'
        page.update()
    
    page.add(
        txt,
        ft.ElevatedButton('➕ 증가',on_click=plus),
        ft.ElevatedButton('➕ 감소',on_click=minus)
    )


    

ft.app(main)




# ➖