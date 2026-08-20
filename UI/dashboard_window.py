import flet as ft

def dashboard_window(page: ft.Page):
    
    page.title = "App de habitos con alertas"

    sidebar=ft.Container(
        content=ft.Column(
            controls=[
                ft.Text(
                    "HABITOS",
                    size=16
                ),

                ft.ElevatedButton(
                    "Dashboard",
                    icon=ft.Icons.DASHBOARD,
                    color="#FFF",
                    bgcolor="#",
                ),

                ft.ElevatedButton(
                    "Habitos",
                    icon=ft.Icons.ROOM,
                    color="#FFF",
                    bgcolor="#"
                )
            ]
        ),
        width=200,
        height=800,
    )



    layout=ft.Container(
        content=ft.Column(
            controls=[
                sidebar
            ]
        )
    )

    page.add(layout)