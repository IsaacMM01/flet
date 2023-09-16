import flet
from flet import Page, Text, TextField, Row, ElevatedButton

txt_nombre = TextField(label = 'Digite su nombre')

def main (page:Page):
    lbl_saludo = Text()
    def saludar(event):
        lbl_saludo.value =f'¡Hola {txt_nombre.value}!'
        page.update()

    row = Row(controls= [
        txt_nombre,
        ElevatedButton(text= 'Saludar', on_click =saludar),
        lbl_saludo
    ])
    page.add(row)

#Ejecucion en el escritorio
flet.app(target=main)