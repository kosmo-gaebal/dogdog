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


def input_box(label=None, hint_text=None):
    return ft.TextField(
        width=350,
        height=50,
        border_radius=10,
        border_color=ft.Colors.GREY_300,
        focused_border_color=ft.Colors.GREY_400,
        hint_text=hint_text,
        label=label,
    )


# ✅ 유지: 버튼 함수는 모양만 담당
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


# ✅ 유지: 기존 체크박스 함수 보존
def invisible_checkbox_row(left_text="있다", right_text="없다"):
    return ft.Container(
        width=350,
        height=50,
        padding=10,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
            controls=[
                ft.Row(
                    spacing=5,
                    controls=[
                        ft.Checkbox(),
                        ft.Text(left_text, weight=ft.FontWeight.W_500),
                    ],
                ),
                ft.Row(
                    spacing=5,
                    controls=[
                        ft.Checkbox(),
                        ft.Text(right_text, weight=ft.FontWeight.W_500),
                    ],
                ),
            ],
        ),
    )


def main(page: ft.Page):
    page.bgcolor = ft.Colors.WHITE
    page.padding = 0                  # ✅ 추가
    page.spacing = 0                  # ✅ 추가
    page.vertical_alignment = ft.MainAxisAlignment.START   # ✅ 수정
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.HIDDEN
    page.title = "For Dog4"

    allergy_value = None
    disease_value = None

    def on_allergy_change(e):
        nonlocal allergy_value
        allergy_value = e.control.value
        page.update()

    def on_disease_change(e):
        nonlocal disease_value
        disease_value = e.control.value
        page.update()

    body_content = ft.Column(
        width=350,
        spacing=12,
        horizontal_alignment=ft.CrossAxisAlignment.START,
        scroll=ft.ScrollMode.AUTO,
        controls=[
            ft.Container(
                margin=ft.margin.only(top=50),
                content=about_dog(),
            ),
            ft.Text("알레르기", weight=ft.FontWeight.W_500),

            # ✅ 기존 체크박스 (보존)
            # invisible_checkbox_row("있다", "없다"),

            # ✅ 신규: 라디오 방식
            ft.Container(
                width=350,
                padding=12,
                content=ft.RadioGroup(
                    value=allergy_value,
                    on_change=on_allergy_change,
                    content=ft.Row(
                        spacing=20,
                        controls=[
                            ft.Radio(value="yes", label="있다"),
                            ft.Radio(value="no", label="없다"),
                        ],
                    ),
                ),
            ),

            input_box("반려동물의 알레르기를 적어주세요"),

            ft.Text("질병", weight=ft.FontWeight.W_500),

            # ✅ 기존 체크박스 (보존)
            # invisible_checkbox_row("있다", "없다"),

            # ✅ 신규: 라디오 방식
            ft.Container(
                width=350,
                padding=12,
                content=ft.RadioGroup(
                    value=disease_value,
                    on_change=on_disease_change,
                    content=ft.Row(
                        spacing=20,
                        controls=[
                            ft.Radio(value="yes", label="있다"),
                            ft.Radio(value="no", label="없다"),
                        ],
                    ),
                ),
            ),

            input_box("반려동물의 질병을 적어주세요"),
            ft.Container(height=20),
        ],
    )

    # ✅ 수정: 패딩 없이 자연스럽게 하단 고정
    fixed_button = ft.Container(
        width=float("inf"),
        alignment=ft.Alignment(0, 1),
        content=ft.Container(
            width=350,
            alignment=ft.Alignment(0, 0),
            content=bottom_continue_button(),
        ),
    )

    body = ft.Container(
        expand=True,
        content=ft.Column(
            expand=True,
            spacing=0,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    expand=True,
                    content=body_content,
                ),
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