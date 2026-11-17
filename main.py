# sessão de controle de caminhões


# menu principal da aplicação
def menu():
    while True:
        print("\n===== Controle de Logística Portuária =====")
        print("1 - Controle de Caminhões")
        print("2 - Controle de Contêineres")
        print("3 - Frota de Veículos")
        print("4 - Árvore de Rotas")
        print("5 - Sair")

        try:
            entrada = int(input("Digite uma opção: "))
        except ValueError:
            print("Atenção! Digite apenas números.")
            continue

        if entrada == 1:
            while True:
                print("\n---- Controle de Caminhões ----")
                print("1 - Inserir Caminhões")
                print("2 - Atualizar Lista")
                print("3 - Deletar Caminhões")
                print("4 - Consultar Registros")
                print("5 - Voltar")

                try:
                    escolha = int(input("Digite a opção: "))
                except ValueError:
                    print("Atenção! Digite apenas números.")
                    continue

                if escolha == 5:
                    break
                elif escolha in (1, 2, 3, 4):
                    print("Em Breve")
                else:
                    print("Atenção! Selecione uma opção válida.")

        elif entrada == 2:
            while True:
                print("\n---- Controle de Contêineres ----")
                print("1 - Inserir Contêineres")
                print("2 - Atualizar Lista")
                print("3 - Deletar Contêineres")
                print("4 - Consultar Registros")
                print("5 - Voltar")

                try:
                    escolha = int(input("Digite a opção: "))
                except ValueError:
                    print("Atenção! Digite apenas números.")
                    continue

                if escolha == 5:
                    break
                elif escolha in (1, 2, 3, 4):
                    print("Em Breve")
                else:
                    print("Atenção! Selecione uma opção válida.")

        elif entrada == 3:
            while True:
                print("\n---- Frota de Veículos ----")
                print("1 - Inserir Veículos")
                print("2 - Atualizar Lista")
                print("3 - Deletar Veículos")
                print("4 - Consultar Registros")
                print("5 - Voltar")

                try:
                    escolha = int(input("Digite a opção: "))
                except ValueError:
                    print("Atenção! Digite apenas números.")
                    continue

                if escolha == 5:
                    break
                elif escolha in (1, 2, 3, 4):
                    print("Em Breve")
                else:
                    print("Atenção! Selecione uma opção válida.")

        elif entrada == 4:
            while True:
                print("\n---- Árvore de Rotas ----")
                print("1 - Inserir Rota")
                print("2 - Atualizar Lista")
                print("3 - Deletar Rota")
                print("4 - Consultar Registros")
                print("5 - Voltar")

                try:
                    escolha = int(input("Digite a opção: "))
                except ValueError:
                    print("Atenção! Digite apenas números.")
                    continue

                if escolha == 5:
                    break
                elif escolha in (1, 2, 3, 4):
                    print("Em Breve")
                else:
                    print("Atenção! Selecione uma opção válida.")

        elif entrada == 5:
            print("Saindo do sistema...")
            break

        else:
            print("Atenção! Selecione uma sessão válida.")


menu()
