def mostrar_menu():
    

    print("-----------🤓BEM VINDO AO QUIZ MANEIRÃO UHUHUHUHUHUHU🤓---------")
    print("-----------1. Jogar----------------------------------------------")
    print("-----------2. Pontuação------------------------------------------")
    print("-----------3. Sair-----------------------------------------------")
    
    try:
        escolha = int(input("Escreva a opção desejada: "))
      
    except ValueError:
          input("é pra ser um numero, tente de novo")
          mostrar_menu()
    


