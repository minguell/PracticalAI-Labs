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

A inicialização com `b = 0`, `w = 1`, `alpha = 0.8` e `num_iterations = 100`
trouxe o melhor resultado que o grupo conseguiu obter.

O erro quadrático médio final obtido com os parâmetros e hiperparâmetros
iniciais que mais otimizaram a hipótese do modelo foi de
`mse<sub>f</sub> = 0.014802014491336607`.

## 2. Tensorflow/Keras

Neste ponto, avaliou-se a biblioteca Tensorflow/Keras para modelar redes
neurais que geram hipóteses para os clássicos datasets que são detalhados
abaixo:

### 2.1. Informações sobre os Datasets

- MNIST:

    - Número de Classes: 10;

    - Número de Amostras: 60000 de treinamento e 10000 de teste;

    - Tamanho das Imagens: 28 x 28 x 1 (altura x largura x canais de cor).

- Fashion MNIST:

    - Número de Classes: 10;

    - Número de Amostras: 60000 de treinamento e 10000 de teste;


    - Tamanho das Imagens: 28 x 28 x 1 (altura x largura x canais de cor).

- CIFAR-10:

    - Número de Classes: 10;

    - Número de Amostras: 50000 de treinamento e 10000 de teste;

    - Tamanho das Imagens: 32 x 32 x 3 (altura x largura x canais de cor).

- CIFAR-100:

    - Número de Classes: 100;

    - Número de Amostras: 50000 de treinamento e 10000 de teste;

    - Tamanho das Imagens: 32 x 32 x 3 (altura x largura x canais de cor).

Para cada dataset, foram testados as seguintes cinco configurações de 
modelos com as respectivas acurácias e erro médio no final do treinamento:

### 2.2. Modelos Implementados para cada Dataset

- MNIST:

    - Modelo 1:
       
        - ...

        - Acurácia Final: ?;

        - Perda Final: ?.

    - Modelo 2:
       
        - ...

        - Acurácia Final: ?;

        - Perda Final: ?.

    - Modelo 3:
       
        - ...

        - Acurácia Final: ?;

        - Perda Final: ?.

    - Modelo 4:
       
        - ...

        - Acurácia Final: ?;

        - Perda Final: ?.

    - Modelo 5:
       
        - ...

        - Acurácia Final: ?;

        - Perda Final: ?.

- Fashion MNIST:

    - Modelo 1:
       
        - Uso da função de ativação ReLU, salvo a última camada;

        - Camada CNN com 32 Kernels com janela de 3x3;

        - Uso de MaxPooling 2x2 e Flatten;

        - MLP com camada oculta de 64 neurônios e camada final de 10 neurônios com Softmax;

        - Acurácia Final: 89,48%;

        - Perda Final: 0,3721;

    - Modelo 2:
       
        - Uso da função de ativação ReLU, salvo a última camada;

        - Camada CNN com 32 Kernels com janela de 3x3;

        - Uso de MaxPooling 2x2 e Flatten;

        - MLP com camada oculta de 256 neurônios e camada final de 10 neurônios com Softmax;

        - Acurácia Final: 89,18%;

        - Perda Final: 0,5088;

    - Modelo 3:
       
        - Uso da função de ativação ReLU, salvo a última camada;

        - Camada CNN com 64 Kernels com janela de 3x3;

        - Uso de MaxPooling 2x2 e Flatten;

        - MLP com camada oculta de 64 neurônios e camada final de 10 neurônios com Softmax;

        - Acurácia Final: 89,06%;

        - Perda Final: 0,4196;

    - Modelo 4:
       
        - Uso da função de ativação ReLU, salvo a última camada;

        - Camada CNN com 32 Kernels com janela de 3x3;

        - Uso de MaxPooling 2x2 e Flatten;

        - MLP com duas camadas ocultas de 64 neurônios e camada final de 10 neurônios com Softmax;

        - Acurácia Final: 89,46%;

        - Perda Final: 0,3920;

    - Modelo 5:
       
        - Uso da função de ativação ReLU, salvo a última camada;

        - Duas camadas CNNs com 64 Kernels na primeira e 128 Kernels na segunda, ambas com janela de 3x3;

        - Uso de MaxPooling 2x2 e Flatten;

        - MLP com uma camada oculta de 64 neurônios e camada final de 10 neurônios com Softmax;

        - Acurácia Final: 89,42%;

        - Perda Final: 0,3680;

    - Modelo 6 (Extra):
       
        - Uso da função de ativação ReLU, salvo a última camada;

        - Duas camadas CNNs com 48 Kernels na primeira e 64 Kernels na segunda, ambas com janela de 3x3;

        - Uso de um MaxPooling 2x2 e outro MaxPooling 3x3, além do Flatten;

        - MLP com uma camada oculta de 64 neurônios e camada final de 10 neurônios com Softmax;

        - Uso de Dropout, técnica que consiste em desativar neurônios aleatoriamente para reduzir o           overtfitting, uma vez que força o modelo a ser mais robusto. Foram usados Dropout de 20% e de 40%.

        - Uso do hiperparametro LearningRate, que determina o tamanho dos passos e a velocidade de aprendizado, impedindo que o modelo "pule" certas etapas do aprendizado 

        - Acurácia Final: 86,29%;

        - Perda Final: 0,3652;


- CIFAR-10:

    - Modelo 1:
       
        - ...

        - Acurácia Final: ?;

        - Perda Final: ?.

    - Modelo 2:
       
        - ...

        - Acurácia Final: ?;

        - Perda Final: ?.

    - Modelo 3:
       
        - ...

        - Acurácia Final: ?;

        - Perda Final: ?.

    - Modelo 4:
       
        - ...

        - Acurácia Final: ?;

        - Perda Final: ?.

    - Modelo 5:
       
        - ...

        - Acurácia Final: ?;

        - Perda Final: ?.

- CIFAR-100:

    - Modelo 1:
       
        - ...

        - Acurácia Final: ?;

        - Perda Final: ?.

    - Modelo 2:
       
        - ...

        - Acurácia Final: ?;

        - Perda Final: ?.

    - Modelo 3:
       
        - ...

        - Acurácia Final: ?;

        - Perda Final: ?.

    - Modelo 4:
       
        - ...

        - Acurácia Final: ?;

        - Perda Final: ?.

    - Modelo 5:
       
        - ...

        - Acurácia Final: ?;

        - Perda Final: ?.

Com todos esses dados, obteve-se uma relação de ordem de dificuldade entre
os datasets. Abaixo, em ordem de facilidade (o primeiro é mais fácil que o
segundo e assim por diante), estão listados os datasets com as suas respectivas
justificativas para estarem nas suas posições do ranking:

### 2.3. Ranking de Facilidade dos Datasets

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

### 2.4. Análise dos Resultados

- MNIST:

    - Análise...

- Fashion MNIST:

    - Análise...

- CIFAR-10:

    - Análise...

- CIFAR-100:

    - Análise...