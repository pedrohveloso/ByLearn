class Aluno(object):
    status = False
    
    def __init__(self, nome):
        self.nome = nome
    
    def notas(self, nota1, nota2):
        self.nota1 = nota1
        self.nota2 = nota2
        
    def calcular_media(self):
        return (self.nota1 + self.nota2) / 2
    
    def mostrar_inf(self):
        status = (self.calcular_media() >= 6)
        if status:
            print(f"O aluno {self.nome} foi aprovado!")
        else:
            print(f"O aluno {self.nome} reprovou...")
