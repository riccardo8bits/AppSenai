from cProfile import label

import flet
from flet import ThemeMode, Text, TextField, OutlinedButton, Column, CrossAxisAlignment, Container, Colors, FontWeight
from datetime import datetime


tempo = (datetime.now()).year
def main(page: flet.Page):
    # Configurações
    page.title = "Primeiro app"
    page.theme_mode = ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700

    # Funções
    def salvar_nome():
        text.value = f"Bom dia {input_nome.value} {input_sobrenome.value}"
        page.update()

    def impar_par():
        num_convertido = int(input_numero_impar_par.value)

        if num_convertido % 2 == 0:
            result = "Par"
        else:
            result = "Impar"


        text2.value = f"Seu numero é {result}"
        page.update()

    def verificar_idade():
        idade = int(input_digite_idade.value)

        calculo = tempo - idade
        if calculo >= 18:
            texto = f"Você tem {calculo} anos. Você é maior de idade"
        else:
            texto = f"Você tem {calculo} anos. Você é menor de idade "

        text3.value = texto
        page.update()

    # Componentes
    text_saudacao = Text("Olá! digite seu nome")
    text = Text("")
    input_nome = TextField(label="Digite seu nome: ")
    input_sobrenome = TextField(label="Digite seu sobrenome: ")
    btn_salvar = OutlinedButton("Salvar", on_click=salvar_nome)
    input_numero_impar_par = TextField(label = "Digite seu numero: ")
    text2 = Text("")
    btn_nm = OutlinedButton("ver", on_click=impar_par)
    input_digite_idade = TextField(label="Digite o ano do seu nascimento: ")
    text3 = Text("")
    btn_idade = OutlinedButton("Calcular", on_click=verificar_idade)

    # Construção da tela
    page.add(
        Column(
            [
                text_saudacao,
                Container(
                    Column(
                        [
                            Text("Atividade 1", weight=FontWeight.BOLD, color=Colors.RED_500, size=25),
                            input_nome,
                            input_sobrenome,
                            btn_salvar,
                            text,
                        ],
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                    ),
                    bgcolor=Colors.INDIGO_900,
                    padding=15,
                    border_radius=10,
                    width=300,
                ),

                Container(
                    Column(
                        [
                            input_numero_impar_par,
                            btn_nm,
                            text2,
                        ],
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                    ),
                    bgcolor=Colors.PINK,
                    padding=15,
                    border_radius=10,
                    width=300,
                ),

                Container(
                    Column(
                        [
                            input_digite_idade,
                            btn_idade,
                            text3
                        ],
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                    ),
                    bgcolor=Colors.GREEN,
                    padding=15,
                    border_radius=10,
                    width=300,
                )


            ],
            width=400,
            horizontal_alignment=CrossAxisAlignment.CENTER
        )
    )

flet.run(main)
