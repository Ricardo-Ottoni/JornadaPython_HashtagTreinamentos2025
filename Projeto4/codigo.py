# -> Ferramentas (Framework*) para criar sites / sistemas / aplicativos no Python:
# Flask -> Criar site, somente backend, lógica de servidor.

# Django -> Criar site, somente backend, incluindo gerenciamento de banco de dados e autenticação de usuários.

# FastAPI -> Criar site, somente backend, criar APIs.

# Flet -> Python -> faz o frontend e backend para site, sistema e app. 

# Kivy -> Criar app's grágicos e móveis, somente frontend.

# *Framework -> biblioteca com regras específicas.


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
# função main é o ponto de entrada do app, recebe como parâmetro um objeto (pagina)
def main(pagina):              
        #criar os elementos
        titulo = ft.Text("Hashzap")

        titulo_janela = ft.Text("Bem vindo ao Hashzap")
        campo_nome = ft.TextField()
        botao_entrar = ft.ElevatedButton("Entrar no chat")
        janela = ft.AlertDialog(
            title=titulo_janela,
            content=campo_nome,
            actions=[botao_entrar] 
        )

        def abrir_dialog(evento):               # precisa receber um parâmetro
                pagina.dialog = janela          # criar janela
                janela.open = True              # abrir janela
                pagina.update()                 # recarrega a página automaticamente

        botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=abrir_dialog)

        # colocar os elementos na página
        pagina.add(titulo)
        pagina.add(botao_iniciar)

# Passo 3: rodar o aplicativo
ft.app(main, view=ft.WEB_BROWSER)           # ctrl+c no terminal -> parar de rodar



# Obs.:
# sempre que clicamos em qualquer botão -> flet cria um evento (evento do click)
# no Flet, permite que as edições no código apareçam sem recarregar a página -> "pagina.update()"