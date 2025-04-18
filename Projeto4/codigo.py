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

        def enviar_mensagem_tunel(mensagem):
            texto_mensagem = ft.Text(mensagem) 
            chat.controls.append(texto_mensagem)
            pagina.update()

        # websocket -> túnel de comunicação*
        pagina.pubsub.subscribe(enviar_mensagem_tunel)   # criando túnel e passando por parâmetro a função que será executada p/ todo mundo.

        def enviar_mensagem(evento):
            mensagem = f"{campo_nome.value}: {campo_mensagem.value}" # valor dinâmico -> usar f-strings e colchetes
            # enviar a mensagem no tunel
            pagina.pubsub.send_all(mensagem)    # enviando mensagem (passada por parâmetro) para todo mundo
            campo_mensagem.value = ""       # limpar campo
            pagina.update()

        campo_mensagem = ft.TextField(label="Escreva sua mensagem", on_submit=enviar_mensagem)  #submit -> enviar com enter
        botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
        chat = ft.Column()
        linha_mensagem = ft.Row([campo_mensagem, botao_enviar])

        def entrar_chat(evento):
            pagina.pubsub.send_all(f"{campo_nome.value} entrou no chat")        # aviso de novo usuário no chat
            # fechar a janela / dialog
            janela.open = False
            # tirar o título
            pagina.remove(titulo)
            # tirar o botão iniciar
            pagina.remove(botao_iniciar)
            # criar o chat
            pagina.add(chat)
            # criar o campo digite sua mensagem
            # botão enviar
            pagina.add(linha_mensagem)
            pagina.update()

        campo_nome = ft.TextField(label="Digite o seu nome", on_submit=entrar_chat)
        botao_entrar = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)

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
#ft.app(main)         



# Obs.:
# sempre que clicamos em qualquer botão -> flet cria um evento (evento do click)
# sempre que atribuímos uma função ao botão, por padrão esta função tem que receber por parâmetro o evento do click do botão (evento)
# no Flet, permite que as edições no código apareçam sem recarregar a página -> "pagina.update()"
# túnel de comunicação* -> permite um usuário se comunicar com outro pela internet
# ver documentação p/ deploy no site https://flet.dev/docs/publish