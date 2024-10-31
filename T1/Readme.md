# Trabalho 1 – Aprendizado Supervisionado

## Integrantes do Grupo (Turma A):

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
        - Uso da função de ativação ReLU, salvo a última camada;
        - Camada CNN com 32 Kernels com janela de 3x3;
        - Uso de MaxPooling 2x2 e Flatten;
        - MLP com uma camada oculta de 64 neurônios e camada final de 10 neurônios com Softmax;
        - Acurácia Final: 98,06%;
        - Perda Final: 0,1389.
    - Modelo 2:
        - Uso da função de ativação ReLU, salvo a última camada;
        - Camada CNN com 32 Kernels com janela de 4x4;
        - Uso de MaxPooling 3x3 e Flatten;
        - MLP com uma camada oculta de 64 neurônios e camada final de 10 neurônios com Softmax;
        - Acurácia Final: 98,21%;
        - Perda Final: 0,1156.
    - Modelo 3:
        - Uso da função de ativação ReLU, salvo a última camada;
        - Camada CNN com 32 Kernels com janela de 4x4;
        - Uso de MaxPooling 3x3 e Flatten;
        - MLP com duas camadas ocultas de 64 neurônios e camada final de 10 neurônios com Softmax;
        - Acurácia Final: 89,02%;
        - Perda Final: 0,3319.
    - Modelo 4:
        - Uso da função de ativação ReLU, salvo a última camada;
        - Camada CNN com 64 Kernels com janela de 4x4;
        - Uso de MaxPooling 3x3 e Flatten;
        - MLP com uma camada oculta de 64 neurônios e camada final de 10 neurônios com Softmax;
        - Acurácia Final: 89,07%;
        - Perda Final: 0,3602.
    - Modelo 5:
        - Uso da função de ativação ReLU, salvo a última camada;
        - Camada CNN com 32 Kernels com janela de 4x4;
        - Uso de MaxPooling 3x3;
        - Camada CNN com 32 Kernels com janela de 3x3;
        - Uso de MaxPooling 2x2 e Flatten;
        - MLP com uma camada oculta de 64 neurônios e camada final de 10 neurônios com Softmax;
        - Acurácia Final: 89,09%;
        - Perda Final: 0,3373.

- Fashion MNIST:
    - Modelo 1:
        - Uso da função de ativação ReLU, salvo a última camada;
        - Camada CNN com 32 Kernels com janela de 3x3;
        - Uso de MaxPooling 2x2 e Flatten;
        - MLP com camada oculta de 64 neurônios e camada final de 10 neurônios com Softmax;
        - Acurácia Final: 89,48%;
        - Perda Final: 0,3721.
    - Modelo 2:
        - Uso da função de ativação ReLU, salvo a última camada;
        - Camada CNN com 32 Kernels com janela de 3x3;
        - Uso de MaxPooling 2x2 e Flatten;
        - MLP com camada oculta de 256 neurônios e camada final de 10 neurônios com Softmax;
        - Acurácia Final: 89,18%;
        - Perda Final: 0,5088.
    - Modelo 3:
        - Uso da função de ativação ReLU, salvo a última camada;
        - Camada CNN com 64 Kernels com janela de 3x3;
        - Uso de MaxPooling 2x2 e Flatten;
        - MLP com camada oculta de 64 neurônios e camada final de 10 neurônios com Softmax;
        - Acurácia Final: 89,06%;
        - Perda Final: 0,4196.
    - Modelo 4:
        - Uso da função de ativação ReLU, salvo a última camada;
        - Camada CNN com 32 Kernels com janela de 3x3;
        - Uso de MaxPooling 2x2 e Flatten;
        - MLP com duas camadas ocultas de 64 neurônios e camada final de 10 neurônios com Softmax;
        - Acurácia Final: 89,46%;
        - Perda Final: 0,3920.
    - Modelo 5:
        - Uso da função de ativação ReLU, salvo a última camada;
        - Duas camadas CNNs com 64 Kernels na primeira e 128 Kernels na segunda, ambas com janela de 3x3;
        - Uso de MaxPooling 2x2 e Flatten;
        - MLP com uma camada oculta de 64 neurônios e camada final de 10 neurônios com Softmax;
        - Acurácia Final: 89,42%;
        - Perda Final: 0,3680.
    - Modelo 6 (Extra):
        - Uso da função de ativação ReLU, salvo a última camada;
        - Duas camadas CNNs com 32 Kernels na primeira e 64 Kernels na segunda, ambas com janela de 3x3;
        - Uso de um MaxPooling 2x2 e outro MaxPooling 3x3, além do Flatten;
        - MLP com uma camada oculta de 64 neurônios e camada final de 10 neurônios com Softmax;
        - Uso de Dropout, técnica que consiste em desativar neurônios aleatoriamente para reduzir o overtfitting,
        uma vez que força o modelo a ser mais robusto. Foram usados Dropout de 25%;
        - Uso do hiperparametro LearningRate, que determina o tamanho dos passos e a velocidade de aprendizado,
        impedindo que o modelo "pule" certas etapas do aprendizado;
        - Uso da função BatchNormalization, que é responsável por normalizar os valores de ativação dos neurônios. Sendo assim, neurônios que ficariam subaproveitados com valores muito baixo como -20, passam a ser mais considerados com a mudança de valor que aproxima a média de 0 e deixa a variância mais controlada.
        - Acurácia Final: 90,91%;
        - Perda Final: 0,2460.

- CIFAR-10:
    - Modelo 1:
        - Uso da função de ativação ReLU, salvo a última camada;
        - Camada CNN com 32 Kernels com janela de 3x3;
        - Uso de MaxPooling 2x2 e Flatten;
        - MLP com duas camadas ocultas de 64 neurônios e camada final  de 10 neurônios com Softmax;
        - Acurácia Final: 39,89%;
        - Perda Final: 1,5982.
    - Modelo 2:
        - Uso da função de ativação ReLU, salvo a última camada;
        - Camada CNN com 32 Kernels com janela de 4x4;
        - Uso de MaxPooling 3x3 e Flatten;
        - MLP com duas camadas ocultas de 64 neurônios e camada final  de 10 neurônios com Softmax;
        - Acurácia Final: 59,22%;
        - Perda Final: 1,2255.
    - Modelo 3:
        - Uso da função de ativação ReLU, salvo a última camada;
        - Camada CNN com 32 Kernels com janela de 4x4;
        - Uso de MaxPooling 3x3 e Flatten;
        - MLP com três camadas ocultas de 64 neurônios e camada final  de 10 neurônios com Softmax;
        - Acurácia Final: 59,73%;
        - Perda Final: 1,1956.
    - Modelo 4:
        - Uso da função de ativação ReLU, salvo a última camada;
        - Duas camadas de CNNs com 64 Kernels com janela de 4x4;
        - Uso de MaxPooling 3x3 (entre camadas CNN) e Flatten;
        - MLP com três camadas ocultas de 64 neurônios e camada final  de 10 neurônios com Softmax;
        - Acurácia Final: 66,12%;
        - Perda Final: 0,9932.
    - Modelo 5:
        - Uso da função de ativação ReLU, salvo a última camada;
        - Camada de CNN com 64 Kernels com janela de 2x2;
        - Uso de MaxPooling 2x2;
        - Camada de CNN com 64 Kernels com janela de 3x3;
        - Uso de MaxPooling 3x3;
        - Camada de CNN com 64 Kernels com janela de 4x4;
        - MLP com quatro camadas ocultas de 64 neurônios e camada final  de 10 neurônios com Softmax;
        - Acurácia Final: 66,96%;
        - Perda Final: 0,9859.

- CIFAR-100:
    - Modelo 1:
        - Uso da função de ativação ReLU, salvo a última camada;
        - Camada CNN com 44 Kernels com janela de 4x4;
        - Uso de MaxPooling 3x3 e Flatten;
        - MLP com uma camada oculta de 100 neurônios e camada final de 100 neurônios com Softmax;
        - Acurácia Final: 4,11%;
        - Perda Final: 4,2543.
    - Modelo 2:
        - Uso da função de ativação ReLU, salvo a última camada;
        - Duas camadas CNN com 64 Kernels com janela de 4x4;
        - Uso de MaxPooling 3x3 e Flatten;
        - MLP com uma camada oculta de 64 neurônios e camada final de 100 neurônios com Softmax;
        - Acurácia Final: 23,47%;
        - Perda Final: 3,6552.
    - Modelo 3:
        - Uso da função de ativação ReLU, salvo a última camada;
        - Três camadas CNN com 64 Kernels com janela de 3x3;
        - Uso de três MaxPooling 2x2 (alternadas entre as de CNN) e Flatten;
        - MLP com uma camada oculta de 64 neurônios e camada final de 100 neurônios com Softmax;
        - Acurácia Final: 25,96%;
        - Perda Final: 3,0327.
    - Modelo 4:
        - Uso da função de ativação ReLU, salvo a última camada;
        - Três camadas CNN com 64 Kernels com janela de 3x3;
        - Uso de três MaxPooling 2x2 (alternadas entre as de CNN) e Flatten;
        - MLP com duas camadas ocultas de 64 neurônios e camada final de 100 neurônios com Softmax;
        - Acurácia Final: 26,11%;
        - Perda Final: 3,0167.
    - Modelo 5:
        - Uso da função de ativação ReLU, salvo a última camada;
        - Três camadas CNN com 64 Kernels com janela de 3x3;
        - Uso de três MaxPooling 2x2 (alternadas entre as de CNN) e Flatten;
        - MLP com duas camadas ocultas de 64 neurônios, uma oculta de 128 neurônios e camada final de
        100 neurônios com Softmax;
        - Acurácia Final: 25,02%;
        - Perda Final: 3,0498.

Com todos esses dados, obteve-se uma relação de ordem de dificuldade entre
os datasets. Abaixo, em ordem de facilidade (o primeiro é mais fácil que o
segundo e assim por diante), estão listados os datasets com as suas respectivas
justificativas para estarem nas suas posições do ranking:

### 2.3. Ranking de Facilidade dos Datasets

1. MNIST:

Esse dataset apresenta apenas 10 classes de imagens em tons de cinza. Todas as instâncias com boa
correlação espacial entre seus atributos, apresentando formas simples para os kernels das CNNs detectarem.
Dessa forma, adquiriu-se a maior acurácia com o modelo mais simples dentre todos os datasets.

2. Fashion MNIST:

Ainda com apenas 10 classes de imagens em tons de cinza, este dataset é um pouco mais desafiador que o
MNIST por apresentar a necessidade de filtros mais elaborados para reconhecer as roupas das imagens.
Isso provavelmente se deve ao fato de haver formas mais complexas para identificar cada tipo de
vestimenta.

3. CIFAR-10:

Agora com 10 classes e imagens coloridas (3 canais, RGB), o problema ficou bem mais desafiador. Os
modelos criados não apresentaram desempenho satisfatório em generalização desse tipo de dado. Há
correlação espacial, porém as formas são muito complexas e se propagam em diversas cores, exigindo
alguma técnica além das CNNs e MLPs para relacionar melhor os pixels coloridos.

4. CIFAR-100:

É semelhante ao caso do CIFAR-10, porém pelo menos 10 vezes mais difícil por apresentar 10 vezes
mais classes. Além disso, as imagens desse dataset são mais diversas e constituem um caso bem mais
próximo daqueles em que LLMs de empresas generalizam. O desempenho adquirido pelo grupo para este
dataset foi bem insatisfatório com apenas as técnicas vistas em aula.

Por fim, realizou-se uma análise dos melhores resultados obtidos para cada
dataset, buscando-se explicar o porquê dessas performances junto do histórico
dos modelos construídos:

### 2.4. Análise dos Resultados

- MNIST:

Como o dataset mais simples, foi possível adquirir a melhor acurácia para este dataset do que para
qualquer outro. Ao manter um pequeno grau de complexidade do modelo, com CNN e MaxPooling que reduzem
bastante a quantidade de atributos para a única camada oculta de MLP, obteve-se um ótimo resultado (acurácia de 98%).
Ao torná-lo mais complexo, com mais camadas de CNN e MLP, observou-se um comportamento de overfitting.

- Fashion MNIST:

Este foi o dataset no qual o grupo mais se debruçou e adquiriu bons resultados. Não foram os melhores resultados,
visto que, com o sexto modelo, obteve-se 91% de acurácia. Porém, utilizou-se técnicas não vistas em aula para
aprimorar a topologia da rede neural. Além de algumas camadas de CNN e uma oculta de MLP, utilizou-se Dropout, técnica
que desativa alguns neurônios temporariamente para evitar overfitting, ajustou-se de forma mais fina a taxa de aprendizado
e ainda o método de BatchNormalization para reduzir o desvio padrão dos dados ao serem propagados. Mesmo assim, sendo mais
simples, o modelo para o MNIST adquiriu melhores resultados.

- CIFAR-10:

A partir deste dataset, o grupo não atingiu mais resultados de acurácia satisfatórios. Aqui, obteve-se apenas 67% de acurácia
com um modelo com diversas camadas de CNN e MLP, utilizando 64 kernels por camada de CNN. Obteve-se um bom equilíbrio de
tamanho de janela que não simplificou demais os atributos a serem passados para MLP, no entanto, por serem imagens coloridas,
provavelmente precisar-se-ia de outras abordagens para aprimorar os resultados.

- CIFAR-100:

Como o mais difícil dos datasets, o grupo adquiriu um resultado bem insatisfatório de apenas 26% de acurácia. É compreensível
que se tenha obtido um resultado ainda pior para classificar bem mais classes quando comparado aos datasets anteriores. Como
discutido acima, no CIFAR-10, precisar-se-ia de alguma técnica além de MLP e CNN para introduzir melhores resultados em dados
de imagens com canais de cores, visto que o aumento das camadas desses dois tipos de redes não agregou significativamente para
o aumento da acurácia. Em alguns casos, até apresentou piora.