import flet as ft

def long_box(
    text,
    bgcolor=ft.Colors.WHITE,
    text_color=ft.Colors.BLACK,
    border_color=ft.Colors.GREY_300,
    on_click=None,
    icon=None,
):
    controls = []

    if icon:
        controls.append(ft.Icon(icon, size=18, color=text_color))

    controls.append(
        ft.Text(
            text,
            size=14,
            weight=ft.FontWeight.W_500,
            color=text_color,
        )
    )

    return ft.Container(
        width=350,
        height=50,
        bgcolor=bgcolor,
        border=ft.Border.all(1, border_color),
        border_radius=10,
        padding=10,
        alignment=ft.Alignment(0, 0),
        on_click=on_click,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=8,
            controls=controls,
        ),
    )

def input_box(label=None, hint_text=None):
    return ft.TextField(
        width=350,
        height=50,
        border_radius=10,
        border_color=ft.Colors.GREY_300,
        focused_border_color=ft.Colors.GREY_400,
        hint_text=hint_text,
        label=label,  # 선택적으로 라벨도 넣을 수 있음
    )

def main(page: ft.Page):
    page.bgcolor = ft.Colors.WHITE
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.title = "Sign In / Sign Up"

    # ✅ 추가: 이메일 로그인 영역이 보일지 여부를 저장하는 상태 변수
    # ✅ 기능: "Continue with Email" 박스를 누르면 False → True로 바뀌고 입력창이 나타남
    email_mode = False

    title_text = ft.Text(
        "Sign In / Sign Up",
        size=22,
        weight=ft.FontWeight.W_600,
        color=ft.Colors.BLACK,
    )

    # ✅ 추가: 이메일 박스를 눌렀을 때 실행될 함수
    # ✅ 기능: 숨겨져 있던 이메일 입력 영역을 보이게 하고 화면을 다시 그림
    def show_email_section(e):
        nonlocal email_mode
        email_mode = True
        email_section.visible = email_mode
        page.update()

    continue_cards = ft.Column(
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=16,
        controls=[
            # 🔥 [수정] 기존 Container 3개 → 함수로 변경
            long_box("Continue with Google"),
            long_box("Continue with Apple"),
            long_box("Continue with Kakao"),
        ],
    )

    stop_line = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        width=350,
        controls=[
            ft.Container(
                expand=True,
                height=1,
                bgcolor=ft.Colors.GREY_400,
            ),
            ft.Text("or", size=12),
            ft.Container(
                expand=True,
                height=1,
                bgcolor=ft.Colors.GREY_400,
            ),
        ],
    )

    # ✅ 추가: 이메일 입력 관련 UI를 하나의 컬럼으로 묶음
    # ✅ 기능: visible 속성으로 전체 영역을 한 번에 숨기거나 보여줄 수 있음
    email_section = ft.Column(
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20,
        visible=email_mode,
        controls=[
            ft.Container(
                width=350,
                alignment=ft.Alignment(-1, 0),
                content=ft.Text(
                    "이메일",
                    weight=ft.FontWeight.W_500,
                    color=ft.Colors.BLACK,
                ),
            ),
            input_box(hint_text="이메일 주소를 입력하세요"),
            long_box("Continue", bgcolor=ft.Colors.YELLOW),
        ],
    )

    body = ft.Container(
        padding=ft.padding.only(top=0),  # 🔥 (기존 ft.Padding → ft.padding으로 수정 권장)
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
            controls=[
                title_text,
                continue_cards,
                stop_line,

                # ✅ 수정: 이메일 박스를 누르면 아래 email_section이 나타나도록 on_click 연결
                # ✅ 기능: 라디오 버튼 패턴처럼 클릭 시 숨김 영역이 펼쳐짐
                long_box("Continue with Email", on_click=show_email_section),

                # ✅ 추가: 처음에는 숨겨져 있다가 이메일 박스 클릭 시 나타나는 영역
                # ✅ 기능: 이메일 텍스트 / 입력창 / Continue 버튼을 함께 표시
                email_section,
            ],
        ),
    )

    page.add(body)


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