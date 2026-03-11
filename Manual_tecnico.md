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


