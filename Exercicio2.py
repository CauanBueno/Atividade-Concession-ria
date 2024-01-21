
###################################################################### Dados Clientes(novas vendas)
vendas = []
def cadastrarVenda():
    try:
        clientes = {
            "Código": 0,
            "Nome cliente": "",
            "Veículo": "",
            "Ano veículo": "",
            "Valor compra": "",
        }
        clientes["Código"] = len(vendas) + 1
        clientes["Nome cliente"] = input("Digite nome completo do cliente: ")
        clientes["Veículo"] = input("Digite marca do veículo adquirido: ")
        clientes["Ano veículo"] = int(input("Digite ano do veículo(yyyy): "))
        clientes["Valor compra"] = int(input("Valor total compra R$: "))
        vendas.append(clientes)
        print("")
        print("                      Venda cadastrada com sucesso!!!")
    except:
        print("")
        print("ERRO AO CADASTRAR A VENDA!")
def visualizarVendas():
    for cliente in vendas:
        print(cliente)
#        fazer soma das vendas
    print("")
    input ("Clique qualquer tecla para retornar ao menu inicial")
    print("")
### def alterarClientes():
    ...

############################################################# Dodos dos Carros
carros = []
def cadastrarCarro():
    try:
        carro = {
            "Código Carro": 0,
            "Marca": "",
            "Ano": "",
            "Quantidade": "",
            "Valor R$": "",
        }
        carro["Código Carro"] = len(carros) + 1
        carro["Marca"] = input("Digite marca do carro: ")
        carro["Ano"] = int(input("Digite ano do carro(yyyy): "))
        carro["Quantidade"] = int(input("Quantidade comprada: "))
        carro["Valor R$"] = (input ("Valor R$: "))
        carros.append(carro)
        print("")
        print("                      Carro cadastrado com sucesso!!!")
    except:
        print("")
        print("ERRO AO EFETUAR O CADASTRO!")
def visualizarCarros():
    for carro in carros:
        print(carro)
        
    input ("Clique qualquer tecla para retornar ao menu inicial")
    print("")
def alterarCarros():
    ...

###################################################################### Opções de Alteração de dados
def opcaoAlterarDados():
    print ("(1) Alterar as informações dos carros")
    print ("(2) Alterar os dados dos clientes")
    print("")
    try:
        opcao1 = int(input("Quais dados deseja alterar (1 ou 2)?: "))
        match opcao1:
            case 1:
                alterarCarros()
            case 2:
                alterarClientes()
            case _:
                print("")
                print ("OPÇÃO INVÁLIDA!")
    except:
        print("")
        print ("OPÇÃO INVÁLIDA!")

def iniciar():
    print ("======================================================")
    print ("======== Sistema de Compra e Venda - Carros ==========")
    print ("======================================================")
    print ("")
    print ("(1) Inserir nova compra de carro")
    print ("(2) Inserir uma nova venda")
    print ("(3) Alterar dados já inseridos")
    print ("(4) Visualizar vendas efetuadas")
    print ("(5) Visualizar estoque de carros")
    print ("(6) Sair")
    print ("")
    
    sair = False
    try:
        opcao = int(input("Selecione opção desejada (x): "))
        print("")
        
        match opcao:
            case 1:
                cadastrarCarro()
            case 2:
                cadastrarVenda()
            case 3:
                opcaoAlterarDados()
            case 4:
                visualizarVendas()
            case 5:
                visualizarCarros()
            case 6:
                print ("Saindo...")
                print ("")
                sair = True
            case _:
                print("")
                print ("OPÇÃO INVÁLIDA!")
    except:
        print("")
        print ("OPÇÃO INVÁLIDA!")
    return sair

while iniciar() == False:
    print ("")
    print ("")
    print ("=================== Reiniciando... ===================")
