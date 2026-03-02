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
            
     

def responder(dicionario):
    
    opcao = input("Digite sua resposta entre A, B, C,  D: ")

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


