clientes = []
def cadastrarCliente():
    try:
        cliente = {
            "Código": 0,
            "Nome cliente": "",
            "Data de nascimento": "",
            "Documento": "",
        }
        cliente["Código cliente"] = len(clientes) + 1
        cliente["Nome cliente"] = input("Digite nome completo do cliente: ")
        cliente["Data de nascimento"] = input("Digite a data de nascimento do cliente: ")
        cliente["Documento"] = int(input("Digite um documento do cliente: "))
        clientes.append(cliente)
        print("")
        print("                      Cliente cadastrado com sucesso!!!")
    except:
        print("")
        print("ERRO AO CADASTRAR O CLIENTE!")
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
                cliente["Data de nascimento"] = input("Digite a data de nascimento do cliente: ")
                cliente["Documento"] = int(input("Digite um documento do cliente: "))
                
                clientes.append(cliente)
                print("")
                print("                      Cadastro alterado com sucesso!!!")
        else:
            print("Código inválido!")
    
    except:
        print("Erro ao alterar os dados!")

###################################################################### Novas vendas
vendas = []

def cadastrarVenda():
    try:
        venda = {
            "Código": 0,
            "Nome cliente": "",
            "marca": "",
            "modelo": "",
            "Ano veículo": 0,
            "Valor compra": 0,
        }
        venda["Código"] = len(vendas) + 1
        venda["Nome cliente"] = input("Digite nome completo do cliente: ")
        venda["marca"] = input("Digite marca do veículo adquirido: ")
        venda["modelo"] = input("Digite o modelo do veículo adquirido: ")
        venda["Ano veículo"] = int(input("Digite ano do veículo(yyyy): "))
        venda["Valor compra"] = int(input("Valor total compra R$: "))
        vendas.append(venda)
        
        print("")
        print("                      Venda cadastrada com sucesso!!!")
    
    
        #subtraçao do estoque
        #para funcionar a subtraçao e necessario a confirmaçao de que a venda doi bem sucedida,
        # no caso a venda esta criando outra lista e nao conectando. por isso ela esta criando numeros falso
        #
        #print("")
        #print("")
        
        ###if Quantidade >0
        ###    next
        ###else Quantidade =<0
        ###    print("não foi possivel concretizar a compra")  
        ###if Quantidade >0
        ###    next
        ###else Quantidade =<0
        ###    print("não foi possivel concretizar a compra")    
            
        
        
    except:
        print("")
        print("ERRO AO CADASTRAR A VENDA!")
def visualizarVendas():
    soma = 0
    for venda in vendas:
        print(venda)
            
        soma = soma + venda["Valor compra"]
    
    
    print("")    
    print("O valor total de vendas foi de R$ ",soma)
        
    print("")
    input ("Clique qualquer tecla para retornar ao menu inicial")
    print("")

############################################################# Dados e estoque Carros
carros = []
def cadastrarCarro():
    try:
        carro = {
            "Código Carro": 0,
            "Marca": "",
            "Modelo": "",
            "Ano": "",
            "Quantidade": "",
            "Valor R$": "",
        }
        carro["Código Carro"] = len(carros) + 1
        carro["Marca"] = input("Digite marca do carro: ")
        carro["Modelo"] = input("Digite modelo do carro: ")
        carro["Ano"] = int(input("Digite ano do carro(yyyy): "))
        carro["Quantidade"] = int(input("Quantidade comprada: "))
        carro["Valor R$"] = int(input("Valor R$: "))
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
                carro["Código Carro"] = len(carros) + 1
                carro["Marca"] = input("Digite marca do carro: ")
                carro["Ano"] = int(input("Digite ano do carro(yyyy): "))
                carro["Quantidade"] = int(input("Quantidade comprada: "))
                carro["Valor R$"] = (input ("Valor R$: "))
                
                carros.append(carro)
                print("")
                print("                      Cadastro alterado com sucesso!!!")
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
        
def estoqueCarros():
    print("")
    print("")
    
    for Quantidade in carros:
        if estoqueCarros <= len(carros):
            Quantidade = list(filter(lambda e: ["Quantidade"] == Quantidade, carros))
        ### isso é so um demonstrativo de fazer a leitura da qunatidade, necessita da conexão, para que a subtração de estoque funcione 



###################################################################### Menu
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
