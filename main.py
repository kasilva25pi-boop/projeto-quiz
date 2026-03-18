
import json
import random
nome = input("Olá, para começar, Escreva o seu nome: ")
print("\n")
while True:
    if not nome.strip():
        nome = input("esse nome é invalido digite novamente: ")
        print("\n")
    else:
        break

pontos = 0 

from logica import guardar_info, carregar_perguntas, mostrar_regras, mostrar_info, dar_pontos, responder, verdade_falso
from menu import mostrar_menu, mostrar_jogos, mostrar_pontos

#TESTE debug de guardar pontuação
#testanto_pontuação = int(input("Escreva um numero pra pontuação: "))
 



while True:
    escolhi = mostrar_menu()
    #gerando a lista aleatoria 
    
    #Ultilizador escolheu jogar        
    if escolhi == "1":
        #mostra o menu dos jogos 
        while True:
            escolhi_jogo = mostrar_jogos()
            #escolheu Jogar o modo classico de perguntas de conhecimento geral
                 
            if escolhi_jogo == "1":
                try: 
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
                    if len(lista_aleatoria) < 15:
                        print("a lista tem que ter no minimo 15 perguntas")
                        break
                    pontos = 0
                    guardar_info(nome, pontos, "pontuacao.json") 
                    input(f"VAMOS JOGAR {nome}!!!!!")
                    print("\n")
                except FileNotFoundError:
                    input("Não achamos esse ficheiro com perguntas")
                    break
                except json.JSONDecodeError:
                    input("Tivemos um problema ao tentar abrir o ficheiro")
                    break

                    

                for dic in lista_aleatoria:
                        
                    print(dic['id'])
                    print(dic['Pergunta'])
                    print(f"Dificuldade: {dic['Dificuldade']}", "\n")
                    for i in dic['opcoes']:
                        print(i)
                    print("----------------------------------------")
                    try:
                        pontos_ganhos = responder(dic, False)
                        pontos = pontos + pontos_ganhos
                        try:
                            guardar_info(nome, pontos, "pontuacao.json")
                        except json.JSONDecodeError:
                            print("Erro ao abrir o ficheiro de pontos")
                            break

                    except ValueError:
                        input("Voce digitou algo alem das opções então não ganhou nenhum ponto")
                        print("\n")
                        continue
                  
                input(f"🎉🎉 FIM DO QUIZ 🎉🎉")
                input(f"parabens {nome} Voce fez {pontos} pontos")
                    
            #Jogador quer Jogar Verdadeiro ou Falso
            elif escolhi_jogo == "2":
                try:
                    perguntas_carregadas = carregar_perguntas("verdadeiro_falso.json")
                    lista_aleatoria = []
                    x = 0
                    while x < 15:
                        pergunta_random = random.choice(perguntas_carregadas)
                        if pergunta_random in lista_aleatoria:
                            continue
                        else:
                            lista_aleatoria.append(pergunta_random)
                            x += 1
                    pontos = 0
                    guardar_info(nome, pontos, "pontuacao_verdadeiro_falso.json") 
                    input(f"VAMOS JOGAR Verdadeiro ou falso {nome}!!!!!")
                    print("\n")
                except FileNotFoundError:
                    input("Não achamos esse ficheiro com perguntas")
                    break
                except json.JSONDecodeError:
                    input("tivemos um problema ao abrir as perguntas")
                    break

                    

                for dic in lista_aleatoria:
                        
                    print(dic['id'])
                    print(dic['Pergunta'])
                    print(f"Dificuldade: {dic['Dificuldade']}", "\n")
                    print("Verdadeiro ou Falso?")
                    print("----------------------------------------")
                    try:
                        pontos_ganhos = verdade_falso(dic)
                        pontos = pontos + pontos_ganhos
                        try:
                            guardar_info(nome, pontos, "pontuacao_verdadeiro_falso.json")
                        except json.JSONDecodeError:
                            print("Ocorreu um erro ao abrir o ficheiro JSON dos pontos")
                            break

                    except ValueError:
                        input("Voce digitou algo alem das opções então não ganhou nenhum ponto")
                        print("\n")
                        continue
            
                        
                input("🎉🎉 FIM DO QUIZ 🎉🎉")
                input(f"parabens {nome} Voce fez {pontos} pontos")
            #Usuario quer Jogar pergunta BOMBA
            elif escolhi_jogo == "3":
                try:
                    perguntas_carregadas = carregar_perguntas("perguntas_bomba.json")
                except FileNotFoundError:
                    input("Não achamos esse ficheiro com perguntas")
                    break
                except json.JSONDecodeError:
                    input("Tivemos problema ao abrir as perguntas")
                    break
                lista_aleatoria = []
                x = 0
                while x < 15:
                    pergunta_random = random.choice(perguntas_carregadas)
                    if pergunta_random in lista_aleatoria:
                        continue
                    else:
                        lista_aleatoria.append(pergunta_random)
                        x += 1
                pontos = 0
                try:
                    guardar_info(nome, pontos, "pontuacao_bomba.json") 
                    input(f"VAMOS JOGAR Pergunta BOMBA {nome}🤪🤪!!!!!")
                    print("\n")
                except json.JSONDecodeError:
                    input("Não foi possivel guardar a informação do usuario")
                    break
            
            

                
                #Mostrando as perguntas de bomba
                for dic in lista_aleatoria:
                        
                    print(dic['id'])
                    print(dic['Pergunta'])
                    print(f"Dificuldade: {dic['Dificuldade']}", "\n")
                    for i in dic['opcoes']:
                        print(i)
                    print("----------------------------------------")
                    try:
                        pontos_ganhos = responder(dic, True)
                        if pontos_ganhos == "bomba":
                            break
                        else:
                            try:
                                pontos = pontos + pontos_ganhos
                                guardar_info(nome, pontos, "pontuacao_bomba.json")
                            except json.JSONDecodeError:
                                print("Não foi possivel abrir o Ficheiro de pontos")
                                break

                    except ValueError:
                        input("Voce digitou algo alem das opções então não ganhou nenhum ponto")
                        print("\n")
                        continue
                
                input("🎉🎉 FIM DO QUIZ 🎉🎉")
                input(f"parabens {nome} Voce fez {pontos} pontos")
                
            elif escolhi_jogo == "4":
                print(f"Ok {nome} Voltando pro Menu principal")
                break    
            else:
                input("O que voce escreveu não corresponde com nenhuma das opções da aplicação, tente novamente")
                print("\n")
        
    #Jogador escolher ir ver pontuação
    elif escolhi == "2":
        try:

            print(f"Então vamos pra pontuação {nome}")
            print("\n")
            while True:
                escolhi_pontos = mostrar_pontos()
                
                if escolhi_pontos == "1":
                
                    mostrar_info("pontuacao.json")
                    
                elif escolhi_pontos == "2":
                    mostrar_info("pontuacao_verdadeiro_falso.json")
                elif escolhi_pontos == "3":
                    mostrar_info("pontuacao_bomba.json")
                elif escolhi_pontos == "4":
                    print(f"Beleza meu nobre {nome} bora pro menu")
                    print("\n")
                    break
                else:
                    input("O que voce escreveu não corresponde com nenhuma das opções da aplicação, tente novamente")
                    print("\n")
        except json.JSONDecodeError:
            input("houve um erro ao tentar abrir os pontos")
            
        except:
            input("Há um problema no ficheiros dos pontos")

        
        
    #Jogador quer ver as regras
    elif escolhi == "3":
        print(f"Então vamos para as regras, {nome}")
        mostrar_regras()
        print("\n")

        
    #Jogador quer encerrar o jogo
    elif escolhi == "4":
        print(f"OK Adeus {nome}")
        break
    else:
        input("O que voce escreveu não corresponde com nenhuma das opções da aplicação, tente novamente")
        print("\n")
        
        
