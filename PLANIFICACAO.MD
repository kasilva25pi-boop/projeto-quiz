# 🤓 PROJETO QUIZ 🤓

### Participantes: Rodrigo, kayque, luis(talvez)





### 1) Como vão representar: as perguntas em memória (lista de dicionários?)
> um dicionario dentro de uma lista 
````python
Pergutas = [

    {
        "id": (identificador da pergunta),
        "Pergunta": (a pergunta que aparece para o usuario no terminal),
        "opcoes": [numero de opções em formato de lista em que cada indice é uma das opções de resposta]
        "Dificuldade" = (varia entre facil, medio e dificil dependendo da dificuldade se ganha mais pontos),
        "correta": (indice da lista "opcoes")





    }, 

    {

         "id": "Pergunta_1",
        "Pergunta": "Qual a cor do ceú?",
        "opcoes": ["Azul", "Verde", "Amarelo", "Rosa"]
        "Dificuldade" = "Facil",
        "correta": 0






    }







]

````

#### 1.2. A pontuação (inteiro? dicionário com certas/erradas?)
> vai ser um valor inteiro baseado na dificuldade da 
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
o usuario escreve o nome dele(a)| o programa grava o nome do jogador em um `ficheiro.json` com um dicionario com o nome do jogador e o registra os pontos a partir dele | no terminal sera mostrado o menu |
o modo de jogo se quer continuar ou sair do jogo |sera responsavel por verificar se a resposta do jogador corresponde com a resposta correta e os inputs em geral  | as perguntas na qual o usuario tera de ler e responder     |
Usuario escreve as respostas que achar certo | o Processamento carrega as funções chama variaveis    | mostra as opções e tambem se o jogador acertou ou não




### 3) Lista de funções (com responsabilidades)


- `carregar_perguntas(ficheiro_com_perguntas)` — lê JSON carrega as perguntas no programa principal
- `mostrar_menu(ficheiro_com_ menu)` — imprime opções e devolve escolha válida
- `fazer_pergunta(ficheiro_carregado)` — roda lista com as perguntas, pede resposta
- `guardar_pontuacao(pontos)` — escreve no ficheiro de pontuações, e o nome do ultilizador
- `verifica_respo(lista)` — compara se a resposta do usuario com a resposta da pergunta
- `dar_pontos(pontos_pergunta)` — pontos que são dados ao player se ele acertar a questão baseado na dificuldade da questão e depois guardados na função de guardar pontos

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

> Usaremos o `Raise` para pegarmos erros especificos como por exemplo o jogador não escrever nada na resposta

> usaremos o `Keyerror` se percorremos algum dicionario e alguma chave que tentarmos aceder não exista

>  usaremos um `ImportError` caso o usuario exclua uma das funções de algum ficheiro que tentarmos exportar

> se o ultilizador excluir um `ficheiros.json` usaremos um `FileNotFoundError`

> Quando o ultilizador introduz o seu nome e usar caracteres invalidos ultilizaremos o `TypeError`

> Se tentarmos aceder a uma variavel que o ultilizador excluiu acidentalmente ou que não exista por algum motivo, ultilizaremos um `NameError`




