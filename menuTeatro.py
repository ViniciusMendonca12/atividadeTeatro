linhas = 300
colunas = 300

matriz = []

for i in range(linhas):
    linha = []
    for j in range(colunas):
        linha.append(0)
    matriz.append(linha)

temTeatro = 0
caixa = 0
secaoUsuario = "ativa"
participantes = 0
totalComprado = 0
totalReservado = 0

while secaoUsuario == "ativa":
  print ("------------------Menu---------------------------")
  print ("[1] - Iniciar o teatro")
  print ("[2] - Reservar lugar")
  print ("[3] - Comprar lugar")
  print ("[4] - Liberar lugar")
  print ("[5] - Listar poltronas")
  print ("[6] - Encerrar o espetáculo")
  print ("[7] - Encerrar Seção")
  print("Valor do caixa :", caixa)

  opcaoMenu = int(input("Selecione a opção desejada: "))

  if opcaoMenu == 7:
    simNao = str(input("Deseja mesmo encerrar a seção? sim... não...."))
    if simNao == "sim":
      secaoUsuario = "desativo"

  if opcaoMenu == 1:
    print ("----------------------Opção - Iniciar o teatro---------------------------")
    print("Selecione a quantidade de fileiras e colunas necessárias para a sessão")
    fileiras = int(input("Selecione a quantidade de fileiras desejadas: "))
    colunas = int(input("Selecione a quantidade de colunas desejadas: "))
    publicoTotal = fileiras * colunas

    if fileiras > 300 or colunas > 300:
      print("Os valores preenchidos excedem nossa capacidade maxima")

    print("----------------Selecione o valor do ingresso-------------------")
    valorIngresso = float(input("Selecione o valor do ingresso para sessão:"))
    print("Valor para sessão confirmado")
    print("De volta ao menu!!!")
    print("Selecione uma nova opção!!!")
    temTeatro = 1


  if opcaoMenu == 2:
    if temTeatro == 0:
      print("Não é possivel reservar um lugar sem uma sessão disponivel")
    else:
      print("----------------------Opção - Reservar Lugar ---------------------------")
      print("O valor do ingresso esta: ", valorIngresso)
      reservarFileira = int(input("Informe qual fileira deseja reservar"))
      reservarColuna = int(input("Informe qual coluna deseja reservar"))

      if matriz[reservarFileira][reservarColuna] == 0:
        matriz[reservarFileira][reservarColuna] = 1
        valorReserva = valorIngresso * 0.30
        print("Assento reservado com sucesso. O valor para reserva é 30% do valor do ingresso, neste caso: ", valorReserva)
        caixa += valorReserva
        totalReservado += 1

      else:
        print("Este assento já esta reservado")

  if opcaoMenu == 3:
      print("----------------------Opção - Comprar Lugar ---------------------------")
      print("O valor do ingresso esta: ", valorIngresso)
      comprarFileira = int(input("Informe qual fileira deseja comprar"))
      comprarColuna = int(input("Informe qual coluna deseja comprar"))
      if matriz[comprarFileira][comprarColuna] == 0:
        print("O valor para comprar o assento é de", valorIngresso)
        print("Comprado com sucesso!!!")
        matriz[comprarFileira][comprarColuna] = 2
        caixa += valorIngresso
        participantes += 1
        totalComprado += 1


      else:
        valorDeCompra = valorIngresso * 0.70
        print("O assento escolhido já esta reservado, você pode comprar-lo por:", valorDeCompra)
        simNaoCompra = str(input("Deseja realmente comprar o lugar reservado? S/N"))
        if simNaoCompra == "S":
          print("Adquirido com sucesso")
          matriz[comprarFileira][comprarColuna] = 2
          caixa += valorDeCompra
          participantes += 1
          totalComprado += 1





  if opcaoMenu == 4:
    print("----------------------Opção - Liberar Lugar---------------------------")
    liberarFileira = int(input("Informe qual fileira deseja liberar"))
    liberarColuna = int(input("Informe qual coluna deseja liberar"))
    if matriz[liberarFileira][liberarColuna] == 0:
      print("Esse lugar já esta liberado")
    elif matriz[liberarFileira][liberarColuna] == 1:
      print("Lugar reservado liberado")
      matriz[liberarFileira][liberarColuna] = 0
      caixa -= valorReserva

    elif matriz[liberarFileira][liberarColuna] == 2:
      print("Lugar comprado liberado")
      matriz[liberarFileira][liberarColuna] = 0
      caixa -= valorIngresso

  if opcaoMenu == 5:
    print("----------------------Opção - Listar Poltronas---------------------------")
    print("Legenda: Número 0 = Liberado")
    print("Legenda: Número 1 = Reservado")
    print("Legenda: Número 2 = Comprado")
    simNaoLista = str((input("Deseja ver a lista? S/N" )))
    if simNaoLista == "S":
      for linha in matriz:
        linha_formatada = ' '.join(map(str, linha))
        print(linha_formatada)


  if opcaoMenu == 6:
    print("----------------------Opção - Encerrar Espetáculo ---------------------------")
    if participantes > publicoTotal * 0.60: 
      print("Espetaculo Finalizado")
      print("Publico Total = ", participantes)
      print("Cadeiras vazias = ", publicoTotal - participantes )
      print("Total de pessoas na reserva = ", totalReservado)
      print("Total de pessoas que compraram ingresso = ", totalComprado)
      print("Total Espetaculo = R$", caixa)
      temTeatro = 0
    

