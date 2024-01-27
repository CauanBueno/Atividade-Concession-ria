############################################################# Função cadastro de Carros
carros = []
def cadastrarCarro():
    try:
        carro = {
            "codigoCarro": 0,
            "marca": "",
            "modelo": "",
            "ano": "",
            "quantidade": "",
            "valor": "",
        }
        carro["codigoCarro"] = len(carros) + 1
        carro["marca"] = input("Digite marca do carro: ")
        carro["modelo"] = input("Digite modelo do carro: ")
        carro["ano"] = int(input("Digite ano do carro(yyyy): "))
        carro["quantidade"] = int(input("Quantidade comprada: "))
        carro["valor"] = int(input("Valor R$: "))
        carros.append(carro)
        print("")
        print("                      Carro cadastrado com sucesso!!!")
        print("")
        input ("Clique qualquer tecla para retornar ao menu inicial")
        print("")
    except:
        print("")
        print("ERRO AO EFETUAR O CADASTRO!")
        print("")
        print("")
        input ("Clique qualquer tecla para retornar ao menu inicial")
        print("")

clientes = []
def cadastrarCliente():
    try:
        cliente = {
            "codigo": 0,
            "nomeCliente": "",
            "dataNascimento": "",
            "documento": "",
        }
        cliente["codigoCliente"] = len(clientes) + 1
        cliente["nomeCliente"] = input("Digite nome completo do cliente: ")
        cliente["dataNascimento"] = input("Digite a data de nascimento do cliente: ")
        cliente["documento"] = int(input("Digite um documento do cliente: "))
        clientes.append(cliente)
        print("")
        print("                      Cliente cadastrado com sucesso!!!")
        print("")
    except:
        print("")
        print("ERRO AO CADASTRAR O CLIENTE!")
    print("")
    input ("Clique qualquer tecla para retornar ao menu inicial")
    print("")
    
###################################################################### Novas vendas
vendas = []

def realizadorVenda():
    try:
    ##################################################################  sistema de escolha de compra     
        for cliente in clientes:
            print(f'{cliente["codigoCliente"]}, {cliente["nomeCliente"]}')
        
        print("")
        codigoCliente = int(input("Digite o código do cliente que realizará a compra: "))
        print("")
        
        if codigoCliente <= len(clientes): 
            cliente = list(filter(lambda c: c["codigoCliente"] == codigoCliente, clientes))[0]
            print("")
            
            for carro in carros:
                print(f'{carro["codigoCarro"]} - {carro["marca"] }, {carro["modelo"]}, Estoque = {carro["quantidade"]}')
                
            print("")
            codigoCarro = int(input("Digite o código do carro a ser comprado: "))
            print("")
            
            if codigoCarro <= len(carros):
                carro = list(filter(lambda c: c["codigoCarro"] == codigoCarro, carros))[0]
                print("")
    ##########################################################################################  finalizaçao de compra 
                opcao = int(input("Deseja confirmar a compra? (1 = SIM | 2 = Não) - "))
                print("")
    ######################################################################################### sistema de controle de estoque e criaçao de lista de vendas 
                if opcao == 1:
                    if carro["quantidade"] > 0:
                        carro["quantidade"] -= 1
                        venda = {
                            "cliente": cliente["nomeCliente"],
                            "carro": carro["marca"],
                            "valor": carro["valor"]
                        }
                        vendas.append(venda)
                        print("")
                        print("Venda cadastrada com sucesso!")
                        print("")
                        input ("Clique qualquer tecla para retornar ao menu inicial")
                        print("")
                    else:
                        print("")
                        print("Estoque do carro esgotado.")
                        print("")
                        input ("Clique qualquer tecla para retornar ao menu inicial")
                        print("")
                elif opcao == 2:
                    print("")
                    print("Venda cancelada.")
                    print("")
                    input ("Clique qualquer tecla para retornar ao menu inicial")
                    print("")
                else:
                    print("")
                    print("Opção inválida.")
                    print("")
                    input ("Clique qualquer tecla para retornar ao menu inicial")
                    print("")
            else:
                print("")
                print("Opção inválida.")
                print("")
                input ("Clique qualquer tecla para retornar ao menu inicial")
                print("")
        else:
            print("")
            print("Opção inválida.")
            print("")
            input ("Clique qualquer tecla para retornar ao menu inicial")
            print("")
    ################################################################################ compra finalizada 
    ############################################################################## sistema de soma   
    except:
        print("")
        print("ERRO AO CADASTRAR A VENDA!")
        print("")
        print("")
        input ("Clique qualquer tecla para retornar ao menu inicial")
        print("")

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
                print("")
                print("")
                print("")
                input ("Clique qualquer tecla para retornar ao menu inicial")
                print("")
    except:
        print("")
        print ("OPÇÃO INVÁLIDA!")
        print("")
        print("")
        input ("Clique qualquer tecla para retornar ao menu inicial")
        print("")

def alterarCarros():
    try:
        
        for carro in carros:
            print(f'{carro["codigoCarro"]}; {carro["marca"]}')
        print("")
        print("") 
        codigo = int(input("Digite o código do carro a ser alterao: "))
        print ("")
        print ("")
        
        if codigo <= len(carros):
            
            carro = list(filter(lambda c: c["codigoCarro"] == codigo, carros))[0]
            
            if carro:
                carros.remove(carro)
                carro["codigoCarro"] = len(carros)
                carro["marca"] = input("Digite marca do carro: ")
                carro["modelo"] = input("Digite modelo do carro: ")
                carro["ano"] = int(input("Digite ano do carro(yyyy): "))
                carro["quantidade"] = int(input("Quantidade comprada: "))
                carro["valor"] = (input ("Valor R$: "))
                
                carros.append(carro)
                print("")
                print("                      Cadastro alterado com sucesso!!!")
                print("")
                print("")
                input ("Clique qualquer tecla para retornar ao menu inicial")
                print("")
        else:
            print("")
            print("Código inválido!")
            print("")
            print("")
            input ("Clique qualquer tecla para retornar ao menu inicial")
            print("")
    
    except:
        print("")
        print("Erro ao alterar os dados!")
        print("")
        print("")
        input ("Clique qualquer tecla para retornar ao menu inicial")
        print("")

def alterarClientes():
    try:
        for cliente in clientes:
            print(f'{cliente["codigoCliente"]}; {cliente["nomeCliente"]}')
        print ("")
        print ("")
        codigo = int(input("Digite o código do cliente a ser alterao: "))
        print ("")
        print ("")
        
        if codigo <= len(clientes): 
            
            cliente = list(filter(lambda c: c["codigoCliente"] == codigo, clientes))[0]
            
            if cliente:
                clientes.remove(cliente)
                cliente["codigo"] = len(clientes)
                cliente["nomeCliente"] = input("Digite nome completo do cliente: ")
                cliente["dataNascimento"] = input("Digite a data de nascimento do cliente: ")
                cliente["documento"] = int(input("Digite um documento do cliente: "))
                
                clientes.append(cliente)
                print("")
                print("                      Cadastro alterado com sucesso!!!")
                print("")
                print("")
                input ("Clique qualquer tecla para retornar ao menu inicial")
                print("")
        else:
            print("")
            print("Código inválido!")
            print("")
            print("")
            input ("Clique qualquer tecla para retornar ao menu inicial")
            print("")
    
    except:
        print("")
        print("Erro ao alterar os dados!")
        print("")
        print("")
        input ("Clique qualquer tecla para retornar ao menu inicial")
        print("")

def visualizarVendas():
    soma = 0
    for venda in vendas:
        print(venda)
            
        soma = soma + venda["valor"]
    
    
    print("")    
    print("O valor total de vendas foi de R$ ",soma)
        
    print("")
    input ("Clique qualquer tecla para retornar ao menu inicial")
    print("")

def visualizarCarros():
    for carro in carros:
        print(carro)
        
    print("")
    input ("Clique qualquer tecla para retornar ao menu inicial")
    print("")

def estoqueCarros():
    print("")
    print("")
    
    for quantidade in carros:
        if estoqueCarros <= len(carros):
            quantidade = list(filter(lambda e: ["Quantidade"] == quantidade, carros))
    
    print("")
    input ("Clique qualquer tecla para retornar ao menu inicial")
    print("")
        ### isso é so um demonstrativo de fazer a leitura da qunatidade, necessita da conexão, para que a subtração de estoque funcione 

###################################################################### Menu
def iniciar():
    print ("======================================================")
    print ("======== Concessionária Tavares ==========")
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
                realizadorVenda()
            case 4:
                opcaoAlterarDados()
            case 5:
                visualizarVendas()
            case 6: 
                visualizarCarros()
                
            case 7:
                print("")
                print ("Saindo...")
                print ("")
                sair = True
            case _:
                print("")
                print ("OPÇÃO INVÁLIDA!")
                print("")
                print("")
                input ("Clique qualquer tecla para retornar ao menu inicial")
                print("")
    except:
        print("")
        print ("OPÇÃO INVÁLIDA!")
        print("")
        print("")
        input ("Clique qualquer tecla para retornar ao menu inicial")
        print("")
    return sair

while iniciar() == False:
    print ("")
    print ("")
    print ("=================== Retornando ao menu... ===================")
    print ("")
    print ("")
