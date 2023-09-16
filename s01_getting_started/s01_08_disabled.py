import flet
from flet import Column, Page, TextField

def main (page:Page):
    txt_first_name = TextField()
    txt_last_name = TextField()

    #Propiedad disabled asignada de forma individual:
    #txt_first_name.disabled = True
    #txt_last_name.disabled = True

    col_controls = Column(controls=[
        txt_first_name,
        txt_last_name
    ])
    col_controls.disabled = True
    page.add(col_controls)

#Ejecucion de la aplicacion en modo escritorio
flet.app(target=main)