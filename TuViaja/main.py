from ui import criar_tela_inicial
import webbrowser
from flet import Page, colors, app
# Definindo cores para reutilização
COR_COMBUSTIVEL = colors.RED
COR_VIAGEM = colors.GREEN
COR_TEXTO = colors.WHITE
COR_CINZA_ESCURO = "#333333"  # Usando código hexadecimal para cinza escuro

def main(page: Page):
    # Função para abrir o Instagram
    def abrir_instagram(e):
        webbrowser.open("https://www.instagram.com/vinny_luis")

    # Criar a tela inicial
    criar_tela_inicial(page)

if __name__ == "__main__":
    app(target=main)
