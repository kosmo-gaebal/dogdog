import flet as ft

def about_dog():
    return ft.Column(
        spacing=0,
        controls=[
            ft.Text("About your Dog", weight=ft.FontWeight.W_500, color=ft.Colors.BLACK, size=30),
            ft.Text("반려동물의 기본 정보를 입력하세요", weight=ft.FontWeight.W_500, color=ft.Colors.BLACK, size=15),
        ],
    )


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


# 🟩 수정: 1번 파일 기준 패턴에 맞춰 버튼 함수는 단순하게 유지
# 🟩 이유: 아래 여백과 위치는 바깥 fixed_button에서 통일 관리
def bottom_continue_button(on_click=None):
    return ft.Container(
        alignment=ft.Alignment(0, 0),
        content=long_box(
            "Continue",
            bgcolor=ft.Colors.YELLOW,
            text_color=ft.Colors.BLACK,
            on_click=on_click,
        ),
    )


def invisible_checkbox(text):
    return ft.Container(
        width=350,
        height=50,
        border=None,
        border_radius=10,
        padding=10,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Checkbox(),
                ft.Text(text, weight=ft.FontWeight.W_500, color=ft.Colors.BLACK),
            ],
        ),
    )


# 🟦 추가: 산책 시간은 여러 개를 동시에 고르는 체크박스가 아니라
# 🟦 3자택일(하나만 선택)이어야 하므로 라디오 버튼 전용 행을 따로 만듦
# 🟦 기능 구현 위치:
# - 실제 "하나만 선택" 동작은 아래 radio_time_group() 안의 ft.RadioGroup 에서 처리됨
# - 이 함수는 화면에 보이는 라디오 1줄 모양만 만들어주는 역할
def invisible_radio(text, value):
    return ft.Container(
        width=350,
        height=50,
        border=None,
        border_radius=10,
        padding=10,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Radio(value=value),
                ft.Text(text, weight=ft.FontWeight.W_500, color=ft.Colors.BLACK),
            ],
        ),
    )


# 🟦 추가: 산책 시간 3개 항목을 하나의 그룹으로 묶는 함수
# 🟦 이유:
# - Radio 버튼은 같은 RadioGroup 안에 있어야 3자택일이 됨
# - 즉, 3개 중 하나를 누르면 나머지는 자동으로 해제됨
# 🟦 기능 구현 위치:
# - ft.RadioGroup 이 "단일 선택" 기능의 핵심
# - Column 안에 invisible_radio() 3개를 넣어서 기존 세로 배치 흐름 유지
def radio_time_group():
    return ft.RadioGroup(
        content=ft.Column(
            spacing=0,
            controls=[
                invisible_radio("하루 30분", "30min"),
                invisible_radio("하루 30분 이상", "30min_plus"),
                invisible_radio("하루 1시간 이상", "1hour_plus"),
            ],
        ),
    )


def main(page: ft.Page):
    page.bgcolor = ft.Colors.WHITE
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # 🟧 수정: 페이지 전체 스크롤을 끄고 본문만 스크롤되게 변경
    # 🟧 기능: Continue 버튼이 본문과 같이 움직이지 않고 하단에 고정되도록 하기 위함
    page.scroll = ft.ScrollMode.HIDDEN

    page.title = "For Dog3"

    # 🟧 추가: 스크롤되는 본문 영역을 따로 분리
    # 🟧 기능: 체크박스/텍스트 영역만 스크롤되고, 아래 Continue 버튼은 고정됨
    body_content = ft.Column(
        width=350,  # 🔥 (2) Column 자체의 너비를 고정
        spacing=12,
        horizontal_alignment=ft.CrossAxisAlignment.START,  # center를 start로 바꿈
        scroll=ft.ScrollMode.AUTO,
        controls=[
            ft.Container(
                margin=ft.margin.only(top=50),
                content=about_dog(),
            ),
            ft.Text("급여 시간", weight=ft.FontWeight.W_500, color=ft.Colors.BLACK),
            invisible_checkbox("아침"),
            invisible_checkbox("점심"),
            invisible_checkbox("저녁"),

            ft.Text("산책 시간", weight=ft.FontWeight.W_500, color=ft.Colors.BLACK),

            # 🟦 수정: 산책 시간은 기존 체크박스 3개 대신 3자택일 라디오 그룹으로 변경
            # 🟦 기능:
            # - radio_time_group() 안의 RadioGroup이 3개 항목을 하나의 선택 묶음으로 관리
            # - 그래서 사용자는 산책 시간 3개 중 하나만 선택 가능
            radio_time_group(),

            # 🟧 추가: 마지막 체크박스가 고정 버튼에 가려지지 않도록 아래 여백 확보
            # 🟧 기능: 스크롤을 끝까지 내렸을 때 마지막 항목이 버튼 뒤에 숨지 않게 함
            ft.Container(height=20),
        ],
    )

    # 🟧 추가: 하단 고정 Continue 버튼 영역
    # 🟧 기능: 본문 스크롤과 분리해서 화면 아래쪽에 Continue 버튼을 고정
    fixed_button = ft.Container(
        width=float("inf"),
        alignment=ft.Alignment(0, 0),
        padding=ft.padding.only(top=10, bottom=20),
        content=ft.Container(
            width=350,
            alignment=ft.Alignment(0, 0),
            content=bottom_continue_button(),
        ),
    )

    body = ft.Container(
        padding=ft.padding.only(top=0),  # 🔥 (1) 전체 레이아웃을 아래로 내림 음수 제거
        expand=True,
        content=ft.Column(
            expand=True,
            spacing=0,

            # 🟧 추가: 전체 레이아웃의 가로 중앙 기준을 맞춤
            # 🟧 기능: 위 본문 영역과 아래 고정 버튼 영역이 같은 중심선 위에 놓이도록 함
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,

            controls=[
                # 🟧 추가: 위쪽은 스크롤되는 본문 영역
                ft.Container(
                    expand=True,
                    content=body_content,
                ),

                # 🟧 추가: 아래쪽은 고정 버튼 영역
                fixed_button,
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