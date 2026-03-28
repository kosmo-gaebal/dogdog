import flet as ft


def main(page: ft.Page):
    page.title = "Splash"
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER
    # page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    page.add(
        ft.Container(
            expand=True, # ☑️ 이게 없으면 그라데이션이 가로만 적용됨 
            width=float("inf"), # ☑️ 이게 없으면 그라데이션이 세로만 적용됨
            gradient=ft.LinearGradient( 
                begin=ft.Alignment(0, 1),   # ☑️ 아래
                end=ft.Alignment(0, -1),    # ☑️ 위
                colors=[
                    ft.Colors.YELLOW,
                    ft.Colors.YELLOW_100,
                    ft.Colors.WHITE,
                ],
            ),
            content=ft.Column(
                expand = True,
                alignment=ft.MainAxisAlignment.CENTER, # ☑️ 이게 없으면 로고가 천장에 붙음
                horizontal_alignment=ft.CrossAxisAlignment.CENTER, # ☑️ 이게 없으면 로고가 왼쪽에 붙음
                controls=[
                    ft.Image(
                        src="ddoglogo.png",
                        width=150,
                        height=150,
                    ),
                ],
            ),
        )
    )

ft.run(main)

if __name__ == "__main__":
    import webbrowser
    import os

    if os.getenv("FLET_NO_BROWSER"):
        webbrowser.open = lambda *args, **kwargs: None

    ft.app(
        main,
        assets_dir="assets",
        view=ft.AppView.WEB_BROWSER,
        port=34636,
    )