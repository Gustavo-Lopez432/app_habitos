import flet as ft
from UI.dashboard_window import dashboard_window
from UI.registro_window import registro_window
from UI.inicio_sesion_window import inicio_sesion_window


ft.app(target=inicio_sesion_window)
ft.app(target=registro_window)
ft.app(target=dashboard_window)