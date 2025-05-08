import flet as ft

def main(page: ft.Page):
    #Configuração da página
    page.title = 'Minha aplicação Flet'
    page.theme_mode = ft.ThemeMode.DARK #ou ft.ThemeMode.LIGHT
    page.window.width = 375
    page.window.height = 667

    #Definição de funções


    #Criação de componentes
    input_nome = ft.TextField(label='Nome:', hint_text='EX: Fernanda')

    #Construir o layout
    page.add(
        input_nome
    )


ft.app(main)