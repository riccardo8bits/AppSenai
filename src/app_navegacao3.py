import asyncio

import flet
from flet import ThemeMode, View, AppBar, Colors, Button, TextField
import flet
from flet import ThemeMode, Text, TextField, OutlinedButton, Column, CrossAxisAlignment, Container, Colors, FontWeight
from datetime import datetime



def main(page: flet.Page):
    # Configurações
    page.title = "Primeiro app"
    page.theme_mode = ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700

    # Funções
    def mostra_nome():
        text_display.value = f"NOME: {text_name.value}"
        text_display_cpf.value = f"CPF: {text_cpf.value}"
        text_display_email.value = f"E-mail: {text_email.value}"
        text_display_salary.value = f"Salary: {text_salary.value}"


        tem_erro = False

        if text_name.value:
            text_name.error = None
        else:
            tem_erro = True
            text_name.error = "Campo obrigatório"

        if text_cpf.value:
            text_cpf.error = None
        else:
            tem_erro = True
            text_cpf.error = "Campo obrigatório"

        if text_email.value:
            text_email.error = None
        else:
            tem_erro = True
            text_email.error = "Campo obrigatório"

        if text_salary.value:
            text_salary.error = None

        else:
            tem_erro = True
            text_salary.error = "Campo obrigatório"

        if not tem_erro:
            text_name.value = ""
            text_cpf.value = ""
            text_email.value = ""
            text_salary.value = ""
            navegate("/segunda_tela")















#

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
                    text_name_cpf,
                    text_cpf,
                    text_name_email,
                    text_email,
                    text_name_salary,
                    text_salary,
                    bnt_save,



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
                        text_display,
                        text_display_cpf,
                        text_display_email,
                        text_display_salary



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
    #Nome:
    text = Text("What's your name?")
    text_display = Text("")
    text_name = TextField("")

    #CPF:
    text_name_cpf = Text("What's your CPF?")
    text_display_cpf = Text("")
    text_cpf = TextField("")

    #EMAIL

    text_name_email = Text("What's your email address?")
    text_display_email = Text("")
    text_email = TextField("")

    #SALÁRIO

    text_name_salary = Text("What's your salary?")
    text_display_salary = Text("")
    text_salary = TextField("")



    bnt_save = Button("Save changes", on_click=mostra_nome)


    # Eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()

flet.run(main)