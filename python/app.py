from modules.mysql import MySQL
from modules.aluno import Aluno
 
import sys
 
from PySide6.QtWidgets import(
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton
)
class TelaCadastro():
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.janela = QWidget()
        self.layout = QVBoxLayout()
        
        self.labels = []
        self.campos = []
        
        self.janela.setWindowTitle("Cadastro Aluno")
        self.janela.resize(1200, 600)
        
    def criar_componentes(self):
        self.labels.append(QLabel("Digite um nome:"))
        self.labels.append(QLabel("Digite um email:"))
        self.labels.append(QLabel("Digite um cpf:"))
        self.labels.append(QLabel("Digite um telefone:"))
        self.labels.append(QLabel("Digite um endereço:"))
          
        for label in self.labels:
            self.layout.addWidget(label)
            
            campo = QLineEdit()
            self.campos.append(campo)
            self.layout.addWidget(campo)
            
        botao_Cadastro = QPushButton("Cadastrar")
        self.layout.addWidget(botao_Cadastro)
        
        self.janela.setLayout(self.layout)
        botao_Cadastro.clicked.connect(self.cadastrar)
            
             

    def cadastrar():
        aluno = Aluno(
            campo_nome.text(),
            campo_email.text(),
            campo_cpf.text(),
            campo_telefone.text(),
            campo_endereco.text()
        )
    
        banco = MySQL()
        banco.connect()
    
        aluno.cadastrar(banco)
    
        banco.disconnect()
 
#app = QApplication(sys.argv)
 
#janela = QWidget()
#janela.setWindowTitle("Cadastro Aluno")
#janela.resize(1200, 600)
 
#layout = QVBoxLayout()
 
#Componentes
label_nome = QLabel("Digite seu nome: ")
campo_nome = QLineEdit()
 
label_email = QLabel("Digite seu email: ")
campo_email = QLineEdit()
 
label_cpf = QLabel("Digite seu cpf: ")
campo_cpf = QLineEdit()
 
label_telefone = QLabel("Digite seu telefone: ")
campo_telefone = QLineEdit()
 
label_enedereco = QLabel("Digite seu endereço: ")
campo_endereco = QLineEdit()
 
botao = QPushButton("Cadastrar")
 
#Adicionar componentes a janela
 
janela.setLayout(layout)
 
botao.clicked.connect(cadastro)
janela.show()
sys.exit(app.exec())
 