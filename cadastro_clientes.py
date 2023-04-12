from modulos import *
from validEntry import Validadores
from reports import Relatorios
from funcionalidades import Funcs

janela = tix.Tk()

class Application(Funcs, Relatorios, Validadores):
    def __init__(self):
        self.janela = janela
        self.validaEntradas()
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.lista_frame2()
        self.montaTabelas()
        self.select_lista()
        self.menus()
        janela.mainloop() #Final do class Sempre!
    def tela(self):
        self.janela.title("Cadastro de Clientes")
        self.janela.configure(background="#1e3743")
        self.janela.geometry("700x500")
        self.janela.resizable(True, True)
        self.janela.minsize(width=100, height=100)
        self.janela.maxsize(width=900, height=700)
    def frames_da_tela(self):
        self.frame_1 = Frame(self.janela, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=6) #highlightbackground = cor da borda do frame, highlightthickness cor da borda do frame
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)#aumento e posições de elementos proporcionais, posicioes de 0 a 1. ex: x=0.30 = 30%, y=0.35 = 35%

        self.frame_2 = Frame(self.janela, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=6)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)
    def widgets_frame1(self):

        self.abas = ttk.Notebook(self.frame_1)

        self.aba1 = Frame(self.abas)
        self.aba2 = Frame(self.abas)

        self.aba1.configure(background="#dfe3ee")
        self.aba2.configure(background="lightgray")

        self.abas.add(self.aba1, text="Aba 1")
        self.abas.add(self.aba2, text="Aba 2")

        self.abas.place(relx=0, rely=0, relheight=0.98, relwidth=0.98)

        self.bt_limpar = Button(self.aba1, text="Limpar", bd = 2, bg = '#107db2', fg = 'white', font=('verdana',8, 'bold'), command=self.limpar_tela)
        self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)
        texto_Ballonlimpar = "Limpará, todos registros que digitou e não estão registrados ainda"
        self.balao_limpar = tix.Balloon(self.aba1)
        self.balao_limpar.bind_widget(self.bt_limpar, balloonmsg= texto_Ballonlimpar)

        self.bt_buscar = Button(self.aba1, text="Buscar", bd = 2, bg = '#107db2', fg = 'white', font=('verdana',8, 'bold'), command=self.busca_cliente)
        self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)
        texto_BallonBuscar = "Digite no campo 'nome' o cliente que deseja pesquisar!"
        self.balao_buscar = tix.Balloon(self.aba1)
        self.balao_buscar.bind_widget(self.bt_buscar, balloonmsg = texto_BallonBuscar)


        self.bt_novo = Button(self.aba1, text="Novo", bd = 2, bg = '#107db2', fg = 'white', font=('verdana',8, 'bold' ), command= self.add_clientes)
        self.bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)
        texto_BallonNovo = "Confirma em sistema o registro!"
        self.balao_novo = tix.Balloon(self.aba1)
        self.balao_novo.bind_widget(self.bt_novo, balloonmsg = texto_BallonNovo)

        self.bt_alterar = Button(self.aba1, text="Alterar",bd = 2, bg = '#107db2', fg = 'white', font=('verdana',8, 'bold' ), command=self.altera_cliente)
        self.bt_alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)
        texto_BallonAlterar = "Alterar o registro do sistema!"
        self.balao_alterar = tix.Balloon(self.aba1)
        self.balao_alterar.bind_widget(self.bt_alterar, balloonmsg = texto_BallonAlterar)

        self.bt_apagar = Button(self.aba1, text="Apagar", bd = 2, bg = '#107db2', fg = 'white', font=('verdana',8, 'bold' ), command=self.deleta_cliente)
        self.bt_apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)
        texto_BallonApagar = "Apaga o registro em Sistema. Somente Após Selecionar, clicando duas vezes!"
        self.balao_apagar = tix.Balloon(self.aba1)
        self.balao_apagar.bind_widget(self.bt_apagar, balloonmsg = texto_BallonApagar)

 #codigo
        self.lb_codigo = Label(self.aba1, text="Código", bg='#dfe3ee', fg='#187db2')
        self.lb_codigo.place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.15)

        self.codigo_entry = Entry(self.aba1, validate="key", validatecommand=self.vcmd2)
        self.codigo_entry.place(relx=0.05, rely=0.2, relwidth=0.1)

#nome
        self.lb_nome = Label(self.aba1, text="Nome", bg='#dfe3ee', fg='#187db2')
        self.lb_nome.place(relx=0.05, rely=0.35, relwidth=0.1, relheight=0.15)

        self.nome_entry = Entry(self.aba1)
        self.nome_entry.place(relx=0.05, rely=0.50, relwidth=0.8)

#telefone
        self.lb_telefone = Label(self.aba1, text="Telefone", bg='#dfe3ee', fg='#187db2')
        self.lb_telefone.place(relx=0.05, rely=0.6)

        self.telefone_entry = Entry(self.aba1)
        self.telefone_entry.place(relx=0.05, rely=0.7, relwidth=0.4)
#cidade
        self.lb_cidade = Label(self.aba1, text="Cidade", bg='#dfe3ee', fg='#187db2')
        self.lb_cidade.place(relx=0.5, rely=0.6)

        self.cidade_entry = Entry(self.aba1)
        self.cidade_entry.place(relx=0.5, rely=0.7, relwidth=0.4)


        self.Tipvar = StringVar()
        self.TipV = ("Solteiro(a)", "Casado(a)", "Divorciado(a)", "Viuvo(a)", "Fudido(a)" )
        self.Tipvar.set("Solteiro(a)")

        self.popupMenu = OptionMenu(self.aba2, self.Tipvar, *self.TipV)
        self.popupMenu.place(relx=0.1, rely=0.1, relwidth=0.2, relheight=0.2)

        self.estado_civil = self.Tipvar.get()
        print(self.estado_civil)

        #calendario
        self.bt_calendario = Button(self.aba2, text="Data", command=self.calendario)
        self.bt_calendario.place(relx=0.5, rely=0.02)
        self.entry_data = Entry(self.aba2, width=10)
        self.entry_data.place(relx=0.5, rely=0.2)


    def lista_frame2(self):
        self.listaCli = ttk.Treeview(self.frame_2, height= 3, columns=("col1", "col2", "col3", "col4"))
        self.listaCli.heading("#0", text="")
        self.listaCli.heading("#1", text="Codigo")
        self.listaCli.heading("#2", text="Nome")
        self.listaCli.heading("#3", text="Telefone")
        self.listaCli.heading("#4", text="Cidade")

        self.listaCli.column("#0", width=1)
        self.listaCli.column("#1", width=50)
        self.listaCli.column("#2", width=200)
        self.listaCli.column("#3", width=125)
        self.listaCli.column("#4", width=125)

        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.scroolLista = Scrollbar(self.frame_2, orient="vertical")
        self.listaCli.configure(yscrollcommand=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)
        self.listaCli.bind("<Double-1>", self.OnDoubleClick)
    def menus(self):
        menubar = Menu(self.janela) #definimos menubar como um Menu() children de self.janela que é a master
        self.janela.config(menu = menubar) #menu() herda menubar

        filemenu = Menu(menubar, tearoff=0)#ambos estão herdando menubar
        filemenu2 = Menu(menubar, tearoff=0) #ambos estão herdando menubar
        def Quit():
            self.janela.destroy()

        menubar.add_cascade(label="Opções", menu = filemenu)
        menubar.add_cascade(label="Relatorios", menu=filemenu2)


        filemenu.add_command(label="Sair", command=Quit)
        filemenu.add_command(label="Janela 2", command=self.janela2)
        filemenu2.add_command(label="Limpar", command=self.limpar_tela)
        filemenu2.add_command(label = "Ficha do Cliente", command=self.geraRelatCliente)
    def janela2(self):
        self.janela2 = Toplevel()
        self.janela2.title("Cadastro de Clientes")
        self.janela2.configure(background="#1e3743")
        self.janela2.geometry("400x200+200+220")
        self.janela2.resizable(False, False)
        self.janela2.transient(self.janela)
        self.janela2.focus_force()
        self.janela2.grab_set()
    def validaEntradas(self):
        self.vcmd2 = (self.janela.register(self.validate_entry2), "%P")



Application()