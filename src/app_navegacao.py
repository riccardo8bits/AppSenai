import asyncio

import flet
from flet import ThemeMode, View, AppBar, Colors, Button


def main(page: flet.Page):
    # Configurações
    page.title = "Primeiro app"
    page.theme_mode = ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700

    # Funções

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
                controls=[#
                    flet.AppBar(
                        title="First Page",
                        bgcolor=Colors.PINK


                    ),

                    Button("Next page", on_click=lambda:navegate ("/segunda_tela"))
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

                        )

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


    # Eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()

flet.run(main)