import flet as ft

def main(page: ft.Page):
    #페이지 기본설정
    page.title = "똑똑"
    page.scroll = ft.ScrollMode.AUTO 
    #메인컬러 설정
    Main_color = "#FFDD30"

    #상단 헤더
    header = ft.Row(
        controls=[
            ft.Text("츄츄(4년 9개월, ♀)", size=22, weight="bold", color=Main_color),
        ],
        alignment=ft.MainAxisAlignment.CENTER,)

    #페이지 레이아웃 배치
    page.add(
        header)


#페이지 실행
if __name__ == "__main__":
    import webbrowser, os
    if os.getenv("FLET_NO_BROWSER"):
        webbrowser.open = lambda *args, **kwargs: None
    ft.run(
        main,
        assets_dir="assets",
        view=ft.AppView.WEB_BROWSER,
        port=34636,
    )