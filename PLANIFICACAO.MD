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

#### 4) Fluxo do programa

Um fluxograma simples (pode ser em texto ou diagrama) ou passos numerados que expliquem:

- Ao iniciar o programa durante o quiz será feita perguntas para o jogador respondê-las, conforme o jogador for acertando as perguntas ele ganhará pontos 
- como o menu liga ao jogo, como o jogo termina, etc.
- A entradas invalidas serão tratadas com tratamento de erros
- como se escolhe jogar outra vez ou sair


#### 5) Estrutura de ficheiros / módulos (decidida por vocês)

> vamos possuir o `main.py` onde o jogo acontece

>tambem terremos o `menu.py` onde rodara a função do menu

> terremos o `logica.py` onde teremos a função onde ele faz a pergunta 


#### 6) Plano de testes (manual)

Criar uma lista de testes do tipo:

> Se escrever ‘a’, ou um numero em vez de uma opção que não exista, o programa não crasha da um `ValueError` e volta a pedir a resposta da pergunta”

>  Se escolher uma opção fora do intervalo, usamos um `Indexerror` e repete o programa


> se o algum dos `ficheiros.json` não existir usaremos um `FileNotFoundError`

> Usaremos o `Raise` para pegarmos erros especificos como por exemplo o jogador não escrever nada



