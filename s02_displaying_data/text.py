import flet
from flet import Page, Text

def main(page:Page):
    lbl_texto = Text(
        value= '¡FLet y Python!',
        size = 30,
        color = 'green',
        bgcolor = 'black',
        weight = 'bold',
        italic = True
    )
    page.add (lbl_texto)

#aplicacion de escritorio
flet.app(target=main)