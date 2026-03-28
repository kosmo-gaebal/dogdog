import flet as ft

def arrow_back(on_click=None):
      return ft.Container(
        width=float("inf"),  # 👉 전체 너비 차지
        alignment=ft.Alignment(-1, 0),  # 👉 왼쪽 정렬  # 👈 왼쪽 이동
        on_click=on_click,
        content=ft.Icon(ft.Icons.ARROW_BACK),
        )

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
        hint_text = hint_text,
        label=label,  # 선택적으로 라벨도 넣을 수 있음
    )

def bottom_continue_button(on_click=None):
    return ft.Container(
        alignment=ft.Alignment(0, 1),
        padding=ft.padding.only(bottom=20),
        content=long_box(
            "Continue",
            bgcolor=ft.Colors.YELLOW,
            text_color=ft.Colors.BLACK,
            on_click=on_click,
        ),
    )

def main(page: ft.Page):
    page.bgcolor = ft.Colors.WHITE
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO
    page.title = "Pet info food"

    harim_bottom_tip_sheet = ft.BottomSheet(
        # ✅ 1. 배경 어둡게 → 시선 집중 (핵심)
        # 살짝 어둡게 바꿔야 "떠있는 느낌" 남
        # barrier_color=ft.Colors.with_opacity(0.4, ft.Colors.BLACK), 
        # ✅ 2. 배경 밝게 → FIGMA 디자인 기준
        barrier_color=ft.Colors.TRANSPARENT,

        size_constraints=ft.BoxConstraints(
            max_height=700,
            min_height=430,
        ),

        content=ft.Container(
            padding=20,
            bgcolor=ft.Colors.WHITE,

            # ✅ 2. 둥근 상단 → 바텀시트 느낌 강화
            border_radius=ft.border_radius.only(
                top_left=20,
                top_right=20,
            ),

            # ✅ 3. 그림자 효과 → 떠있는 느낌
            shadow=ft.BoxShadow(
                spread_radius=2,
                blur_radius=20,
                color=ft.Colors.with_opacity(0.2, ft.Colors.BLACK),
                offset=ft.Offset(0, -4),  # 위쪽 그림자
            ),

            content=ft.Column(
                tight=True,
                controls=[
                    
                    # ✅ 4. 드래그 핸들 (요즘 앱 필수 요소)
                    ft.Container(
                        width=40,
                        height=5,
                        border_radius=10,
                        bgcolor=ft.Colors.GREY_400,
                        alignment=ft.Alignment(0, 0),  # ✅ 가운데 정렬,
                    ),

                    ft.Container(height=10),  # 여백

                    ft.Text("사료 검색", size=25, weight='bold'),

                    input_box("Search"),

                    ft.Text("하림 가맛시"),
                    ft.Text("하림 가맛시"),
                    ft.Text("하림 가맛시"),
                    ft.Text("하림 가맛시"),
                    ft.Text("하림 가맛시"),

                    ft.Container(height=10),
                ],
            ),
        )
    )

    # 앱이 시작될때 bottomSheet을 띄우기
    def show_inital_tip(e=None):
      harim_bottom_tip_sheet.open = True
      page.update()



    body = ft.Container(
                      padding=ft.padding.only(top=0), # 🔥 (1) 전체 레이아웃을 아래로 내림 음수 제거
                      content=ft.Column(
                          width=350, # 🔥 (2) Column 자체의 너비를 고정
                          spacing=12, 
                          horizontal_alignment=ft.CrossAxisAlignment.START, # center를 start로 바꿈
                          scroll=ft.ScrollMode.AUTO,
                          controls=[
                              arrow_back(),
                              ft.Container(
                                  margin=ft.margin.only(top=50),
                                  content=about_dog(),
                              ),
                              ft.Text("현재 급여 중인 사료", weight=ft.FontWeight.W_500, color=ft.Colors.BLACK),
                              input_box("현재 급여 중인 사료를 적어주세요"),

                              ft.Text("현재 급여 중인 사료 잔여량", weight=ft.FontWeight.W_500, color=ft.Colors.BLACK),
                              input_box("현재 급여 중인 사료 잔여량을 적어주세요"),

                              bottom_continue_button(),
                          ],
                        ),
                      )
                  
              
  ### 페이지에 BottomSheet를 등록하기
    page.overlay.append(harim_bottom_tip_sheet)
    show_inital_tip()
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