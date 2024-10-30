import numpy as np

def compute_mse(b, w, data):
    """
    Calcula o erro quadratico medio
    :param b: float - bias (intercepto da reta)
    :param w: float - peso (inclinacao da reta)
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :return: float - o erro quadratico medio
    """
    x = data[:,0]
    y = data[:,1]
    n = len(data)
    mse = 0
    for i in range(n):
        mse += (y[i] - (w*x[i] + b))**2
    mse = mse/n

    return mse     


def step_gradient(b, w, data, alpha):
    """
    Executa uma atualização por descida do gradiente e retorna os valores atualizados de b e w.
    :param b: float - bias (intercepto da reta)
    :param w: float - peso (inclinacao da reta)
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :return: float,float - os novos valores de b e w, respectivamente
    """
    x = data[:,0]
    y = data[:,1]
    n = len(data)
    part_deriv_b = 0
    part_deriv_w = 0
    for i in range(n):
        part_deriv_b += -2*(y[i] - (w*x[i] + b))
        part_deriv_w += -2*x[i]*(y[i] - (w*x[i] + b))
    part_deriv_b = part_deriv_b/n
    part_deriv_w = part_deriv_w/n

    new_b = b - alpha*part_deriv_b
    new_w = w - alpha*part_deriv_w

    return new_b, new_w

def fit(data, b, w, alpha, num_iterations):
    """
    Para cada época/iteração, executa uma atualização por descida de
    gradiente e registra os valores atualizados de b e w.
    Ao final, retorna duas listas, uma com os b e outra com os w
    obtidos ao longo da execução (o último valor das listas deve
    corresponder à última época/iteração).

    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param b: float - bias (intercepto da reta)
    :param w: float - peso (inclinacao da reta)
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :param num_iterations: int - numero de épocas/iterações para executar a descida de gradiente
    :return: list,list - uma lista com os b e outra com os w obtidos ao longo da execução
    """
    raise NotImplementedError  # flamingo


