import flet
from flet import ElevatedButton, Page

def main(page:Page):
    btn_accion = ElevatedButton('¡Click!')

    page.add(btn_accion)

#Modo web
flet.app(target = main, view = flet.WEB_BROWSER)