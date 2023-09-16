import flet
from flet import Column, ElevatedButton, TextField, Page, Text

def main(page: Page):
    txt_nombre = TextField(label = 'Nombre', autofocus =True)
    txt_apellido = TextField(label='Apellido')
    col_controles = Column()

    def saludar_clicked(event):
        col_controles.controls.append(Text(f'¡Hola, {txt_nombre.value} {txt_apellido.value}!'))

        txt_nombre.value = ''
        txt_apellido.value = ''
        page.update()
        txt_nombre.focus()

    btn_saludar = ElevatedButton('Saludar', on_click = saludar_clicked)

    page.add(
        txt_nombre,
        txt_apellido,
        btn_saludar,
        col_controles
    )

#Ejecucion de la aplicacion en modo escritorio

flet.app(target=main)