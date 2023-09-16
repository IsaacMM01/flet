import flet
from flet import Checkbox, ElevatedButton, Row, TextField, Page

def main(page: Page):
    def agregar_tarea_clicked(event):
        page.add(Checkbox(label = txt_nueva_tarea.value))

    txt_nueva_tarea = TextField(hint_text = '¿Cual tarea desea agregar?', width = 300)

    btn_agregar_tarea = ElevatedButton('Agregar', on_click = agregar_tarea_clicked)
    page.add(Row([
        txt_nueva_tarea, 
        btn_agregar_tarea]))

flet.app(target = main)