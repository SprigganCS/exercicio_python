def deposito(cliente, notas, cn):
    valor = contaValorNotas(notas)

    insereNotasCn(notas, cn) #adiciona as notas no caixa


    cliente_index = findCliente(cliente)

    if(cliente_index == -1): #se nao tiver cliente deve criar, se não é só adicionar o valor
        clientes.append(cliente)
        saldos.append(valor)
    else:
        saldos[cliente_index] += valor #aqui é garantido que sempre vai ter um index válido

def transferencia(cliente, valor, cliente_credito):
    print("transferencia")
    #deverá transferir o valor do cliente para o cliente_credito
    # os saldos dos clientes serão atualizados, mas a quantidade de notas no caixa não
    saldo_cliente = saldos[findCliente(cliente)]
    if saldo_cliente < valor:
        print("Saldo insuficiente para realizar a transferência.")
        return
    
    saldos[findCliente(cliente)] -= valor
    saldos[findCliente(cliente_credito)] += valor

def saque(cliente, valor, cn):   
    index_cliente = findCliente(cliente)

    if index_cliente == -1:
        print("Cliente não encontrado!") #pode ser que os testes já garantam isso, mas só pra garantir eu coloquei
        return
    
    saldo_cliente = saldos[index_cliente]

    if saldo_cliente < valor:
        print("Saldo insuficiente para realizar o saque.") #tbm pode ser que já seja garantido
        return

    
    valores_notas = [100, 50, 20, 10, 5, 2, 1]
    qtd_min_notas = [0, 0, 0, 0, 0, 0, 0] 
    notas_cn = matriz_notas[cn]
    
    #boa sorte implementando isso aqui

    valores_notas = [100, 50, 20, 10, 5, 2, 1]
    qtd_min_notas = [0, 0, 0, 0, 0, 0, 0]

    for i in range(len(valores_notas)): #eu testaria bem toda essa lógica aqui
        if valor >= valores_notas[i] and notas_cn[i] > 0:
            qtd_min_notas[i] = valor // valores_notas[i]
            qtd_min_notas[i] = min(qtd_min_notas[i], notas_cn[i])
            valor -= qtd_min_notas[i] * valores_notas[i]
            notas_cn[i] -= qtd_min_notas[i]

    if valor == 0:
        print("A quantidade disponível de notas é:", notas_cn)
        print("A quantidade mínima de notas é:", qtd_min_notas)
        saldos[index_cliente] -= contaValorNotas(qtd_min_notas)
    else:
        print("Não há notas suficientes para o valor solicitado.")


    #atualizar saldo do cliente e qtd de notas do caixa
    #Caso não haja notas suficientes, o saque não será realizado.

def findCliente(cliente):
    print("findCliente")
    #retorna o indice do cliente na lista clientes
    index_cliente = -1
    for i in range(len(clientes)):
        if clientes[i] == cliente:
            index_cliente = i
            break
    return index_cliente
    #se nao existir retorna -1

def contaValorNotas(notas):
    valor = 0
    valor += int(notas[0]) * 100
    valor += int(notas[1]) * 50
    valor += int(notas[2]) * 20
    valor += int(notas[3]) * 10
    valor += int(notas[4]) * 5
    valor += int(notas[5]) * 2
    valor += int(notas[6]) * 1
    return valor

def insereNotasCn(notas, cn):
    for i in range(len(notas)):
        matriz_notas[cn][i] += notas[i]

def relatorios():
    print("Dados dos clientes:")
    for i in range(len(clientes)):
        print(f"{clientes[i]}: {saldos[i]}")

    print()

    print("Relatório de caixas:")
    print("caixa: n100 n50 n20 n10 n5 n2 n1")
    for i in range(len(matriz_notas)):
        print(f"{i+1}: {matriz_notas[i][0]} {matriz_notas[i][1]} {matriz_notas[i][2]} {matriz_notas[i][3]} {matriz_notas[i][4]} {matriz_notas[i][5]} {matriz_notas[i][6]}")

    print()





num_caixas = int(input("Digite a quantidade de caixas eletrônicos: "))

matriz_notas = []
clientes = []
saldos = []

for i in range(num_caixas):
    notas_caixa = []
    notas_input = input(f"Digite as quantidades de notas para o caixa {i + 1} (separadas por espaço): ").split() #notas de 100, 50, 20, 10, 5, 2, 1

    for nota in notas_input:
        notas_caixa.append(int(nota))

    matriz_notas.append(notas_caixa)


while True:
    operacao = int(input("Digite a operação desejada: (1 - Depósito, 2 - Saque, 3 - Transferência): "))
    if operacao == 0:
        relatorios()
        break

    elif operacao == 1:
        cn = int(input("Digite o número do caixa: "))
        nome_cliente = input("Digite o nome do cliente: ")
        notas = input("Digite a quantidade de notas para o depósito: ").split()

        notas = [int(nota) for nota in notas] #aqui to transformando a lista de strings em uma lista de inteiros

        deposito(nome_cliente, notas, cn-1) #tirei 1 pq parece que as saídas não consideram o caixa 0

    elif operacao == 2:
        cn = int(input("Digite o número do caixa: "))
        nome_cliente = input("Digite o nome do cliente: ")
        valor = int(input("Digite o valor do saque: "))
        saque(nome_cliente, valor, cn-1)

    elif operacao == 3:
        cn = int(input("Digite o número do caixa: ")) #sla pq mas o enunciado pede o número do caixa
        nome_cliente = input("Digite o nome do cliente: ")
        valor = int(input("Digite o valor da transferência: "))
        nome_cliente_credito = input("Digite o nome do cliente que receberá a transferência: ")
        transferencia(nome_cliente, valor, nome_cliente_credito)

    else:
        print("Operação inválida!")