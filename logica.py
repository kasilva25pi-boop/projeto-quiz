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


def mostrar_info(ficheiro_json):
    maior = 0
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
    
    if maior == 0:
        print("A maior pontuação é zero, ou ninguem jogou ainda ou todo mundo é burro")
    
    else:
        
        print(f"A pessoa(s) com maior pontos é(são) {nome_maior} com: {maior} pontos")

    input("Aperte Enter para voltar para o Menu: ")
    print("\n")




def mostrar_regras():

    print("REGRAS: ")
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
            return -1

        elif dicionario['Dificuldade'] == "Medio":
            input(f"❌❌❌❌voce errou perdeu 2 pontos, aperte enter pra continuar.....❌❌❌❌")
            return -2
        elif dicionario['Dificuldade']:
            input(f"❌❌❌❌voce errou perdeu 3 pontos, aperte enter pra continuar.....❌❌❌❌")
            return -3
            
    print("\n")

