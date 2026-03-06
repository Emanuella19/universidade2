from PySide6.QtWidgets import (
    QApplication,
    QVBoxLayout,
    QWidget,
    QPushButton,
    QGraphicsDropShadowEffect
)

from PySide6.QtGui import QColor

from screen.cadastrar import Cadastrar
from screen.listar import Listar

import sys


class App:
    def __init__(self):
        self.app = QApplication(sys.argv)

        self.janela = QWidget()
        self.layout = QVBoxLayout()

        self.janela.setWindowTitle("Sistema Universidade")
        self.janela.resize(400, 200)
        self.janela.setLayout(self.layout)

        self.aplicar_estilo()

        self.criar_botoes()

        self.janela.show()

    def aplicar_estilo(self):
        self.janela.setStyleSheet("""
            QWidget {
                background-color: #c7d2fe;
                color: #1f1f1f;
                font-size: 16px;
            }

            QPushButton {
                background-color: #a855f7;
                border: none;
                padding: 12px;
                border-radius: 10px;
                font-weight: bold;
                color: white;
            }

            QPushButton:hover {
                background-color: #9333ea;
            }

            QPushButton:pressed {
                background-color: #7e22ce;
            }
        """)

    def criar_sombra(self, botao):
        sombra = QGraphicsDropShadowEffect()
        sombra.setBlurRadius(20)
        sombra.setXOffset(0)
        sombra.setYOffset(5)
        sombra.setColor(QColor(0, 0, 0, 120))
        botao.setGraphicsEffect(sombra)

    def criar_botoes(self):
        botao_listar = QPushButton("Listar")
        self.criar_sombra(botao_listar)
        self.layout.addWidget(botao_listar)
        botao_listar.clicked.connect(self.abrir_listagem)

        botao_cadastrar = QPushButton("Cadastrar")
        self.criar_sombra(botao_cadastrar)
        self.layout.addWidget(botao_cadastrar)
        botao_cadastrar.clicked.connect(self.abrir_cadastro)

    def abrir_listagem(self):
        self.tela_listagem = Listar(self.app)
        self.tela_listagem.janela.show()

    def abrir_cadastro(self):
        self.tela_cadastro = Cadastrar(self.app)
        self.tela_cadastro.janela.show()


if __name__ == "__main__":
    system = App()
    sys.exit(system.app.exec())