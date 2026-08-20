
#<----FORMULARIO DE REGISTRAR CUENTA---->

#<----IMPORTS NECESARIOS PARA QUE LA VENTANA FUNCIONE---->
import flet as ft

#<----DEFINE LA FUNCION PRINCIPAL DEL FORMULARIO---->
def registro_window(page: ft.Page):

    #<----CONFIGURACION GENERAL DE LA VENTANA---->
    page.title="Registro"
    page.bgcolor="#1A1625"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    #<----INPUTS - BOTONES - TEXTOS - ICONOS---->
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

    crear_cuenta=ft.ElevatedButton(
        "Crear cuenta",
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10)
        ),
        bgcolor="#9D7BFF",
        color="#EDEBF5",
        icon=ft.Icons.PERSON_ADD_ALT,   
        width=250
    )

    iniciar_sesion=ft.ElevatedButton(
        "Ya tengo una cuenta",
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10)
        ),
        bgcolor="#9D7BFF",
        color="#EDEBF5",
        icon=ft.Icons.LOGIN,
        width=250
    )

    icono_uptime=ft.Icon(
        icon=ft.Icons.INSIGHTS,
        width=100,
        height=100,
        size=70
    )

    divider=ft.Container(
        ft.Divider(),
        width=400
    )

    #<----FORMLUARIO---->
    formulario=ft.Container(
        
        #<----CONFIGURACION DEL FORMLUARIO---->
        width=600,
        height=800,
        bgcolor="#211C2E",
        border_radius=25,
        alignment=ft.Alignment.CENTER,

        #<----ORDEN DEL FORMULARIO---->
        content=ft.Column(
            controls=[

                #<----ICONO---->
                icono_uptime,
                
                #<----TITULO DE LA APP---->
                titulo,
                
                #<----FRASE---->
                subtitulo,

                #<----CAMPO NOMBRE---->
                nombre,

                #<----CAMPO CORREO---->
                correo,

                #<----CAMPO CONTRASEÑA---->
                password,

                #<----CAMPO CONFIRMAR CONTRASEÑA---->
                password_confirmar,

                #<----BOTON CREAR CUENTA---->
                crear_cuenta,

                divider,

                #<----BOTON INICIAR SESIÒN---->
                iniciar_sesion
            ],

            #<----CENTRA EL CONTENIDO DEL FORMULARIO---->
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15
        ),
    )

    #<----LAYOUT DE LA VENTANA---->
    layout=ft.Container(
        content=ft.Column(
            controls=[
                formulario,
            ]
        )
    )

    #<----AÑADE EL LAYOUT A LA PAGINA PRINCIPAL---->
    page.add(layout)