# Declaração da Classe
class Gafanhoto:
    def __init__(self): # Método construtor
    # Atributos de Instância
        self.nome = ""
        self.idade = 0

    # Métodos de Instância
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."

# Declaração de Objetos
g1 = Gafanhoto() # Instanciando o objeto g1 da classe Gafanhoto
g1.nome = "João"
g1.idade = 20
print(g1.mensagem())
g1.aniversario()
print(g1.mensagem())

g2 = Gafanhoto() # Instanciando o objeto g2 da classe Gafanhoto
g2.nome = "Maria"
g2.idade = 25
print(g2.mensagem())

g3 = Gafanhoto() # Instanciando o objeto g3 da classe Gafanhoto
print(g3.mensagem())