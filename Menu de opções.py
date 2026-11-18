while True:
    print("\n--- MENU DE OPÇÕES ---")
    print("1. Mostrar uma mensagem de Bom dia")
    print("2. Mostrar um cálculo")
    print("3. Sair")
    
    opcao = input("Escolha uma opção (1-3): ")

    if opcao == "1":
        print("\nOlá! Tenha um Bom Dia.")
    elif opcao == "2":
        resultado = 6 * 4
        print(f"\nCálculo executado: 6 x 4 = {resultado}")
    elif opcao == "3":
        print("\nSaindo do programa... Até logo!")
        break
    else:
        print("\nOpção inválida! Por favor, escolha 1, 2 ou 3.")
