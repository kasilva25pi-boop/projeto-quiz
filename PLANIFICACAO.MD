# 🤓 PROJETO QUIZ 🤓

### Participantes: Rodrigo, kayque, luis(talvez)




### 1) Como vão representar: as perguntas em memória (lista de dicionários?)
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


| entradas | Processamento | Saída |
|------------|-------------|-------|
o usuario escreve o nome o modo de jogo e o numero das respostas que achar certo| o programa grava o nome do jogador em um `ficheiro.json` com um dicionario com o nome do jogar e o registra os pontos a partir dele, ele tambem sera responsavel por verificar se a resposta do jogador corresponde com o que o jogador inserir na resposta| no terminal sera mostrado o menu, as perguntas assim como as opções e tambem se o jogador acertou ou não|----------|-----------|---------|




### 3) Lista de funções (com responsabilidades)


- `carregar_perguntas(ficheiro_com_perguntas)` — lê JSON carrega as perguntas no programa principal
- `mostrar_menu(ficheiro_com_ menu)` — imprime opções e devolve escolha válida
- `fazer_pergunta(ficheiro_carregado)` — roda lista com as perguntas, pede resposta, devolve se acertou
- `guardar_pontuacao(pontos)` — escreve no ficheiro de pontuações














#### 5) Estrutura de ficheiros / módulos (decidida por vocês)

> vamos possuir o `main.py` onde o jogo acontece

>tambem terremos o `menu.py` onde rodara a função do menu

> terremos o `logica.py` onde teremos a função onde ele faz a pergunta 

