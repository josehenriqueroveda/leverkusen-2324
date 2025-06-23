# Analytics da temporada invicta do Bayer Leverkusen na Bundesliga 23/24

Testando algumas análises com dados de futebol, peguei a partida Bayer 04 Leverkusen 5x0 Werder Bremen (da temporada 23/24 invicta do Leverkusen) e decidi explorar os dados da Hudl Statsbomb pra entender um pouco melhor o que aconteceu em campo.
Consegui gerar algumas visualizações:

### ⚽ Heatmap de passes

O Heatmap de Passes mostra:
- A quantidade de passes realizados em diferentes zonas do campo (dividido em quadrantes).
- As cores mais escuras indicam zonas com maior volume de passes.
- Permite visualizar em quais áreas a equipe mais construiu o jogo e onde teve maior presença com a bola.

<br>Muito usado por clubes e analistas para entender:<br>
- As zonas preferenciais de construção de jogo.
- Se o time tem maior volume de jogo em um dos lados do campo.
- Como foi a ocupação territorial durante a partida.

### ⚽ Rede de passes (Passing Network)

O Passing Network mostra:
- Cada jogador é representado por um círculo (posição média em campo). 
- A espessura das linhas entre os jogadores representa o número de passes trocados entre eles. 
- Mostra as conexões e o fluxo de jogo coletivo. 

<br>Muito usado por clubes e analistas para entender:<br>
- Quem é o “hub” do time (quem mais distribui) 
- Quem joga mais próximo de quem 
- Se o time joga mais pela esquerda, direita, centro, etc.

### ⚽ Zonas de Controle (Voronoi)

As Zonas de Controle mostram:
- Divisão do campo baseada na posição média dos jogadores, usando diagramas de Voronoi.
- Cada região indica qual jogador tem mais probabilidade de alcançar primeiro a bola naquela área.
- Ajuda a visualizar o domínio espacial de cada jogador e a compactação do time.

<br>Muito usado por clubes e analistas para entender:<br>
- Como o time ocupa o espaço ao longo do jogo.
- O grau de compactação defensiva ou ofensiva.
- Quais jogadores controlam as maiores áreas do campo.

### ⚽ Pressões aplicadas em campo
O Mapa de Pressão mostra:
- A localização de cada pressão aplicada durante o jogo (representado por círculos).
- Mostra onde a equipe tentou recuperar a posse de bola.
- Permite avaliar a intensidade e a zona de aplicação da pressão.

<br>Muito usado por clubes e analistas para entender:<br>
- Se a pressão foi alta (próximo ao gol adversário) ou média/baixa.
- A agressividade defensiva do time.
- As zonas preferenciais para tentar retomar a posse.


![](https://raw.githubusercontent.com/josehenriqueroveda/leverkusen-2324/refs/heads/main/imgs/out.png)

Visualmente ficou bem claro o domínio territorial no setor centro ofensivo do campo e a intensidade ofensiva que o Leverkusen imprimiu durante a partida.

Gostou? Dê uma ⭐ nesse repositório!

