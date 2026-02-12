
import json
nome = input("digite seu nome: ")


from logica import guardar_info, carregar_perguntas, mostrar_regras
from menu import mostrar_menu

#TESTE debug
testanto_pontuação = int(input("Escreva um numero pra pontuação: "))
guardar_info(nome, testanto_pontuação, "pontuacao.json")  

while True:
    escolhi = mostrar_menu()

    if escolhi == "1":
        
        print(f"VAMOS JOGAR {nome}")
    elif escolhi == "2":
        print(f"Então vamos pra pontuação {nome}")
        
    
    elif escolhi == "3":
        print(f"Então vamos para as regras, {nome}")
    
    elif escolhi == "4":
        print(f"OK Adeus {nome}")
        break
    else:
        input("O que voce escreveu não corresponde com nenhuma das opções da aplicação, tente novamente")
        
        
