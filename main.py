
import json
import random
nome = input("digite seu nome: ")

pontos = 0 

from logica import guardar_info, carregar_perguntas, mostrar_regras, mostrar_info, dar_pontos, responder
from menu import mostrar_menu

#TESTE debug de guardar pontuação
#testanto_pontuação = int(input("Escreva um numero pra pontuação: "))
guardar_info(nome, pontos, "pontuacao.json")  
perguntas_carregadas = carregar_perguntas("perguntas.json")
lista_aleatoria = []
x = 0
while x < 15:
    pergunta_random = random.choice(perguntas_carregadas)
    if pergunta_random in lista_aleatoria:
        continue
    else:
        lista_aleatoria.append(pergunta_random)
        x += 1

print(len(lista_aleatoria))

while True:
    escolhi = mostrar_menu()

    if escolhi == "1":
        
        input(f"VAMOS JOGAR {nome}!!!!!")
        print("\n")

        

        for dic in lista_aleatoria:
            
            print(dic['id'])
            print(dic['Pergunta'])
            print(f"Dificuldade: {dic['Dificuldade']}", "\n")
            for i in dic['opcoes']:
                print(i)
            try:
                pontos_ganhos = responder(dic)
                pontos = pontos + pontos_ganhos
                guardar_info(nome, pontos, "pontuacao.json")

            except ValueError:
                input("Voce digitou algo alem de um numero então não ganhou nenhum ponto")
                continue

            
            
                

        

    elif escolhi == "2":
        print(f"Então vamos pra pontuação {nome}")
        mostrar_info("pontuacao.json")
    
    elif escolhi == "3":
        print(f"Então vamos para as regras, {nome}")
        
    
    elif escolhi == "4":
        print(f"OK Adeus {nome}")
        break
    else:
        input("O que voce escreveu não corresponde com nenhuma das opções da aplicação, tente novamente")
        
        
