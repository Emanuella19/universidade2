from modules.aluno import Aluno 
from modules.mysql import MySQL

banco = MySQL()

banco.connect()

aluno = Aluno(
    "Joao Enzo",
    "Joaoirmao@gmail.com",
    "98745612345",
    "031944445555",
    "Rua Paineira, Eldorado, 1200"
)
query = aluno.cadastrar()
print (query)

banco.execute_query(query)

banco.disconnect()
