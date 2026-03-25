import flet as ft
from home import home_view
from log import log_view

def handle_menu_item_click(e):
        print(f"{e.control.content.value}.on_click")

def dog_list(dog):
    return ft.MenuItemButton(
        width=200,
        content=ft.Text(dog, size=15),
        style=ft.ButtonStyle(
            bgcolor={
                ft.ControlState.HOVERED: ft.Colors.GREEN_100
            }
        ),
        on_click=handle_menu_item_click,
    )

# 메뉴바
dog_menubar = ft.Row(
        [
            ft.MenuBar(
                expand=True,
                style=ft.MenuStyle(
                    alignment=ft.Alignment.CENTER,
                    bgcolor=ft.Colors.YELLOW_600,
                    elevation=0,  # 그림자 제거
                    shadow_color=ft.Colors.TRANSPARENT,  # 그림자 완전 제거
                    mouse_cursor={
                        ft.ControlState.HOVERED: ft.MouseCursor.WAIT,
                        ft.ControlState.DEFAULT: ft.MouseCursor.ZOOM_OUT,
                    },
                ),
                controls=[
                    ft.SubmenuButton(
                        width=200,
                        content=ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=
                                    [
                                        ft.Text("츄츄(4년 9개월,♀)", size=18),
                                        ft.Icon(ft.Icons.KEYBOARD_ARROW_DOWN, size=25, color=ft.Colors.BLACK_54),
                                    ]
                                ),
                        controls=[
                            dog_list("츄츄(4년 9개월,♀)"),
                            dog_list("츄츄(4년 9개월,♀)"),
                            dog_list("츄츄(4년 9개월,♀)"),
                        ],
                    ),
                ],
            )
        ]
    )

def main(page: ft.Page):
    # 1. 가운데 내용물이 들어갈 '빈 거실(액자)'을 하나 미리 만들어 둡니다.
    # expand=True를 줘서 화면 중앙의 남는 공간을 모두 차지하게 합니다.
    body_container = ft.Container(expand=True)

    # 2. 하단 네비게이션 바 메뉴를 눌렀을 때 실행될 아주 간단한 함수입니다.
    def change_page(e):
        idx = e.control.selected_index
        
        # 3. 누른 번호에 따라 빈 거실(body_container)의 내용물(content)만 쏙 바꿔줍니다!
        if idx == 0:
            body_container.content = home_view(page)
        elif idx == 1:
            body_container.content = log_view(page)
        else:
            body_container.content = ft.Text("페이지 준비 중")
            
        # 4. "거실 가구 바꿨으니 화면 새로고침 해줘!"라고 Flet에게 알립니다.
        page.update()

    # 하단 네비게이션 바
    bottom_nav = ft.CupertinoNavigationBar(
        bgcolor=ft.Colors.YELLOW_600,
        selected_index=0, # 처음엔 무조건 홈(0번)
        on_change=change_page, # 메뉴를 누르면 알맹이를 바꾸는 함수 실행!
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Home"),
            ft.NavigationBarDestination(icon=ft.Icons.CALENDAR_MONTH, label="Log"),
            ft.NavigationBarDestination(icon=ft.Icons.FOOD_BANK_ROUNDED, label="Shop"),
            ft.NavigationBarDestination(icon=ft.Icons.MESSENGER_OUTLINE_ROUNDED, label="Contents"),
            ft.NavigationBarDestination(icon=ft.Icons.PERSON_OUTLINE, label="MyPage"),
        ],
    )

    # 앱 구동 시 가장 처음 보여줄 거실(홈 화면)을 세팅합니다.
    body_container.content = home_view(page)

    # 5. 도화지(page)에 상단바, 거실(body_container), 하단바를 순서대로 딱 한 번만 올려줍니다.
    # page.views를 클리어하고 append하는 복잡한 과정이 싹 사라졌습니다!
    page.add(
        dog_menubar, # 위에서 만든 상단바 
        body_container, # 내용물이 바뀔 마법의 거실
        bottom_nav # 고정된 하단바
    )

ft.app(target=main)