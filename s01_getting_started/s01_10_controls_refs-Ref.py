import flet
from flet import Column, ElevatedButton, TextField, Page, Text, Ref

def main(page: Page):
    txt_nombre = Ref[TextField]()
    txt_apellido = Ref[TextField]()
    col_controles = Ref[Column]()

    def saludar_clicked(event):
        col_controles.current.controls.append(Text(f'¡Hola, {txt_nombre.current.value} {txt_apellido.current.value}!'))

        txt_nombre.current.value = ''
        txt_apellido.current.value = ''
        page.update()
        txt_nombre.current.focus()

    btn_saludar = ElevatedButton('Saludar', on_click = saludar_clicked)

    page.add(
        TextField(ref = txt_nombre, label = 'Nombre', autofocus = True),
        TextField(ref = txt_apellido, label = 'Apellido'),
        btn_saludar,
        Column(ref=col_controles)
    )

#Ejecucion de la aplicacion en modo escritorio

flet.app(target=main)