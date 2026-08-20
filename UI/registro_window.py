import flet as ft
from flet.controls import colors, icon_data

def registro_window(page: ft.Page):

    page.title="Registro"
    page.bgcolor="#1A1625"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    titulo=ft.Text(
        "Uptime",
        align=ft.Alignment.CENTER,
        size=30,
        color="#EDEBF5"
    )

    subtitulo=ft.Text(
        "Empieza tu racha hoy",
        size=20,
        color="#A39FB5"
    )

    nombre=ft.TextField(
        label="Nombre",
        width=300,
        height=50,
        icon=ft.Icons.PERSON,
        border=ft.InputBorder.UNDERLINE,
        border_color="#EDEBF5",
        color="#A39FB5",
        label_style=ft.TextStyle(color="#A39FB5"),
    )

    correo=ft.TextField(
        label="Correo",
        width=300,
        height=50,
        icon=ft.Icons.MAIL,
        border=ft.InputBorder.UNDERLINE,
        border_color="#EDEBF5",
        color="#A39FB5",
        label_style=ft.TextStyle(color="#A39FB5"),
    )

    password=ft.TextField(
        label="Contraseña",
        width=300,
        height=50,
        can_reveal_password=True,
        password=True,
        icon=ft.Icons.LOCK,
        border=ft.InputBorder.UNDERLINE,
        border_color="#EDEBF5",
        color="#A39FB5",
        label_style=ft.TextStyle(color="#A39FB5")
    )

    password_confirmar=ft.TextField(
        label="Comfirmar contraseña",
        width=300,
        height=50,
        can_reveal_password=True,
        password=True,
        icon=ft.Icons.LOCK,
        border=ft.InputBorder.UNDERLINE,
        border_color="#EDEBF5",
        color="#A39FB5",
        label_style=ft.TextStyle(color="#A39FB5")
    )

    #<----FORMLUARIO---->
    formulario=ft.Container(
        width=600,
        height=800,
        bgcolor="#211C2E",
        border_radius=25,
        alignment=ft.Alignment.CENTER,
        content=ft.Column(
            controls=[

                ft.Icon(
                    icon=ft.Icons.INSIGHTS,
                    width=100,
                    height=100,
                    size=70
                ),

                titulo,
                
                subtitulo,

                nombre,

                correo,

                password,

                password_confirmar,

                ft.ElevatedButton(
                    "Crear cuenta",
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=10)
                    ),
                    bgcolor="#9D7BFF",
                    color="#EDEBF5",
                    icon=ft.Icons.PERSON_ADD_ALT,   
                    width=250
                ),

                ft.Container(
                    ft.Divider(),
                    width=400
                ),

                ft.ElevatedButton(
                    "Ya tengo una cuenta",
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=10)
                    ),
                    bgcolor="#9D7BFF",
                    color="#EDEBF5",
                    icon=ft.Icons.LOGIN,
                    width=250
                ),

                
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