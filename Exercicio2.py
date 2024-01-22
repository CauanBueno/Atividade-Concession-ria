clientes = []
def cadastrarCliente():
    try:
        cliente = {
            "Código cliente": 0,
            "Nome cliente": "",
            "Data de nascimento": "",
            "Documento": "",
        }
        cliente["Código"] = len(clientes) + 1
        cliente["Nome cliente"] = input("Digite nome completo do cliente: ")
        cliente["Data de nascimento"] = input("Digite a data de nascimento do cliente ")
        cliente["Documento"] = int(input("Digite um documento do cliente: "))
        clientes.append(cliente)
        print("")
        print("                      Cliente cadastrado com sucesso!!!")
    except:
        print("")
        print("ERRO AO CADASTRAR A CLIENTE!")
    print("")
    input ("Clique qualquer tecla para retornar ao menu inicial")
    print("")



###################################################################### Dados Clientes(novas vendas) NESCESSÁRIO ALTERAÇÃO
vendas = []
def cadastrarVenda():
    try:
        
        cliente = {
            "Código cliente": 0,
            "Nome cliente": "",
            "Veículo": "",
            "Ano veículo": "",
            "Valor compra": "",
        }
        cliente["Código"] = len(vendas) + 1
        cliente["Nome cliente"] = input("Digite nome completo do cliente: ")
        cliente["Veículo"] = input("Digite marca do veículo adquirido: ")
        cliente["Ano veículo"] = int(input("Digite ano do veículo(yyyy): "))
        cliente["Valor compra"] = int(input("Valor total compra R$: "))
        vendas.append(cliente)
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


def alterarClientes():
    try:
        
        for cliente in clientes:
            print(f'{cliente["Código cliente"]}; {cliente["Nome cliente"]}')
            
        codigo = int(input("Digite o código do cliente a ser alterao: "))
        
        if codigo <= len(clientes): 
            
            cliente = list(filter(lambda c: c["Código cliente"] == codigo, clientes))[0]

            if cliente:
                clientes.remove(cliente)
                
                cliente["Código"] = len(clientes) + 1
                cliente["Nome cliente"] = input("Digite nome completo do cliente: ")
                cliente["Data de nascimento"] = input("Digite a data de nascimento do cliente ")
                cliente["Documento"] = int(input("Digite um documento do cliente: "))
                
                carros.append(cliente)
                
        else:
            print("Código inválido!")
    
    except:
        print("Erro ao alterar os dados!")

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
    try:
        
        for carro in carros:
            print(f'{carro["Código Carro"]}; {carro["Marca"]}')
            
        codigo = int(input("Digite o código do carro a ser alterao: "))
        
        if codigo <= len(carros):
            
            carro = list(filter(lambda c: c["Código Carro"] == codigo, carros))[0]

            if carro:
                carros.remove(carro)
                
                carro["Marca"] = input("Digite marca do carro: ")
                carro["Ano"] = int(input("Digite ano do carro(yyyy): "))
                carro["Quantidade"] = int(input("Quantidade comprada: "))
                carro["Valor R$"] = (input ("Valor R$: "))
                
                carros.append(carro)
                
        else:
            print("Código inválido!")
    
    except:
        print("Erro ao alterar os dados!")

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
    print ("(1) Inserir um novo carro")
    print ("(2) Inserir um novo cliente")
    print ("(3) Inserir uma nova venda")
    print ("(4) Alterar dados já inseridos")
    print ("(5) Visualizar vendas efetuadas")
    print ("(6) Visualizar estoque de carros")
    print ("(7) Sair")
    print ("")
    
    sair = False
    try:
        opcao = int(input("Selecione opção desejada (x): "))
        print("")
        
        match opcao:
            case 1:
                cadastrarCarro()
            case 2:
                cadastrarCliente()
            case 3:
                cadastrarVenda()
            case 4:
                opcaoAlterarDados()
            case 5:
                visualizarVendas()
            case 6:
                visualizarCarros()
            case 7:
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
