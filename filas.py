# Usando listas como filas

último = 10
fila = list(range(1, último + 1))
fila2 = list(range(1, último + 1))
while True:
    print(f"\nExistem {len(fila)} clientes na primeira fila")
    print(f"Fila atual: {fila}")
    print(f"\nExistem {len(fila2)} clientes na segunda fila")
    print(f"Fila atual: {fila2}")
    print("Digite F para adicionar um cliente ao fim da  primeira fila,")
    print("ou G para adicionar um cliente ao fim da segunda fila.")
    print("Digite A para atender um cliente da primeira fila,")
    print("ou B para atender um cliente da segunda fila.")
    print("Digite S para sair.")
    operação = input("Operação (F, G, B, A ou S): ")
    x = 0
    sair = False
    while x < len(operação):
        if operação[x] == "A":
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f"Cliente {atendido} atendido")
            else:
                 print("Primeira fila vazia! Ninguém para atender.")
        elif operação[x] == "F":
            último += 1
            fila.append(último)
        elif operação[x] == "B":
            if len(fila2) > 0:
                atendido = fila2.pop(0)
                print(f"Cliente {atendido} atendido")
            else:
                print("Segunda fila vazia! Ninguém para atender.")
        elif operação[x] == "G":
            último += 1
            fila2.append(último)
        elif operação[x] == "S":
            sair = True
            break
        else:
             print("Operação inválida! Digite apenas G, B ou S!")
        x += 1
    if sair:
        break
