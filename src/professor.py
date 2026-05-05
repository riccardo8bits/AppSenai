import asyncio
from datetime import datetime

import flet
import ft
from flet import ThemeMode, View, AppBar, Colors, Button, FloatingActionButton, Icons, TextField, Column, Text, \
    DatePicker, Row, Dropdown, DropdownOption, ListView, ListTile, PopupMenuButton, Icon, PopupMenuItem, Container, \
    CrossAxisAlignment
from markdown_it.rules_block import lheading


class Professor:
    def __init__(self, nome, ano_nascimento, telefone, email, salario, turno, genero):
        self.nome = nome
        self.ano_nascimento = ano_nascimento
        self.telefone = telefone
        self.email = email
        self.salario = salario
        self.turno = turno
        self.genero = genero


def main(page: flet.Page):
    # Configurações
    page.title = "Primeiro app"
    page.theme_mode = ThemeMode.LIGHT
    page.window.width = 400
    page.window.height = 700

    lista_dados = []

    # Funções

    # Navegar
    def navegate(route):
        asyncio.create_task(

            page.push_route(route)

        )

    def ver_detalhes(professor):
        text_nome.value = professor.nome
        text_ano_nascimento.value = professor.ano_nascimento
        text_telefone.value = professor.telefone
        text_email.value = professor.email
        text_salario.value = professor.salario
        text_turno.value = professor.turno
        text_genero.value = professor.genero

        navegate("/detalhes")

    def salvar_dados():
        nome = input_nome.value.strip()
        nascimento = input_nascimento.value.strip()
        telefone = input_nascimento.value.strip()
        email = input_email.value.strip()
        salario = input_salario.value.strip()
        turno = input_turno.value
        genero = input_genero.value.strip()

        tem_erro = False

        if nome:
            input_nome.error = None
        else:
            tem_erro = True
            input_nome.error = "Campo obrigatório"

        if ano_nascimento:
            input_nascimento.error = None
        else:
            input_nascimento.error = "Campo obrigatório"

        if telefone:
            input_telefone.error = None
        else:
            input_telefone.error = "Campo obrigatório"

        if email:
            input_email.error = None
        else:
            input_email.error = "Campo obrigatório"

        if salario:
            input_salario.error = None
        else:
            input_salario.error = "Campo obrigatório"
        if turno:
            input_turno.error = None
        else:
            input_turno.error = "Campo obrigatório"

        if genero:
            input_genero.error = None
        else:
            input_genero.error = "Campo obrigatório"

        if not tem_erro:
            professor = Professor(
                nome=nome,
                ano_nascimento=nascimento,
                telefone=telefone,
                email=email,
                salario=salario,
                turno=turno,
                genero=genero
            )
            lista_dados.append(professor)

            input_nome.value = ""
            input_nascimento.value = ""
            input_telefone.value = ""
            input_email.value = ""

        mostrar_lista_padrao()


    def mostrar_lista_padrao():
        list_view.controls.clear()

        for item in lista_dados:
            list_view.controls.append(
                ListTile(
                    leading=Icon(Icons.MAN) if item.genero == "Masculino" else Icon(Icons.WOMAN),
                    title=item.nome,
                    subtitle=item.telefone,
                    trailing=PopupMenuButton(
                        icon=Icons.MORE_VERT,
                        items=[
                            PopupMenuItem("Ver detalhes", icon=Icons.REMOVE_RED_EYE, on_click=lambda _, professor=item: ver_detalhes(professor)),
                            PopupMenuItem("Excluir", icon=Icons.DELETE, on_click=lambda: excluir(item))

                        ]
                    ),
                )
            )

    def excluir(item):
        lista_dados.remove(item)
        mostrar_lista_padrao()

    # Gerenciar as telas(Routes)
    def route_change():
        page.views.clear()  # Limpar telas
        page.views.append(

            View(  # Tela

                route="/",
                controls=[  #
                    flet.AppBar(
                        title="Professores",
                        bgcolor=Colors.AMBER_200

                    ),
                    list_view,
                ],
                floating_action_button=FloatingActionButton(
                    icon=Icons.ADD,
                    on_click=lambda: navegate("/cadastro")

                )

            )
        )

        if page.route == "/cadastro":
            page.views.append(

                View(  # Tela

                    route="/cadastro",
                    controls=[
                        flet.AppBar(
                            title="Cadastro de professores",
                            bgcolor=Colors.AMBER_200

                        ),
                        Text("Digite seu nome:"),
                        input_nome,
                        Text("Ano de nascimento:"),
                        Row([
                            ano_nascimento,
                            input_nascimento,
                        ]),
                        Text("Digite seu telefone:"),
                        input_telefone,
                        Text("Digite seu email:"),
                        input_email,
                        Text("Digite seu sálario"),
                        input_salario,
                        Text("Turno?"),
                        input_turno,
                        Text("Digite seu gênero"),
                        input_genero,
                        btn_salvar

                    ]

                )
            )

        elif page.route == "/detalhes":
            page.views.append(
                View(
                    route="/detalhes",
                    controls=[
                        flet.AppBar(
                            title="Detalhes:",
                            bgcolor=Colors.AMBER_200,
                        ),
                        Container(
                            Column([
                                Row([
                                    Icon(Icons.ARROW_RIGHT_ROUNDED, size=40),
                                    text_nome
                                ]),
                                Row([
                                    Icon(Icons.ARROW_RIGHT_ROUNDED, size=40),
                                    text_telefone
                                ]),
                                Row([
                                    Icon(Icons.ARROW_RIGHT_ROUNDED, size=40),
                                    text_ano_nascimento
                                ]),
                                Row([
                                    Icon(Icons.ARROW_RIGHT_ROUNDED, size=40),
                                    text_turno
                                ]),
                                Row([
                                    Icon(Icons.ARROW_RIGHT_ROUNDED, size=40),
                                    text_genero
                                ]),
                                Row([
                                    Icon(Icons.ARROW_RIGHT_ROUNDED, size=40),
                                    text_salario
                                ]),
                                Row([
                                    Icon(Icons.ARROW_RIGHT_ROUNDED, size=40),
                                    text_email
                                ]),
                            ],
                                horizontal_alignment=CrossAxisAlignment.CENTER
                            ),
                        ),

                    ]
                )
            )

    # Voltar
    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)

    def select_date(date):
        print(date)
        input_nascimento.value = date.strftime("%Y-%m-%d")

    # Componentes
    input_nome = TextField(label="Digite seu Nome", hint_text="Digite seu nome", )
    ano_nascimento = Column(
        controls=[
            Button(
                "",
                icon=Icons.CALENDAR_MONTH,
                on_click=lambda e: e.control.page.show_dialog(
                    DatePicker(
                        first_date=datetime(1, 1, 1),
                        last_date=datetime(2026, 12, 30),
                        value=datetime.now(),
                        on_change=lambda e: select_date(e.control.value),
                    )
                ),
            ),
        ],
        width=50,
    )

    input_nascimento = TextField(width=300, hint_text="Digite seu nascimento:", disabled=True)
    input_telefone = TextField(label="Digite seu telefone:", hint_text=" (+55) 18991234854", )
    input_email = TextField(label="Digite seu email:", hint_text="exemplo@gmail.com", )
    input_salario = TextField(label="Digite seu salário:", hint_text="1512", )
    input_turno = Dropdown(
        label="Turno",
        options=[
            DropdownOption("Manhã"),
            DropdownOption("Tarde"),
            DropdownOption("Noite"),

        ]

    )

    input_genero = Dropdown(
        label="Gênero",
        options=[
            DropdownOption("Masculino"),
            DropdownOption("Feminino"),

        ]

    )

    # text_nome = professor.nome
    # text_ano_nascimento = professor.ano_nascimento
    # text_telefone = professor.telefone
    # text_email = professor.email
    # text_salario = professor.salario
    # text_turno = professor.turno
    # text_genero = professor.genero

    text_nome = Text()
    text_ano_nascimento = Text()
    text_telefone = Text()
    text_email = Text()
    text_salario = Text()
    text_turno = Text()
    text_genero = Text()



    btn_salvar = Button("Salvar", width=400, on_click=lambda: salvar_dados())
    list_view = ListView(height=500)

    # Eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()


flet.run(main)

