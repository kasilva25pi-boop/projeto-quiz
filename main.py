
import json
#nome = input("digite seu nome: ")
nome = ""
pontos = 0 

from logica import guardar_info, carregar_perguntas, mostrar_regras, mostrar_info, dar_pontos, responder
from menu import mostrar_menu

#TESTE debug de guardar pontuação
#testanto_pontuação = int(input("Escreva um numero pra pontuação: "))
guardar_info(nome, pontos, "pontuacao.json")  

while True:
    escolhi = mostrar_menu()

    if escolhi == "1":
        
        print(f"VAMOS JOGAR {nome}")

        perguntas_carregadas = carregar_perguntas("perguntas.json")

        for dic in perguntas_carregadas:
            
            print(dic['id'])
            print(dic['Pergunta'])
            for i in dic['opcoes']:
                print(i)
            
            responder(dic)
                

        

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
        
        
