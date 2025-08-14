# Nova Mecânica para Rituais

## Introdução

Para não confundir com a nomenclatura original, usaremos o termo **Categoria** para classificar rituais.

A categoria de um ritual é **igual ao seu círculo**, podendo aumentar conforme suas formas discentes ou verdadeiras.

Segue abaixo uma tabela com o resumo das informações necessárias:

| Categoria | Sucessos | Ações | PD  | DT  |
| --------- | -------- | ----- | --- | --- |
| 1         | 1        | 1     | 1   | 16  |
| 2         | 2        | 2     | 2   | 17  |
| 3         | 3        | 3     | 4   | 19  |
| 4         | 4        | 4     | 6   | 21  |
| 5         | 5        | 5     | 8   | 23  |
| 6         | 6        | 6     | 10  | 25  |

_Obs.: a contagem de ações é descrita melhor em [Combate](/Jo4FPQ8_T5mruE2ezO4geg)_

---

## Mudanças

### Categoria

É usado uma nova terminologia para não confundir com a do livro original. Alguns rituais possuem em suas formas discentes e verdadeiras o pré-requisito de um círculo maior, mas outras, não. Para unificar a lógica e aumentar a previsibilidade dos custos, ações, DTs e afins, criamos o conceito de **categoria**

A categoria do ritual é controlada, nos níveis mais baixos, pelo limite de gastos de PD por rodada, enquanto os círculos dos rituais são controlados pelo NEx do personagem. Mais informações em [[NEx]].

### Aprimoramentos

Aprimoramentos **Discente** e **Verdadeiro** aumentam a **Categoria** em 1 e 2 passos, respectivamente.

### Custo

O custo em **PD** (Pontos de Determinação) aumenta na mesma lógica dos bônus de treinamento: começa em 1 e depois aumenta de 2 em 2. Considerando a forma como a DT é calculada, o aumento do custo de PD é controlado porque nossa proposta oferece outra forma de balancear um teste: **número de sucessos**. Confira a parte de Conjuração complexa para saber mais.

### DT do Ritual e Número de Sucessos

A DT do ritual, em geral, é **DT = 15 + custo em PD**. Em situações especiais e para alguns rituais específicos, a DT base de 15 pode aumentar ou diminuir, a critério do mestre.

A número de sucessos necessários para passar no teste é igual à sua categoria (1 sucesso para Categoria 1, 2 sucessos para Categoria 2 e assim por diante).

Durante a invocação:

O(s) conjurador(es) realizam um teste de **Ocultismo** contra a DT do ritual e, no caso de:

- **Falha:**
  - Gastam **PD adicionais** iguais à **Categoria** do ritual. _(Ex.: falha em ritual de categoria 3 → custo base 4 PD + 3 PD extras)_
  - A partir de **2 sucessos a menos** que o exigido, perde-se **PD permanente** de forma crescente (1 PD para 2 sucessos a menos, 2 PD para 3 sucessos a menos e assim por diante)
- **Sucesso:**
  - Gastam apenas o custo de PD do ritual, sem adicionais, e não correm o risco de perder PD permanentemente
  - A partir de **2 sucessos a mais** que o exigido, o custo de PD diminue em um passo de forma crescente (1 passo para 2 sucessos a mais, 2 passos para 3 sucessos a mais e assim por diante)
    - _Obs.: um ritual de categoria 0 ou menor não gasta PD_

O(s) alvo(s) realizam um teste de resistência (Reflexos, Fortitude ou Vontade) contra a DT do ritual e os efeitos no caso de **falha** ou **sucesso** seguem a descrição do ritual (em geral, o efeito é parcial: metade do dano e sem condições adicionais)

### Gastar componente
Um personagem pode escolher gastar seu componente ritualístico para receber mais um dado no teste

### Conjuração Conjunta

Essas mudanças, principalmente a acima, prevê rituais que são muito difíceis de serem conjurados sozinhos, o que:

- Deixa mais caro e mais complicado para um só ocultista conjurá-lo, balanceando melhor o jogo; ou
- Estimula os jogadores a trabalharem em equipe

No segundo caso, as ações são dividas igualmente entre os jogadores, arredondando para cima, e a DT e o número de sucessos necessários seguem a lógica de [Ajuda](/-RAAzqL2Q-63gMD-OC69vg). Em conjunto, devem somar o número de sucessos exigido pelo ritual. _(Ex.: ritual de 4º círculo prevê DT 21, 4 sucessos, 4 ações. Assim, com 3 ocultistas juntos, a DT seria 17 e os sucessos necessários 6, ou seja, cada um gastaria 2 ações e precisaria de 2 sucessos)_.

O custo do ritual se mantém o mesmo para cada um envolvido e as penalidades de PD extras também são aplicadas a todos.

Quaisquer personagens treinados em Ocultismo podem ajudar em conjuração, porém: 
* Personagens não Ocultistas ajudando na conjuração de um ritual não saibam ritual sofrem -2 dados no teste
* Personagens Ocultistas que não saibam o ritual OU personagens não ocultistas que saibam o ritual sofrem -1 dado no teste
* Personagens Ocultistas que saibam o ritual não tem penalidade

### Elemento Opressor

Efeitos paranormais de um elemento opressor contra criaturas que possuem Vulnerabilidade II ou maior aplicam **desvantagem** no teste de resistência do alvo _(isso já garante dano aumentado e condições extras; removemos o multiplicador de dano x2 para evitar exageros e balancear com os danos normais , ou seja, não paranormais, como balístico, corte, impacto, perfuração e afins — exemplo: Eletrocussão Discente, que poderia causar 6d6×2 + vulnerável contra Morte, é too much)._

### Outras Regras Especiais

* Ao conjurar um ritual, o agente pode escolher consumir por completo o componente ritualístico e ganhar vantagem no teste, sendo necessária a sua reposição.
* O limite de rituais que alguém pode aprender é 3 * INT.
