# Problem B - Another Aztec Riddle

## Descrição

Existe um baralho de cartas, representado numa grelha de tamanho `nr` (linhas) por `nc` (colunas), em que cada carta está posicionada numa célula da grelha. O desafio é preencher essa grelha de forma que **cada coluna contenha exatamente `c` cartas** e **cada linha contenha exatamente `r` cartas**.

Cada disposição diferente das cartas na grelha que respeite as restrições conta como um arranjo válido. O objetivo é, para cada instância do problema, **determinar quantos arranjos distintos** existem. O resultado de cada caso é sempre inferior a $2^{63}$.

Se não houver nenhuma configuração possível, deve-se considerar o resultado como zero.

## Entrada

A entrada contém:

* Um inteiro `T` representando o número de casos de teste.
* Para cada caso de teste:
  * Uma linha com dois inteiros `nc` e `nr`:
    * `nc` → número de colunas da grelha
    * `nr` → número de linhas da grelha
  * Uma linha com dois inteiros `c` e `r`:
    * `c` → número de cartas a colocar em cada coluna
    * `r` → número de cartas a colocar em cada linha

## Saída

Para cada caso de teste, é suposto imprimir um inteiro representando o **total de arranjos possíveis** para preencher a grelha, obedecendo exatamente ao número de cartas em cada linha e coluna.

## Restrições

```
2 <= nr <= 24
2 <= nc <= 24
1 <= r <= 7
1 <= c <= 7
```

## Exemplo

### Entrada

```
3
2 2
1 1
2 4
2 1
2 8
4 1
```

### Saída

```
2
6
70
```
