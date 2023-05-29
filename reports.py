from modulos import *

class Relatorios():
    def printCliente(self):
        caminho_pdf = os.path.abspath("cliente.pdf")
        caminho_pdf = "file://" + caminho_pdf.replace("\\", "/")
        webbrowser.open(caminho_pdf)
    def geraRelatCliente(self):
        self.c = canvas.Canvas("cliente.pdf")

        self.codigoRel = self.codigo_entry.get()
        self.nomeRel = self.nome_entry.get()
        self.telefoneRel = self.telefone_entry.get()
        self.cidadeRel = self.cidade_entry.get()
        self.cpfRel = self.cpf_entry.get()
        self.idadeRel = self.idade_entry.get()

        self.c.setFont("Helvetica-Bold", 24)
        self.c.drawString(200, 790, 'Ficha do Cliente')

        self.c.setFont("Helvetica-Bold", 18)
        self.c.drawString(50,700, 'Codigo: ')
        self.c.drawString(50,670, 'Nome: ')
        self.c.drawString(50,635, 'Telefone: ')
        self.c.drawString(50,600, 'Cidade: ')
        self.c.drawString(50,575, 'CPF: ')
        self.c.drawString(50,545, 'Idade: ')

        self.c.setFont("Helvetica", 18)
        self.c.drawString(150, 700, self.codigoRel)
        self.c.drawString(150, 670, self.nomeRel)
        self.c.drawString(150, 635, self.telefoneRel)
        self.c.drawString(150, 600, self.cidadeRel)
        self.c.drawString(150, 575, self.cpfRel)
        self.c.drawString(150, 545, self.idadeRel)

        self.c.rect(20,250,550,500, fill=False, stroke=True)


        self.c.showPage()
        self.c.save()
        self.printCliente()