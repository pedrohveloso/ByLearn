class Carro(object):
    
    comprado = False
    
    def __init__(self, modelo, ano, estado):
        self.modelo = modelo
        self.ano = ano
        self.estado = estado
        
    def liga_desliga(self, status):
        if status:
            print("Você ligou o carro")
        else:
            print("Você desligou o carro")
   
    def acelerar(self):
        if self.comprado == True:
            print("O carro é seu, então você pode acelerar")
        elif self.comprado == False:
            print("Você precisa comprar o carro para poder acelerar")
    
    def test_drive(self):
        if self.comprado == False:
            print("Você pode realizar um test drive")
            
        else:
            print("Você já é o dono do carro, não há motivos para um Test Drive")
    
    def comprar(self):
        if self.comprado == False:
            adquirir = input("Você deseja comprar este carro?  (S/N)")
            if adquirir == "S":
                self.comprado = True
                print("Parabéns por comprar o carro!")
            elif adquirir == "N":
                self.comprado = False
                print("Talvez na próxima você decida comprar o carro...")
        else:
            print("O carro já é seu, você não pode comprar de novo")
            
    def dirigir(self):
        if self.comprado == True:
            print("O carro é seu, portanto você pode dirigir-lo")
        
        else: 
            print("Você precisa comprar o carro para dirigir")
