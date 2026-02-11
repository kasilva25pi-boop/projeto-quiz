
nome = input("digite seu nome: ")



from menu import mostrar_menu
while True:
    escolhi = mostrar_menu()

    if escolhi == "1":
        
        print(f"VAMOS JOGAR {nome}")
    elif escolhi == "2":
        print(f"Então vamos pra pontuação {nome}")
    
    elif escolhi == "3":
        print(f"OK Adeus {nome}")
        break
    else:
        input("O que voce escreveu não corresponde com nenhuma das opções da aplicação, tente novamente")
        
        

          