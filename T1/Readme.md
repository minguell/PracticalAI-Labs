# Trabalho 1 – Aprendizado Supervisionado

## Integrantes do Grupo:

- Ana Cláudia Rodrigues (00343123);
- Miguel Dutra Fontes Guerra (00342573);
- Pedro Lubaszewski Lima (00341810).

## Bibliotecas Necessárias (Python):

- Numpy:

```
pip install numpy
```

- Matplotlib:

```
pip install matplotlib
```

- Pandas:

```
pip install pandas
```

- Tensorflow:

```
pip install tensorflow
```

## 1. Regressão Linear

Nesta etapa, foi implementado um modelo de aprendizado supervisionado
que utiliza o método de regressão linear.

Os dados de entrada foram normalizados através da função max-min
(colocando os valores de entrada no intervalo de 0 a 1).

A inicialização com `b = ?`, `w = ?`, `alpha = ?` e `num_iterations = ?`
trouxe o melhor resultado que o grupo conseguiu obter.

O erro quadrático médio final obtido com os parâmetros e hiperparâmetros
iniciais que mais otimizaram a hipótese do modelo foi de
`mse<sub>f</sub> = ?`.

## 2. Tensorflow/Keras

Neste ponto, avaliou-se a biblioteca Tensorflow/Keras para modelar redes
neurais que geram hipóteses para os clássicos datasets que são detalhados
abaixo:

### 2.1. Informações sobre os Datasets:

- MNIST:

    - Número de Classes: ?;

    - Número de Amostras: ?;

    - Tamanho das Imagens: ? x ? x ? (altura x largura x canais de cor).

- Fashion MNIST:

    - Número de Classes: ?;

    - Número de Amostras: ?;

    - Tamanho das Imagens: ? x ? x ? (altura x largura x canais de cor).

- CIFAR-10:

    - Número de Classes: ?;

    - Número de Amostras: ?;

    - Tamanho das Imagens: ? x ? x ? (altura x largura x canais de cor).

- CIFAR-100:

    - Número de Classes: ?;

    - Número de Amostras: ?;

    - Tamanho das Imagens: ? x ? x ? (altura x largura x canais de cor).

Para cada dataset, foram testados as seguintes cinco configurações de 
modelos com as respectivas acurácias e erro médio no final do treinamento:

### 2.2. Modelos Implementados para cada Dataset:

- MNIST:

    - Modelo 1:
       
        - ...

        - Acurácia Final: ?;

        - Erro Médio Final: ?.

    - Modelo 2:
       
        - ...

        - Acurácia Final: ?;

        - Erro Médio Final: ?.

    - Modelo 3:
       
        - ...

        - Acurácia Final: ?;

        - Erro Médio Final: ?.

    - Modelo 4:
       
        - ...

        - Acurácia Final: ?;

        - Erro Médio Final: ?.

    - Modelo 5:
       
        - ...

        - Acurácia Final: ?;

        - Erro Médio Final: ?.

- Fashion MNIST:

    - Modelo 1:
       
        - ...

        - Acurácia Final: ?;

        - Erro Médio Final: ?.

    - Modelo 2:
       
        - ...

        - Acurácia Final: ?;

        - Erro Médio Final: ?.

    - Modelo 3:
       
        - ...

        - Acurácia Final: ?;

        - Erro Médio Final: ?.

    - Modelo 4:
       
        - ...

        - Acurácia Final: ?;

        - Erro Médio Final: ?.

    - Modelo 5:
       
        - ...

        - Acurácia Final: ?;

        - Erro Médio Final: ?.

- CIFAR-10:

    - Modelo 1:
       
        - ...

        - Acurácia Final: ?;

        - Erro Médio Final: ?.

    - Modelo 2:
       
        - ...

        - Acurácia Final: ?;

        - Erro Médio Final: ?.

    - Modelo 3:
       
        - ...

        - Acurácia Final: ?;

        - Erro Médio Final: ?.

    - Modelo 4:
       
        - ...

        - Acurácia Final: ?;

        - Erro Médio Final: ?.

    - Modelo 5:
       
        - ...

        - Acurácia Final: ?;

        - Erro Médio Final: ?.

- CIFAR-100:

    - Modelo 1:
       
        - ...

        - Acurácia Final: ?;

        - Erro Médio Final: ?.

    - Modelo 2:
       
        - ...

        - Acurácia Final: ?;

        - Erro Médio Final: ?.

    - Modelo 3:
       
        - ...

        - Acurácia Final: ?;

        - Erro Médio Final: ?.

    - Modelo 4:
       
        - ...

        - Acurácia Final: ?;

        - Erro Médio Final: ?.

    - Modelo 5:
       
        - ...

        - Acurácia Final: ?;

        - Erro Médio Final: ?.

Com todos esses dados, obteve-se uma relação de ordem de dificuldade entre
os datasets. Abaixo, em ordem de facilidade (o primeiro é mais fácil que o
segundo e assim por diante), estão listados os datasets com as suas respectivas
justificativas para estarem nas suas posições do ranking:

### 2.3. Ranking de Facilidade dos Datasets:

1. dataset_mais_facil:

    - Justificativa...

2. segundo_dataset_mais_facil:

    - Justificativa...

3. segundo_dataset_mais_dificil:

    - Justificativa...

4. dataset_mais_dificil:

    - Justificativa...

Por fim, realizou-se uma análise dos melhores resultados obtidos para cada
dataset, buscando-se explicar o porquê dessas performances junto do histórico
dos modelos construídos:

### 2.4. Análise dos Resultados:

- MNIST:

    - Análise...

- Fashion MNIST:

    - Análise...

- CIFAR-10:

    - Análise...

- CIFAR-100:

    - Análise...