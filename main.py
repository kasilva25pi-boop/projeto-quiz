
import json
import random
nome = input("digite seu nome: ")

pontos = 0 

from logica import guardar_info, carregar_perguntas, mostrar_regras, mostrar_info, dar_pontos, responder
from menu import mostrar_menu

#TESTE debug de guardar pontuação
#testanto_pontuação = int(input("Escreva um numero pra pontuação: "))
 
perguntas_carregadas = carregar_perguntas("perguntas.json")


while True:
    escolhi = mostrar_menu()
    
    lista_aleatoria = []
    x = 0
    while x < 15:
        pergunta_random = random.choice(perguntas_carregadas)
        if pergunta_random in lista_aleatoria:
            continue
        else:
            lista_aleatoria.append(pergunta_random)
            x += 1
    if escolhi == "1":
        pontos = 0
        guardar_info(nome, pontos, "pontuacao.json") 
        input(f"VAMOS JOGAR {nome}!!!!!")
        print("\n")

        

        for dic in lista_aleatoria:
            
            print(dic['id'])
            print(dic['Pergunta'])
            print(f"Dificuldade: {dic['Dificuldade']}", "\n")
            for i in dic['opcoes']:
                print(i)
            print("----------------------------------------")
            try:
                pontos_ganhos = responder(dic)
                pontos = pontos + pontos_ganhos
                guardar_info(nome, pontos, "pontuacao.json")

            except ValueError:
                input("Voce digitou algo alem de um numero então não ganhou nenhum ponto")
                print("\n")
                continue

            
            
                

        

    elif escolhi == "2":
        print(f"Então vamos pra pontuação {nome}")
        print("\n")
        mostrar_info("pontuacao.json")
    
    elif escolhi == "3":
        print(f"Então vamos para as regras, {nome}")
        
    
    elif escolhi == "4":
        print(f"OK Adeus {nome}")
        break
    else:
        input("O que voce escreveu não corresponde com nenhuma das opções da aplicação, tente novamente")
        
        
