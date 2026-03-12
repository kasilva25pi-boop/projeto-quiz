# MANUAL TECNICO

## Lista de ficheiros

### Ficheiros Py 

`main.py`: onde o jogo é executado e as funções são importadas, além de ser onde o ultilizador registra o nome

`menu.py`: onde é guardado as funções que mostram o menu no terminal e devolvem a escolha da onde o ultilizador deseja ir na aplicação 

`logica.py`: onde possui a maioria das funções do programa, de fazer perguntas, responder, carregar as respostas e etc. 

### Ficheiros json

`perguntas.json`: onde as perguntas do quiz do modo classico estão, elas são exportadas para o `main.py` e separadas aleatoriamente

`perguntas_bomba.json`: igual o `perguntas.json` pórem guarda as perguntas do modo bomba, o diferencial é que cada pergunta tem uma bomba guardada em uma opção errada 

`verdadeiro_falso.json`: tambem igual as anteriores, porem as opções são apenas entre verdadeiro e falso 

`pontuacao.json`: onde a pontuação e nome do jogador são guardados, apenas se aplica ao modo classico.

`pontuacao_bomba.json`: tambem onde as informações do player são guardadas pórem se no quiz o jogador achar uma bomba ele não é registrado nesse ficheiro.


`pontuacao_verdadeiro_falso.json`: tambem onde as informações do player são guardadas, pórem, os pontos podem ser negativos já que uma pergunta errada no quiz de verdadeiro e falso anula uma certa

### Ficheiros Md
`PLANIFICACAO.md`: onde fizemos a planificação do projeto quais funções iriamos usar e etc

`PASSOSDOPROJETO.md`: onde tem a atividade passada no github

`README.md`: Explica o que é esse projeto


# Lista De Funções

### Main.py:
O main não possui Funções

### Logica.py: 

`carregar_perguntas(ficheiro_com_perguntas)`: Carrega as perguntas de acordo com o ficheiro designado, no programa depende de qual modo o jogador escolheu pra jogar.

`guarda_info(nome, pontos, ficheiro)`: Guarda a informação do jogador, nome os pontos que fez no quiz e no ficheiro do modo que o jogador estiver jogando

`mostra_info(ficheiro_json)`: mostra a informação para o jogador do nome e pontuação alem de mostrar a pessoa com mais pontos se tiver, dependendo do modo de jogo o ficheiro muda

`mostra_regras()`: mostra as regras pra jogar o jogo e como cada modo funciona

`dar_pontos(dificuldade)`: devolve a quantidade de pontos de acordo com o a dificuldade da questão, e depois é somada com os pontos, obviamente se o jogar errar a função não é chamada, lembrando que essa função não é usada diretamente no programa e sim chamada em outr função

`responder(dicionario, tem_bomba)`: função que é chamada pro usuario responder a pergunta, ela é chamada toda volta que o programa dá ao precorrer a lista de perguntas, ela é responsavel por pegar a resposta da pergunta feito pro usuario e verificar se est correta, se estiver correta ela chama a função `dar_pontos(dificuldade)` e retorna o quanto o usuario ganhou, se não estiver correta retorna o ganho que é igual a zero, vale mencionar que essa função tambem verifica se o modo que o jogador esta jogando é o modo bomba se for a diferença é que ele verifica quando o usuario erra se o que ele escolheu tinha uma bomba dentro, se nao tiver o quiz continua, se tiver o o quiz encerra e o usuario volta pro menu

`verdade_falso(dicionario)`: parecida com a anterior, pórem, o diferencial é que se o usuario errar ele perde pontos de acordo com a dificuldade da pergunta


### Menu.py:

`mostrar_menu`: Mostra o menu principal do jogo onde possui as pontuações, jogar, regras ou sair(o que encerra o programa), pergunta o que o usuario quer fazer e devolve a escolha dele, dependendo o que o usario no `main.py`o programa verifica e executa uma determinada ação de acordo 

`mostrar_jogos`: Se o usario escolher jogar no menu principal, o jogo mostra o menu de jogos, lá ele pode escolher qual modo de jogo ele quer jogar, Verdadeiro ou Falso, Modo Classico ou o Modo Bomba(tambem pode apertar em sair pra ele voltar pro menu principal); aqui ele tambem devolve a escolha do usuario

`mostra_pontos`: Bem parecida com a anterior, quando o jogador seleciona ver os pontos no menu, ele é levado a esse menu, aqui ele escolher qual modo de jogo ele quer ver a pontuação: Verdadeiro ou Falso, Modo Classico ou o Modo Bomba tambem pode sair o que leva para o menu principal