import json

def carregar_perguntas(ficheiro_com_perguntas):
    try:
        with open(nome_ficheiro, "r", encoding="utf-8") as f:
            return json.load(f)

    except (FileNotFoundError, json.JSONDecodeError):
        print("Houve um erro no ficheiro")
        return []