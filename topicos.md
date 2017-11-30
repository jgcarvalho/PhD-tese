## Capítulo 1 - Métodos de atribuiçao de estrutura secundária

### Introdução

- DSSP
- Stride
- KAKSI
- PROSS

### Materiais e Métodos

- conjunto de dados top_5000

### Resultados

- ok Quantos resíduos tem a mesma estrutura secundária entre os métodos?
- ok Qual a variação no tamanho das estruturas secundarias?
- ok Qual a variação no número de estruturas secundarias?
    (Tem como mostrar isso melhor que boxplot?)
- ok Quais aminoácidos sofrem maior variação entre os métodos?
    * normalizar pelo número de aminoácidos de cada tipo
- ok Onde ocorrem a falta de consenso?
    * Se for entre resíduos com o mesmo tipo de estrutura há separação/união da estrutura
    * Se for entre resíduos com diferentes tipos de estrutura há 
        encurtamento/elongamento da estrutura
    * Pode ainda ser no inicio/fim da cadeia
- ok Há relação entre o número de resíduos dissensos vs tamanho da proteina?
    * Proteinas mais curtas ou mais longas são mais variáveis?
- ok Quantos resíduos apresentam o dissenso:
    - helice/fita
    - helice/coil
    - fita/coil
    * Isso mostra os principais problemas

### Conclusão

## Capítulo 2 - Rede neural similar ao modelo de Holley e Karplus

### Introdução

- Rede neural desenvolvida por Holley e Karplus

### Materiais e métodos

- Implementação da rede neural similar a HK

### Resultados

- Análise do treinamento variando o número de neurônios
    - Gráfico para mostrar quando o overfitting começa a ocorrer
- Análise do treinamento utilizando os dados de consenso x os métodos separadamente

### Conclusão

## Capítulo 3 - Autômatos celulares

### Introdução

- Autômatos celulares
- EDA

### Materiais e métodos

- Implementação do autômato celular
- EDA distribuido
- Funções de fitness
    - CBA
    - MCC
    - Entropia cruzada 
    - (Funções compostas)

### Resultados

- Q3 obtidos para cada função de fitness
- Distribuição do número de resíduos por estrutura secundária (por f fitness)
- Similaridade entre as estruturas secundárias preditas por diferentes funções de fitness

### Conclusão


## Capítulo 4 Redes neurais residuais

### Introdução

- Redes neurais profundas
- Redes neurais convolucionais profundas
- Redes neurais residuais

### Materiais e métodos

- Rede neural residual implementada

### Resultados

- Q3 obtido
- Embedding (codificação do aminoácido) semelhança entre os resíduos
