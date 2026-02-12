import json

def carregar_perguntas(ficheiro_com_perguntas):
    try:
        with open(ficheiro_com_perguntas, "r", encoding="utf-8") as f:
            return json.load(f)

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
            json.dump(lista_carregada, f)

    except (FileNotFoundError, json.JSONDecodeError):
        print("Houve um erro no ficheiro")


guardar_info("teste", 25, "pontuacao.json")