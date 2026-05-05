import asyncio

import flet
from flet import ThemeMode, View, AppBar, Colors, Button, TextField
import flet
from flet import ThemeMode, Text, TextField, OutlinedButton, Column, CrossAxisAlignment, Container, Colors, FontWeight
from datetime import datetime


#
def main(page: flet.Page):
    # Configurações
    page.title = "Primeiro app"
    page.theme_mode = ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700

    # Funções
    def mostra_nome():
        text_exibir.value = f"Hello {text_name.value}!!!"
        page.update()
        navegate("/segunda_tela")














    # Navegar
    def navegate(route):
        asyncio.create_task(

            page.push_route(route)

        )



    # Gerenciar as telas(Routes)
    def route_change():
        page.views.clear()  # Limpar telas
        page.views.append(

            View(  #Tela


                route="/",
                controls=[
                    flet.AppBar(
                        title="First Page",
                        bgcolor=Colors.PINK,





                    ),
                    text,
                    text_name,
                    bnt_save

                ]

            )
        )



        if page.route == "/segunda_tela":
            page.views.append(

                View(  # Tela

                    route="/segunda_tela",
                    controls=[
                        flet.AppBar(
                            title="Second page",
                            bgcolor=Colors.PINK



                        ),
                        text_exibir,


                    ]

                )
            )




    # Voltar
    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)



    # Componentes
    text = Text("What's your name?")
    text_exibir = Text("What's your name?")
    text_name = TextField("")
    bnt_save = Button("Save changes", on_click=mostra_nome)


    # Eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()

flet.run(main)