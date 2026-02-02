# PROJETO QUIZ

### Participantes: Rodrigo, kayque, luis(talvez)




### 1. Como vão representar: as perguntas em memória (lista de dicionários?)
> um dicionario dentro de uma lista 

#### 1.2. A pontuação (inteiro? dicionário com certas/erradas?)
> vai ser um valor inteiro
#### 1.3. as pontuações guardadas (lista de dicionários em pontuacoes.json?)
> dicionario com o nome e a pontuação que a pessoa fez
````python
Pontos = {
    "Nome_exemplo": 35

}

````


### 2) Entradas / Processamento / Saídas

##### Uma tabela ou lista com:
#### 2.1 entradas (o que o utilizador escreve / o que vem do JSON)

> o usuario escreve o nome o modo de jogo e o numero das respostas que achar certo

#### 2.2 processamento (o que o programa calcula/decide)
> o programa grava o nome do jogador em um `ficheiro.json` com um dicionario com o nome do jogar e o registra os pontos a partir dele, ele tambem sera responsavel por verificar se a resposta do jogador corresponde com o que o jogador inserir na resposta

#### 2.3 saídas (o que mostra no terminal / o que guarda em ficheiro)
> no terminal sera mostrado o menu, as perguntas assim como as opções e tambem se o jogador acertou ou não


| entradas | Processamento | Saída |
|------------|-------------|-------|
o usuario escreve o nome o modo de jogo e o numero das respostas que achar certo| o programa grava o nome do jogador em um `ficheiro.json` com um dicionario com o nome do jogar e o registra os pontos a partir dele, ele tambem sera responsavel por verificar se a resposta do jogador corresponde com o que o jogador inserir na resposta| no terminal sera mostrado o menu, as perguntas assim como as opções e tambem se o jogador acertou ou não|----------|-----------|---------|




