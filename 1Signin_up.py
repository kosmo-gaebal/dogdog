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

    # ⬜ 아이콘이 있으면 왼쪽에 추가
    if icon:
        controls.append(ft.Icon(icon, size=18, color=text_color))

    # ⬜ 텍스트를 중앙 정렬용 Row에 넣기 위해 추가
    controls.append(
        ft.Text(
            text,
            size=14,
            weight=ft.FontWeight.W_500,
            color=text_color,
        )
    )

    return ft.Container(
        width=350,  # ☑️ 버튼 가로 크기를 고정해서 모든 박스 너비를 같게 맞춤
        height=50,  # ☑️ 버튼 세로 크기를 고정해서 높이를 일정하게 맞춤
        bgcolor=bgcolor,
        border=ft.Border.all(1, border_color),
        border_radius=10,
        padding=10,  # ☑️ 내부 여백을 줘서 텍스트/아이콘이 테두리에 붙지 않게 함
        alignment=ft.Alignment(0, 0),  # ☑️ Container 내부 content의 기준 위치를 정중앙으로 잡음
        on_click=on_click,

        # ✅ [UI 구성] 버튼 내부 레이아웃 (아이콘 + 텍스트 정렬)
        content=ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,  # ☑️ Row 안 요소들을 가로축 기준 가운데로 모음
            vertical_alignment=ft.CrossAxisAlignment.CENTER,  # ☑️ Row 안 요소들을 세로축 기준 가운데 정렬
            spacing=8,  # ☑️ 아이콘과 텍스트 사이 간격
            controls=controls,
        ),
    )

def main(page: ft.Page):
    page.bgcolor = ft.Colors.WHITE

    # ✅ [전체 레이아웃] 화면 전체를 중앙 정렬
    page.vertical_alignment = ft.MainAxisAlignment.CENTER  # ☑️ page에 들어가는 전체 내용을 세로 기준 가운데 배치
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER  # ☑️ page에 들어가는 전체 내용을 가로 기준 가운데 배치

    page.title = "Sign In / Sign Up"

    # ✅ [UI 구성] 화면 상단 제목 텍스트
    title_text = ft.Text(
        "Sign In / Sign Up",
        size=22,
        weight=ft.FontWeight.W_600,
        color=ft.Colors.BLACK,
    )

    # ✅ [UI 구성] 로그인 버튼 묶음 (Google / Apple / Kakao)
    continue_cards = ft.Column(
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # ☑️ Column 안의 버튼들을 가로로 가운데 정렬
        alignment=ft.MainAxisAlignment.CENTER,  # ☑️ Column 안의 버튼 묶음을 세로 기준 가운데 정렬
        spacing=16,  # ☑️ 버튼과 버튼 사이의 세로 간격
        controls=[
            long_box("Continue with Google"),
            long_box("Continue with Apple"),
            long_box("Continue with Kakao"),
        ],
    )

    # ✅ [UI 구성] 구분선 (or + 양쪽 라인)
    stop_line = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,  # ☑️ Row 전체를 가로 가운데 기준으로 정렬
        width=350,  # ☑️ 버튼 너비와 맞춰서 구분선 전체 폭을 동일하게 맞춤
        controls=[
            ft.Container(
                expand=True,  # ☑️ 왼쪽 선이 남는 공간만큼 자동으로 늘어나게 함
                height=1,
                bgcolor=ft.Colors.GREY_400,
            ),
            ft.Text("or", size=12),
            ft.Container(
                expand=True,  # ☑️ 오른쪽 선도 남는 공간만큼 자동 확장해서 좌우 균형 맞춤
                height=1,
                bgcolor=ft.Colors.GREY_400,
            ),
        ],
    )

    # ✅ [UI 구성] 전체 콘텐츠 영역 (제목 + 버튼 + 구분선)
    body = ft.Container(
        padding=ft.padding.only(top=-250),  # ☑️ body 전체를 위쪽으로 끌어올려서 화면 중앙보다 조금 위에 배치
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # ☑️ body 안 요소들을 가로 가운데 정렬
            spacing=20,  # ☑️ 제목, 버튼묶음, 구분선, 이메일 버튼 사이 세로 간격
            controls=[
                title_text,
                continue_cards,
                stop_line,
                long_box("Continue with Email"),
            ],
        ),
    )

    # ✅ [렌더링] 페이지에 최종 UI 추가
    page.add(body)  # ☑️ 정리한 body 전체를 page에 올려서 실제 화면에 배치

if __name__ == "__main__":
    import webbrowser
    import os

    if os.getenv("FLET_NO_BROWSER"):
        webbrowser.open = lambda *args, **kwargs: None

    ft.app(
        main,
        assets_dir="assets",

        # ✅ [실행 설정] 웹 브라우저에서 실행
        view=ft.AppView.WEB_BROWSER,
        port=34636,
    )