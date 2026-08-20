
#<----VENTANA DEL DASHBOARD---->

#<----IMPORTS NECESARIOS PARA QUE LA VENTANA FUNCIONE---->
import flet as ft
from core.theme import Colores

#<----DEFINE LA FUNCION PRINCIPAL DEL DASHBOARD---->
def dashboard_window(page: ft.Page):
    
    page.title = "Dashboard"
    page.bgcolor=Colores.color_fondo
    page.padding=0

    titulo=ft.Text(
        "UPTIME",
        size=16,
        color=Colores.titulos,
    )   

    boton_dashboard=ft.ElevatedButton(
        "Dashboard",
        icon=ft.Icons.DASHBOARD,
        bgcolor=Colores.color_fondo_botones,
        color=Colores.textos,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10)
        ),
    )

    boton_mis_habitos=ft.ElevatedButton(
        "Mis habitos",
        icon=ft.Icons.HOUSE
    )

    #<----SIDEBAR---->
    sidebar=ft.Container(

        #<----CONFIGURACION DEL SIDEBAR---->
        width=250,
        height=800,
        bgcolor=Colores.color_fondo_targetas,

        #<----ORDEN DEL SIDEBAR---->
        content=ft.Column(
            controls=[

                #<----TITULO---->
                titulo,

                #<----BOTON DEL DASHBOARD---->
                boton_dashboard,

                boton_mis_habitos,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15
        )
    )

    #<----LATOUT PRINCIPAL DE LA VENTAN---->
    layout=ft.Container(
        content=ft.Column(
            controls=[
                sidebar
            ]
        )
    )

    #<----AÑADE EL LAYOUT A LA PAGINA PRINCIPAL---->
    page.add(layout)