from menu import initial_menu, determinante_1x1_menu, determinante_2x2_menu, determinante_3x3_menu
def logic():
    while True:
        initial_menu()
        initial_user_select = int(input("Digite sua escolha: "))
        match initial_user_select:
            case 0:
                print("Encerrando o programa.")
                break
            case 1:
                determinante_1x1_menu()
            case 2:
                determinante_2x2_menu()
            case 3:
                determinante_3x3_menu()
            case _:
                print("Opção inválida. Tente novamente.")

            
if __name__ == "__main__":
    logic()


