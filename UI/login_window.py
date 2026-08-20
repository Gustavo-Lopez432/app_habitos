import flet as ft
from flet.controls import colors, icon_data

def login_window(page: ft.Page):

    page.title="Inicia sesiòn"
    page.bgcolor="#1A1625"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    titulo=ft.Text(
        "Iniciar sesiòn",
        align=ft.Alignment.CENTER,
        size=30,
        color="#EDEBF5"
    )

    subtitulo=ft.Text(
        "Construye tus habitos",
        size=20,
        color="#A39FB5"
    )

    correo=ft.TextField(
        label="Correo",
        width=250,
        height=50,
        icon=ft.Icons.MAIL,
        border=ft.InputBorder.UNDERLINE,
        border_color="#000",
        color="#000",
        label_style=ft.TextStyle(color="#A39FB5"),
    )

    password=ft.TextField(
        label="Contraseña",
        width=250,
        height=50,
        can_reveal_password=True,
        password=True,
        icon=ft.Icons.LOCK,
        border=ft.InputBorder.UNDERLINE,
        border_color="#000",
        color="#A39FB5",
        label_style=ft.TextStyle(color="#A39FB5")
    )

    #<----FORMLUARIO---->
    formulario=ft.Container(
        width=450,
        height=600,
        bgcolor="#211C2E",
        border_radius=10,
        alignment=ft.Alignment.CENTER,
        content=ft.Column(
            controls=[

                ft.Icon(
                    icon=ft.Icons.BOOK,
                    width=100,
                    height=100
                ),

                titulo,
                
                subtitulo,

                correo,

                password,

                ft.ElevatedButton(
                    "Iniciar Sesiòn",
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=10)
                    ),
                    bgcolor="#9D7BFF",
                    color="#EDEBF5",
                    icon=ft.Icons.LOGIN
                ),

                ft.Container(
                    ft.Divider(),
                    width=300
                ),

                ft.ElevatedButton(
                    "Crear cuenta",
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=10)
                    ),
                    bgcolor="#9D7BFF",
                    color="#EDEBF5",
                    icon=ft.Icons.PERSON_ADD_ALT,
                    
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15
        ),
    )

    layout=ft.Container(
        content=ft.Column(
            controls=[
                formulario,
            ]
        )
    )

    page.add(layout)