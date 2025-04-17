# -> Ferramentas (Framework) para criar sites / sistemas / aplicativos no Python:
# Flask
# Django
# FastAPI -> Python -> frontend / backend
# Kivy

# Framework -> biblioteca com regras específicas.


# Criar um chat

# Título: Hashzap
# Botão: Inicar Chat
    # quando eu clicar no botão:
        # apareça: Janela / Dialog / Modal / Popup
            # Título: Bem vindo ao Hashzap
            # Botão: Entrar no chat
                # clicou no botão:
                # Fechar o Dialog
                    # criar o chat
                    # criar o campo de mensagem: Digite sua mensagem
                    # botão: Enviar
                        # quando clicar no botão: 
                        # Envie a mensagem para o chat

# Regras para usar flet, instalar: pip install flet
# Passo 1: importar o flet
import flet as ft

# Passo 2: criar a função principal (main) do aplicativo
def main(pagina):
        print("Criou meu aplicativo")

# Passo 3: rodar o aplicativo
ft.app(main)