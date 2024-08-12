from flet import Page, TextField, ElevatedButton, Text, Column, Container, colors, Image, GestureDetector, Row, alignment
from func import calcular_combustivel, calcular_custo_viagem
import webbrowser

def criar_tela_calculo_combustivel(page: Page):
    def on_calcular_combustivel(_):
        try:
            preco_alcool = float(txt_preco_alcool.value.replace(',', '.'))
            preco_gasolina = float(txt_preco_gasolina.value.replace(',', '.'))
            resultado = calcular_combustivel(preco_alcool, preco_gasolina)
            lbl_resultado.value = resultado
        except ValueError:
            lbl_resultado.value = "Erro: Verifique se os valores estão corretos."
        lbl_resultado.update()

    def validar_entrada(event):
        # Permitir apenas números e ponto
        event.control.value = ''.join(c for c in event.control.value if c.isdigit() or c == ',' or c == '.')
        event.control.update()

    # Campos de texto e botão de cálculo
    txt_preco_alcool = TextField(label="Preço do Álcool", on_change=validar_entrada)
    txt_preco_gasolina = TextField(label="Preço da Gasolina", on_change=validar_entrada)
    btn_calcular = ElevatedButton("Calcular", on_click=on_calcular_combustivel, bgcolor="#4CAF50", color=colors.WHITE)
    lbl_resultado = Text()
    btn_voltar = ElevatedButton("Voltar", on_click=lambda _: criar_tela_inicial(page), bgcolor=colors.BLUE, color=colors.WHITE)


    # Adicionando elementos à página
    page.controls.clear()
    page.add(
        Container(
            content=Column(
                controls=[
                    txt_preco_alcool,
                    txt_preco_gasolina,
                    btn_calcular,
                    lbl_resultado,
                    btn_voltar  # Adicionando o botão "Voltar"
                ],
                alignment="center",
                horizontal_alignment="center",
                spacing=10
            ),
            bgcolor="#333333",
            padding=20,
            expand=True
        )
    )
    page.update()

def criar_tela_calculo_viagem(page: Page):
    def on_calcular_viagem(_):
        try:
            distancia = float(txt_distancia.value.replace(',', '.'))
            consumo = float(txt_consumo.value.replace(',', '.'))
            preco_combustivel = float(txt_preco_combustivel.value.replace(',', '.'))
            pedagio = float(txt_pedagio.value.replace(',', '.')) if txt_pedagio.value else 0.0
            custo_total = calcular_custo_viagem(distancia, consumo, preco_combustivel, pedagio)
            lbl_resultado.value = f"Custo Total: R$ {custo_total:.2f}"
        except ValueError:
            lbl_resultado.value = "Erro: Verifique se os valores estão corretos."
        lbl_resultado.update()

    def validar_entrada(event):
        # Permitir apenas números, vírgula e ponto
        event.control.value = ''.join(c for c in event.control.value if c.isdigit() or c == ',' or c == '.')
        event.control.update()

    # Campos de texto e botão de cálculo
    txt_distancia = TextField(label="Distância (km)", on_change=validar_entrada)
    txt_consumo = TextField(label="Quantos Km por litro o seu veículo faz? (km/l)", on_change=validar_entrada)
    txt_preco_combustivel = TextField(label="Preço do combustível que irá usar", on_change=validar_entrada)
    txt_pedagio = TextField(label="Valor dos Pedágios (Opcional)", on_change=validar_entrada)
    btn_calcular = ElevatedButton("Calcular", on_click=on_calcular_viagem, bgcolor="#F44336", color=colors.WHITE)
    lbl_resultado = Text()
    btn_voltar = ElevatedButton("Voltar", on_click=lambda _: criar_tela_inicial(page), bgcolor=colors.BLUE, color=colors.WHITE)

    # Adicionando elementos à página
    page.controls.clear()
    page.add(
        Container(
            content=Column(
                controls=[
                    txt_distancia,
                    txt_consumo,
                    txt_preco_combustivel,
                    txt_pedagio,
                    btn_calcular,
                    lbl_resultado,
                    btn_voltar  # Adicionando o botão "Voltar"
                ],
                alignment="center",
                horizontal_alignment="center",
                spacing=10
            ),
            bgcolor="#333333",
            padding=20,
            expand=True
        )
    )
    page.update()

def criar_tela_inicial(page: Page):
    def abrir_instagram(e):
        webbrowser.open("https://www.instagram.com/vinny_luis")

    # Título
    txt_titulo = Text("TuViaja", size=24, color=colors.WHITE, text_align="center", weight="bold")

    # Botões
    btn_combustivel = ElevatedButton(
        "Calcular Combustível",
        on_click=lambda _: criar_tela_calculo_combustivel(page),
        bgcolor=colors.RED,
        color=colors.WHITE,
    )

    btn_viagem = ElevatedButton(
        "Calcular Viagem",
        on_click=lambda _: criar_tela_calculo_viagem(page),
        bgcolor=colors.GREEN,
        color=colors.WHITE,
    )

    # Rodapé com link para o Instagram
    icone_instagram = Image(src="instagram_icon.png", width=20, height=20)
    txt_rodape = GestureDetector(
        on_tap=abrir_instagram,
        content=Row(
            controls=[
                icone_instagram,
                Text("Desenvolvido @vinny_luis", color=colors.WHITE, size=12)
            ],
            alignment="center",
            spacing=5
        )
    )

    # Layout da página
    page.controls.clear()
    page.add(
        Container(
            content=Column(
                controls=[txt_titulo, btn_combustivel, btn_viagem, txt_rodape],
                alignment="center",
                horizontal_alignment="center",
                spacing=20,
            ),
            alignment=alignment.center,
            padding=20,
            bgcolor="#333333",
            expand=True
        )
    )
    page.update()