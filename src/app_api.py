import asyncio
from pydoc import describe

import flet
from flet import ThemeMode, View, Colors, ListView, Icons, ListTile, Image, Column, Text, \
    Pagelet, NavigationBar, NavigationBarDestination, ScrollMode, FontWeight, Card, Row

from src.api_endpoints import get_planetas, get_personagens


def main(page: flet.Page):
    # Configurações
    page.title = "Exemplo de API"
    page.theme_mode = ThemeMode.LIGHT  # ou ThemeMode.Light
    page.window.width = 400
    page.window.height = 700

    # Funções
    # Navegar
    def navegar(route):
        asyncio.create_task(
            page.push_route(route)
        )
    def genero(item):

        color = Colors.RED


        gender = item["gender"]

        if gender == "Male":
            color= Colors.BLUE
            return color
        elif gender == "Female":
            color = Colors.PINK
            return color
        else:
            color = Colors.RED
            return color














    def montar_lista_personagens():
        list_view.controls.clear()

        lista_dados = get_personagens()

        for item in lista_dados["items"]:
            list_view.controls.append(
                Card(
                    height=200,
                    content=Row([
                        Image(src=item["image"], width=90),
                        Column([
                            Text(item["name"], weight=FontWeight.BOLD),
                            Text(f"Ki - {item["ki"]}", color=Colors.BLACK),
                            Text(f"Gender - {item["gender"]}", color=genero(item)),
                        ]),
                    ]),
                )
            )

        # TODO: Montar a lista de personagens do seu jeito, capricha ein

    def montar_lista_planetas():
        list_view.controls.clear()

        # chamar a função que busca na api
        lista_dados = get_planetas()

        # item é um apelido para o objeto que esta vindo da api
        for item in lista_dados["items"]:
            list_view.controls.append(
                ListTile(

                    leading=Image(src=item["image"], width=60),
                    title=Text(item["name"], weight=FontWeight.BOLD, color=Colors.ORANGE),
                    subtitle=Text(item["description"], max_lines=2, color=Colors.GREY),

                )
            )

    def define_lista(e):
        # Muda a lista de acordo com o indice do NavigationBar
        return montar_lista_planetas() if e.data == 1 else montar_lista_personagens()

    # Gerenciar as telas(routes)
    def route_change():

        # montar_lista()
        montar_lista_personagens()

        page.views.clear()

        page.views.append(
            View(
                route="/",
                controls=[
                    flet.AppBar(
                        title=Text("Dragon Ball Z", weight=FontWeight.BOLD),
                        bgcolor=Colors.ORANGE
                    ),
                    Column([
                        pagelet,
                    ])
                ],
                padding=0
            )
        )

    # Voltar
    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)

    # Componentes
    list_view = ListView(height=500)

    pagelet = Pagelet(
        navigation_bar=NavigationBar(
            destinations=[
                NavigationBarDestination(icon=Icons.MAN, label="Personagens"),
                NavigationBarDestination(icon=Icons.BLUR_ON, label="Planetas"),
            ],
            on_change=define_lista,
        ),
        content=Column([
            list_view,
        ],
            scroll=ScrollMode.HIDDEN,
            height=500
        ),
        height=600,
    )

    #  eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()


flet.run(main)
