import tkinter as tk
import sqlite3
import tkinter as tk
from datetime import datetime, timedelta
from tkinter import Tk, ttk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

################################################################

################################################################

janela = tk.Tk()
janela.title('Login')
janela.geometry('750x500')
janela.resizable(False, False)

style = ttk.Style()
style.element_create("Transparent.Tlabelframe", "from", "clam")
style.layout("Transparent.Tlabelframe",
             [("Transparent.Tlabelframe.border", {"sticky": "nswe",
                                                  "children": [("Transparent.Tlabelframe.padding", {"sticky": "nswe",
                                                                                                    "children": [(
                                                                                                        "Transparent.Tlabelframe.label",
                                                                                                        {
                                                                                                            "sticky": "w"})]})]})])


def BANCO():
    conexao = sqlite3.connect("Projetos_Pessoais\Agenda\Banco de Dados\database.db")
    cursor = conexao.cursor()
    cursor.execute("""create table if not exists LOGIN
                   (CPF INTEGER PRIMARY KEY AUTOINCREMENT,
                    NOME TEXT,
                    CELULAR INTEGER,
                    EMAIL TEXT,
                    SENHA TEXT)""")
    conexao.close()


def salvar_cadastro():
    conexao = sqlite3.connect("Projetos_Pessoais\Agenda\Banco de Dados\database.db")
    cursor = conexao.cursor()
    cursor.execute("""
                   insert into LOGIN
                   (CPF, NOME, CELULAR, EMAIL, SENHA)
                   values (?, ?, ?, ?, ?)""",
                   (en_cpf.get(),
                    en_nome.get(),
                    en_celular.get(),
                    en_email.get(),
                    en_senha.get()))
    conexao.commit()
    conexao.close()

    MAIN_ADM()


def limpar_janela():
    for widget in janela.winfo_children():
        widget.destroy()


def MAIN_ADM():
    limpar_janela()

    global entry_login, entry_senha
    global lf_main_adm, im_main_admin, ft_main_admin, lb_main_admin

    janela.geometry('1000x520')
    janela.title("Login")
    janela.configure(background="white")

    lf_main_adm = LabelFrame(janela, text='Main Authorization', labelanchor='n')
    lf_main_adm.place(relx=0.5, rely=0.5, anchor=CENTER)
    lf_transparente = ttk.Labelframe(janela, text="Login", style="Transparent.TLabelframe")
    lf_transparente.place(relx=0.5, rely=0.45, anchor=tk.CENTER)

    im_main_admin = Image.open("Projetos_Pessoais\Agenda\Imagens\Main.jpg")
    ft_main_admin = ImageTk.PhotoImage(im_main_admin)
    lb_main_admin = tk.Label(lf_main_adm, image=ft_main_admin)
    lb_main_admin.grid(row=0, column=0, padx=10, pady=10)

    btn_voltar = ttk.Button(lf_main_adm, text="Voltar")
    btn_voltar.grid(row=1, column=0, pady=10)

    label_login = ttk.Label(lf_transparente, text="Login:")
    label_login.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)

    entry_login = ttk.Entry(lf_transparente)
    entry_login.grid(row=0, column=1, padx=5, pady=5)

    label_senha = ttk.Label(lf_transparente, text="Senha:")
    label_senha.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)

    entry_senha = ttk.Entry(lf_transparente, show="*")
    entry_senha.grid(row=1, column=1, padx=5, pady=5)

    button_entrar = ttk.Button(lf_transparente, text="Entrar", command=login)
    button_entrar.grid(row=2, column=0, padx=5, pady=10)
    button_cadastro = ttk.Button(lf_transparente, text="Cadastro", command=cadastro)
    button_cadastro.grid(row=2, column=1, padx=5, pady=10)


def login():
    janela.title("Login")
    janela.configure(background="white")

    CPF = entry_login.get()
    SENHA = entry_senha.get()

    conn = sqlite3.connect("Projetos_Pessoais\Agenda\Banco de Dados\database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM LOGIN WHERE CPF=? AND SENHA=?", (CPF, SENHA))
    user = cursor.fetchone()

    if user:
        messagebox.showinfo('Sucesso', 'Login realizado com sucesso.')
        print("Login realizado com sucesso!")
        limpar_janela()
        MAIN()
    else:
        messagebox.showerror('Erro', 'Usuário ou senha incorretos.')
        print("Login não realizado")
    conn.close()


def cadastro():
    global im_cadastro, ft_cadastro, lb_cadastro, en_cpf, en_nome, en_celular, en_email, en_senha

    limpar_janela()
    janela.title("Cadastro")
    janela.geometry("529x300")

    lf_im_cadastro = LabelFrame(janela)
    lf_im_cadastro.place(relx=0.5, rely=0.5, anchor=CENTER)

    im_cadastro = Image.open("Projetos_Pessoais\Agenda\Imagens\Cadastro.png")
    ft_cadastro = ImageTk.PhotoImage(im_cadastro)
    lb_cadastro = tk.Label(lf_im_cadastro, image=ft_cadastro)
    lb_cadastro.grid(row=0, column=0, padx=10, pady=10)

    lf_cadastro = ttk.LabelFrame(janela, text="ADM Cadastro", labelanchor="n", style="Transparent.TLabelframe")
    lf_cadastro.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    lb_cpf = ttk.Label(lf_cadastro, text="CPF:", anchor='e')
    lb_cpf.grid(row=0, column=0, padx=10, pady=10, sticky='we')
    en_cpf = ttk.Entry(lf_cadastro)
    en_cpf.grid(row=0, column=1, padx=10, pady=10, sticky='we')

    lb_nome = ttk.Label(lf_cadastro, text="Nome:", anchor='e')
    lb_nome.grid(row=1, column=0, padx=10, pady=10, sticky='we')
    en_nome = ttk.Entry(lf_cadastro)
    en_nome.grid(row=1, column=1, padx=10, pady=10, sticky='we')

    lb_celular = ttk.Label(lf_cadastro, text="Celular:", anchor='e')
    lb_celular.grid(row=2, column=0, padx=10, pady=10, sticky='we')
    en_celular = ttk.Entry(lf_cadastro)
    en_celular.grid(row=2, column=1, padx=10, pady=10, sticky='we')

    lb_email = ttk.Label(lf_cadastro, text="Email:", anchor='e')
    lb_email.grid(row=3, column=0, padx=10, pady=10, sticky='we')
    en_email = ttk.Entry(lf_cadastro)
    en_email.grid(row=3, column=1, padx=10, pady=10, sticky='we')

    lb_senha = ttk.Label(lf_cadastro, text="Senha:", anchor='e')
    lb_senha.grid(row=4, column=0, padx=10, pady=10, sticky='we')
    en_senha = ttk.Entry(lf_cadastro, show="*")
    en_senha.grid(row=4, column=1, padx=10, pady=10, sticky='we')

    bt_salvar = ttk.Button(lf_cadastro, text="Salvar", command=salvar_cadastro)
    bt_salvar.grid(row=5, column=0, padx=10, pady=10)

    bt_voltar = ttk.Button(lf_cadastro, text="Voltar", command=MAIN_ADM)
    bt_voltar.grid(row=5, column=1, padx=10, pady=10)


def MAIN():
    global lf_tela_toda, lf_menu, lf_pesquisa, lf_compromissos, lf_adsense, lf_calendario, lf_diario
    janela.title('MAIN')
    janela.state('zoomed')
    janela.configure(padx=10, pady=10)
    lf_tela_toda = ttk.LabelFrame(janela)
    lf_tela_toda.place(relx=0.5, rely=0.5, anchor='center')

    lf_menu = ttk.LabelFrame(lf_tela_toda, text="Menu Principal", labelanchor='n')
    lf_menu.grid(row=0, rowspan=9, column=0, padx=10, pady=10, sticky='nswe')
    barra_Lateral()
    lf_pesquisa = ttk.LabelFrame(lf_tela_toda, text="Pesquisa", labelanchor='n')
    lf_pesquisa.grid(row=0, column=1, columnspan=5, padx=10, pady=10, sticky='we')
    barra_pesquisa()
    lf_compromissos = ttk.LabelFrame(lf_tela_toda, text="Compromissos", labelanchor='n')
    lf_compromissos.grid(row=1, rowspan=2, column=1, columnspan=3, padx=10, pady=10, sticky='nswe')
    barra_compromisso()
    lf_adsense = ttk.LabelFrame(lf_tela_toda, text="Adsense", labelanchor='n')
    lf_adsense.grid(row=1, rowspan=2, column=4, padx=10, pady=10, sticky='nswe')
    barra_adsense()
    lf_calendarios = ttk.LabelFrame(lf_tela_toda, text="Calendario", labelanchor='n')
    lf_calendarios.grid(row=3, rowspan=6, column=1, columnspan=2, padx=10, pady=10, sticky='nswe')
    lf_calendario = ttk.LabelFrame(lf_calendarios)
    lf_calendario.pack(expand=True)
    barra_calendario()
    lf_diario = ttk.LabelFrame(lf_tela_toda, text="Diario", labelanchor='n')
    lf_diario.grid(row=3,rowspan=6, column=3, columnspan=2, padx=10, pady=10, sticky='nswe')
    barra_diario()
    carregar_anotacoes() # Carrega o conteúdo do arquivo ao chamar a função


def barra_Lateral():
    global im_logo, ft_logo, lb_logo

    im_logo = Image.open("Projetos_Pessoais\Agenda\Imagens\Logo.jpeg").resize((200, 200))
    ft_logo = ImageTk.PhotoImage(im_logo)
    lb_logo = tk.Label(lf_menu, image=ft_logo)
    lb_logo.grid(row=0, column=0, padx=10, pady=10)

    lb_menu_inicial = ttk.Label(lf_menu, text="Menu Inicial")
    lb_menu_inicial.grid(row=1, column=0, padx=10, pady=20)
    lb_tarefas = ttk.Label(lf_menu, text="Tarefas Diarias")
    lb_tarefas.grid(row=2, column=0, padx=10, pady=20)
    lb_contas = ttk.Label(lf_menu, text="Contas a pagar")
    lb_contas.grid(row=3, column=0, padx=10, pady=20)
    lb_sonhos = ttk.Label(lf_menu, text="Sonhos de Compra")
    lb_sonhos.grid(row=4, column=0, padx=10, pady=20)
    lb_preciso = ttk.Label(lf_menu, text="Coisas que Preciso")
    lb_preciso.grid(row=5, column=0, padx=10, pady=20)
    lb_diario = ttk.Label(lf_menu, text="Diario")
    lb_diario.grid(row=6, column=0, padx=10, pady=20)
    lb_bloco = ttk.Label(lf_menu, text="Bloco de Notas")
    lb_bloco.grid(row=7, column=0, padx=10, pady=20)
    lb_calendario = ttk.Label(lf_menu, text="Calendario")
    lb_calendario.grid(row=8, column=0, padx=10, pady=20)
    lb_apoio = ttk.Label(lf_menu, text="Apoie o Desenvolvedor")
    lb_apoio.grid(row=9, column=0, padx=10, pady=20)
    lb_configuracao = ttk.Label(lf_menu, text="Configuração")
    lb_configuracao.grid(row=10, column=0, padx=10, pady=20)
    lb_colaboradores = ttk.Label(lf_menu, text="Colaboradores")
    lb_colaboradores.grid(row=11, column=0, padx=10, pady=20)

    lb_patrocinios = ttk.Label(lf_menu, text="Patrocinios", width=20, background="gray")
    lb_patrocinios.grid(row=12, column=0, padx=10, pady=20, sticky='nswe')


def barra_pesquisa():
    lb_pesquisa = ttk.Label(lf_pesquisa, text="Pesquisa")
    lb_pesquisa.grid(row=1, column=0, padx=10, pady=10, sticky='we')
    en_pesquisa = ttk.Entry(lf_pesquisa)
    en_pesquisa.grid(row=1, column=1, padx=10, pady=10, sticky='we')
    bt_pesquisa = ttk.Button(lf_pesquisa, text="Pesquisa")
    bt_pesquisa.grid(row=1, column=2, padx=10, pady=10, sticky='we')


def barra_compromisso():
    lf_compromisso1 = ttk.LabelFrame(lf_compromissos, text="Compromisso Importante", labelanchor='n')
    lf_compromisso1.grid(row=0, column=0, padx=10, pady=10, sticky='nswe')
    lb_compromisso1 = ttk.Label(lf_compromisso1, text="Compromisso Importante aqui")
    lb_compromisso1.grid(row=0, column=0, padx=10, pady=10, sticky='nswe')

    lf_compromisso2 = ttk.LabelFrame(lf_compromissos, text="Compromisso Importante", labelanchor='n')
    lf_compromisso2.grid(row=0, column=2, padx=10, pady=10, sticky='nswe')
    lb_compromisso2 = ttk.Label(lf_compromisso2, text="Compromisso Importante aqui")
    lb_compromisso2.grid(row=0, column=2, padx=10, pady=10, sticky='nswe')
    
    lf_compromisso3 = ttk.LabelFrame(lf_compromissos, text="Compromisso Importante", labelanchor='n')
    lf_compromisso3.grid(row=0, column=3, padx=10, pady=10, sticky='nswe')
    lb_compromisso3 = ttk.Label(lf_compromisso3, text="Compromisso Importante aqui")
    lb_compromisso3.grid(row=0, column=3, padx=10, pady=10, sticky='nswe')

    lf_compromisso4 = ttk.LabelFrame(lf_compromissos, text="Compromisso Importante", labelanchor='n')
    lf_compromisso4.grid(row=0, column=4, padx=10, pady=10, sticky='nswe')
    lb_compromisso4 = ttk.Label(lf_compromisso4, text="Compromisso Importante aqui")
    lb_compromisso4.grid(row=0, column=4, padx=10, pady=10, sticky='nswe')


def barra_adsense():
    lb_adsense = ttk.Label(lf_adsense, text="Adsense, adsense, Adsense\nadsense, Adsense, adsense\nadsense, Adsense, adsense")
    lb_adsense.grid(row=0, column=0, padx=10, pady=10, sticky='nswe')
    
    
def barra_calendario():
    class CalendarioApp:
        def __init__(self):

            self.btn_atualizar = tk.Button(lf_calendario, text="Atualizar", command=self.atualizar_calendario)
            self.btn_atualizar.pack(pady=10)

            self.atualizar_calendario()



        def atualizar_calendario(self, event=None):
            now = datetime.now()
            current_year = now.year
            current_month = now.month

            # Obter o primeiro dia da semana (0=segunda-feira, 6=domingo)
            first_day_weekday = (datetime(current_year, current_month, 1).weekday() + 1) % 7

            # Limpar o calendário existente
            for widget in lf_calendario.winfo_children():
                widget.destroy()

            # Criar os rótulos dos dias da semana
            for i, weekday in enumerate(['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']):
                label_weekday = tk.Label(lf_calendario, text=weekday, font="Arial 12 bold")
                label_weekday.grid(row=0, column=i, padx=5, pady=5)

            # Configurar o contêiner para preencher o espaço disponível
            lf_calendario.grid_rowconfigure(0, weight=1)
            lf_calendario.grid_columnconfigure(0, weight=1)

            # Preencher o calendário com os dias do mês
            day = 1
            for row in range(1, 7):
                for col in range(7):
                    if row == 1 and col < first_day_weekday:
                        # Dias vazios no início do mês
                        continue
                    if day > self.get_num_days(current_year, current_month):
                        # Todos os dias do mês foram preenchidos
                        break

                    lf_dia = tk.LabelFrame(lf_calendario)
                    lf_dia.grid(row=row, column=col, padx=5, pady=5)

                    label_dia = tk.Label(lf_dia, text=str(day)+'\n Compromisso!', font="Arial 12 bold")
                    label_dia.pack()

                    day += 1

        def get_num_days(self, year, month):
            if month == 12:
                next_month = 1
                next_year = year + 1
            else:
                next_month = month + 1
                next_year = year
            num_days = (datetime(next_year, next_month, 1) - timedelta(days=1)).day
            return num_days

    # Criar uma instância da classe CalendarioApp
    app = CalendarioApp()

def barra_diario():
    global anotacoes, text_anotacoes, button_salvar, carregar_anotacoes

    def salvar_anotacoes():
        anotacoes = text_anotacoes.get(1.0, tk.END)
        with open("anotacoes.txt", "w") as arquivo:
            arquivo.write(anotacoes)

    def carregar_anotacoes():
        try:
            with open("anotacoes.txt", "r") as arquivo:
                conteudo = arquivo.read()
                text_anotacoes.delete(1.0, tk.END)  # Limpa o conteúdo atual
                text_anotacoes.insert(tk.END, conteudo)  # Preenche o widget com o conteúdo do arquivo
        except FileNotFoundError:
            # Tratamento para o caso em que o arquivo ainda não existe
            pass
    
    text_anotacoes = tk.Text(lf_diario, width=55, wrap="word")
    text_anotacoes.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(lf_diario, command=text_anotacoes.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    text_anotacoes.configure(yscrollcommand=scrollbar.set)

    button_salvar = tk.Button(lf_diario, text="Salvar Anotações", command=salvar_anotacoes)
    button_salvar.pack()
    

BANCO()
MAIN_ADM()
janela.mainloop()
