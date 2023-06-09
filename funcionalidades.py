from modulos import *

class Funcs():
    def limpar_tela(self):
        self.codigo_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.telefone_entry.delete(0, END)
        self.cidade_entry.delete(0, END)
        self.cpf_entry.delete(0, END)
        self.idade_entry.delete(0, END)
    def conecta_bd(self):
        self.conn = sqlite3.connect("clientes.bd")
        self.cursor = self.conn.cursor() ; print("Conectando ao Banco de Dados!")
    def desconecta_bd(self):
        self.conn.close() ; print("Desconectando Banco")
    def montaTabelas(self):
        self.conecta_bd()
        ##Tabela
        self.cursor.execute("CREATE TABLE IF NOT EXISTS clientes (cod INTEGER PRIMARY KEY, nome_cliente CHAR(40) NOT NULL, telefone INTEGER(20), cidade CHAR(40), cpf INTEGER(20), idade INTEGER(10));")
        self.conn.commit() ; print("Banco de dados criado")
        self.desconecta_bd()
    def variaves(self):
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.telefone = self.telefone_entry.get()
        self.cidade = self.cidade_entry.get()
        self.cpf = self.cpf_entry.get()
        self.idade = self.idade_entry.get()
    def add_clientes(self):
        self.variaves()
        if self.nome_entry.get() == "":
            msg = "Você precisa digitar um Nome!!!"
            messagebox.showerror("Campo NOME em Branco!!!", msg)
        else:
            self.conecta_bd()
            self.cursor.execute(" INSERT INTO clientes (nome_cliente, telefone, cidade, cpf, idade ) VALUES (?, ?, ?, ?, ?)", (self.nome, self.telefone, self.cidade, self.cpf, self.idade))
            self.conn.commit()
            self.desconecta_bd()
            self.select_lista()
            self.limpar_tela()
    def select_lista(self):
        self.listaCli.delete(*self.listaCli.get_children())
        self.conecta_bd()
        lista = self.cursor.execute("SELECT cod, nome_cliente, telefone, cidade, cpf, idade FROM clientes ORDER BY nome_cliente ASC;")
        for row in lista:
            self.listaCli.insert("", END, values=row)
        self.desconecta_bd()
    def OnDoubleClick(self, event):
        self.limpar_tela()
        self.listaCli.selection()

        for i in self.listaCli.selection():
            col1, col2, col3, col4, col5, col6 = self.listaCli.item(i, 'values')
            self.codigo_entry.insert(END, col1)
            self.nome_entry.insert(END, col2)
            self.telefone_entry.insert(END, col3)
            self.cidade_entry.insert(END, col4)
            self.cpf_entry.insert(END, col5)
            self.idade_entry.insert(END, col6)
    def deleta_cliente(self):
        self.variaves()
        self.conecta_bd()
        self.cursor.execute("DELETE FROM clientes WHERE cod = ?", (self.codigo))
        self.conn.commit()
        self.desconecta_bd()
        self.limpar_tela()
        self.select_lista()

    def altera_cliente(self):
        self.variaves()
        self.conecta_bd()

        self.cursor.execute("UPDATE clientes SET nome_cliente = ?, telefone = ?, cidade = ?, cpf = ?, idade = ?, WHERE cod = ?", (self.nome, self.telefone, self.cidade, self.cpf, self.idade, self.codigo))
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpar_tela()
    def busca_cliente(self):
        self.conecta_bd()
        self.listaCli.delete(*self.listaCli.get_children())

        self.nome_entry.insert(END, "%")
        nome = self.nome_entry.get()

        self.cursor.execute("SELECT cod, nome_cliente, telefone, cidade, cpf, idade FROM clientes WHERE nome_cliente LIKE '%s' ORDER BY nome_cliente ASC" % nome)
        buscanomeCli = self.cursor.fetchall()
        for i in buscanomeCli:
            self.listaCli.insert("", END, values= i)

        self.limpar_tela()
        self.desconecta_bd()
