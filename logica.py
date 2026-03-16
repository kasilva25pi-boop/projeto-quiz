import json

def carregar_perguntas(ficheiro_com_perguntas):
    try:
        with open(ficheiro_com_perguntas, "r", encoding="utf-8") as f:
            lista_perguntas = json.load(f)
            return lista_perguntas

    except (FileNotFoundError, json.JSONDecodeError):
        print("Houve um erro no ficheiro")
        return []


def guardar_info(nome, pontos, ficheiro):

    with open(ficheiro, "r", encoding="utf-8") as f:
        lista_carregada = json.load(f)

    informacao = {

        nome : pontos
    }

    lista_carregada[nome] = pontos
    try:
        with open(ficheiro, "w", encoding="utf-8") as f:
            json.dump(lista_carregada, f, ensure_ascii=False, indent=4)

    except (FileNotFoundError, json.JSONDecodeError):
        print("Houve um erro no ficheiro")
        return []


def mostrar_info(ficheiro_json):
    maior = -100
    nome_maior = []
    with open(ficheiro_json, "r", encoding="utf-8") as f:
        pontuacao = json.load(f)
    for nome, pontos in pontuacao.items():
        print(f"{nome}: {pontos}")
        print("--------------")
        if pontos >= maior:
            maior = pontos 
            
    for nome, pontos in pontuacao.items():

        if pontuacao[nome] == maior:
            nome_maior.append(nome)
    if len(nome_maior) == 0:
        print("não tem nada registrado ainda")
        print("\n")
    else:
        print(f"A pessoa(s) com maior pontos é(são):")
        print("\n")
        for i in nome_maior:
            print(i)
            print("- - - - - - - - - - - - - - - - - -")
        print("\n")
        print(f"com {maior} pontos")


    input("Aperte Enter para voltar para o Menu: ")
    print("\n")




def mostrar_regras():

    print("\n")
    print("REGRAS: ")
    print("---------------------------------------------------------------------------------------------------------------------------")
    print("O programa é bem simplorio, nada muito complicado, como voce conseguiu chegar ate aqui ja deve saber como,")
    print("navegar pelos menus, voce vê o numero da opção que deseja e escolhe ela escrevendo-a no terminal, o programa")
    print("ira pedir o seu nome no começo, é com ele que os pontos serão registrados")
    print("a cada rodada de jogo os pontos registrados no seu nome são RESETADOS, tenha isso em mente")
    print("---------------------------------------------------------------------------------------------------------------------------")
    input("Aperte Enter pra continuar: ")
    print("\n")
    print("1. Jogar:")
    print("---------------------------------------------------------------------------------------------------------------------------")
    print(f"se escrever {"1"} e apertar enter vai para o menu jogar,")
    print("no menu voce tem como escolher entre 3 categorias, ou voltar pro menu principal,")
    print("---------------------------------------------------------------------------------------------------------------------------")
    input("Aperte Enter pra continuar: ")
    print("\n")
    print("1.1 Modo Classico:")
    print("---------------------------------------------------------------------------------------------------------------------------")
    print("nesse modo voce ira receber 15 perguntas por rodada de conhecimento geral que serão aleatorias, nela voce podera escolher,")
    print("entre A, B, C e D(podem ser minusculas), se a resposta estiver correta voce irá receber os pontos de acordo")
    print("com a dificuldade da pergunta, senão acertar, não recebe nada e passa pra proxima pergunta")
    print("lembrado que se o jogador escrever algo além das opção ou não escrever nada, tambem sera considerado como uma resposta incorreta")
    print("no fim do quiz o programa informara quantos pontos voce recebeu de acordo com o nome que voce registrou no inicio")
    print("---------------------------------------------------------------------------------------------------------------------------")
    input("Aperte Enter pra continuar: ")
    print("\n")
    print("1.2 Modo Verdadeiro ou Falso:")
    print("---------------------------------------------------------------------------------------------------------------------------")
    print("O diferencial desse modo é que inves de escolher entre a,b,c e d,")
    print("voce ira escolher entre (V e F)  V de verdadeiro e F de falso")
    print("Alem disso cada pergunta errada resultara na perda de pontos de acordo com a dificuldade da questão então cuidado!! ")
    print("---------------------------------------------------------------------------------------------------------------------------")
    input("Aperte Enter pra continuar: ")
    print("\n")
    print("1.3 Pergunta Bomba:")
    print("---------------------------------------------------------------------------------------------------------------------------")
    print("Nesse modo o tipo de jogativa é parecida com a classica a difereça é que uma das perguntas erradas é uma bomba ")
    print("Voce pode ate errar mas se a questão que voce errou tiver uma bomba dentro o quiz acaba e voce perde, ou tenha muita sorte ")
    print("ou acerte tudo, para escapar da explosão ")
    print("---------------------------------------------------------------------------------------------------------------------------")
    input("Aperte Enter pra continuar: ")
    print("\n")
    print("2. Pontuação: ")
    print("---------------------------------------------------------------------------------------------------------------------------")
    print("Se digitar 2 Voce é levado ao menu dos pontos os pontos são separados por modos,")
    print("cada modo tem uma lista com a pontuação registrada, antes de mostrar os pontos ")
    print("o programa ira perguntar de qual modo voce quer ver a pontuação, aqui funciona igual o menu anterior digite o que quer ")
    print("e o programa te levara ate lá ")
    print("---------------------------------------------------------------------------------------------------------------------------")
    input("Aperte Enter pra continuar: ")
    print("\n")
    print("3. Regras:")
    print("---------------------------------------------------------------------------------------------------------------------------")
    print("Se digitar 3 o programa Leva as regras, é aonde voce esta agora, ele é responsavel por ")
    print("mostrar como o programa funciona e como as informações são Guardadas")
    print("---------------------------------------------------------------------------------------------------------------------------")
    input("Aperte Enter pra continuar: ")
    print("\n")
    print("4. Sair: ")
    print("---------------------------------------------------------------------------------------------------------------------------")
    print("Se digitar 4 voce encerra o programa lembrando que os pontos continuam registrados junto do nome de quem jogou ")
    print("---------------------------------------------------------------------------------------------------------------------------")
    input("Aperte Enter pra continuar: ")
    print("\n")
    input("Entendeu?, então aperte enter para voltar pro Menu")
    print("\n")




def dar_pontos(dificuldade):
       
            
    if dificuldade == "Dificil":
        return 3
    elif dificuldade == "Facil":
        return 1
    elif dificuldade == "Medio":
        return 2
    else:
        print("não foi encontrada uma dificuldade da pergunta")
        return 0
            
     

def responder(dicionario, tem_bomba):

    bomba = tem_bomba
    if bomba == True:
        opcao = input("Digite sua resposta entre A, B, C ou D: ")

        if opcao in dicionario['correta']:
            ganho = dar_pontos(dicionario['Dificuldade'])
            input("A sua resposta está.......")
            input("Esta.........")
            input("Esta...............")
            input(f"✅✅✅✅ Correta!!!!!!!, por ser uma pergunta {dicionario['Dificuldade']} voce ganhou {ganho} ponto(s) ✅✅✅✅")
            print("\n")
            
            return ganho
        elif opcao in dicionario['Bomba']:
            input("A sua resposta está.......")
            input("Esta.........")
            input("Esta...............")
            input("🎆🎆🎆💣💣💣💣ERRADA E È UMA BOMBA VOCE PERDEU💣💣💣💣🎆🎆🎆")
            
            return "bomba"
            print("\n")

            
        else:
            input("A sua resposta está.......")
            input("Esta.........")
            input("Esta...............")
            input("❌❌❌❌Errada, aperte enter pra continuar.....❌❌❌❌")
            print("\n")
            ganho = 0
            return ganho


    elif bomba == False:

        opcao = input("Digite sua resposta entre A, B, C ou D: ")

        if opcao in dicionario['correta']:
            ganho = dar_pontos(dicionario['Dificuldade'])
            input(f"✅✅✅✅ Voce acertou!!!!!!!, por ser uma pergunta {dicionario['Dificuldade']} voce ganhou {ganho} ponto(s) ✅✅✅✅")
            print("\n")
            
            return ganho
            
        else:
            input("❌❌❌❌voce errou, aperte enter pra continuar.....❌❌❌❌")
            print("\n")
            ganho = 0
            return ganho




def verdade_falso(dicionario):

    opcao = input("Digite V para verdadeiro e F para falso: ")

    if opcao in dicionario['correta']:
        ganho = dar_pontos(dicionario['Dificuldade'])
        input(f"✅✅✅✅ Voce acertou!!!!!!!, por ser uma pergunta {dicionario['Dificuldade']} voce ganhou {ganho} ponto(s) ✅✅✅✅")
        print("\n")
        
        return ganho
        
    else:
        
        if dicionario['Dificuldade'] == "Facil":
            input(f"❌❌❌❌voce errou perdeu 1 ponto, aperte enter pra continuar.....❌❌❌❌")
            print("\n")
            return -1

        elif dicionario['Dificuldade'] == "Medio":
            input(f"❌❌❌❌voce errou perdeu 2 pontos, aperte enter pra continuar.....❌❌❌❌")
            print("\n")
            return -2
        elif dicionario['Dificuldade']:
            input(f"❌❌❌❌voce errou perdeu 3 pontos, aperte enter pra continuar.....❌❌❌❌")
            print("\n")
            return -3
            
    print("\n")

