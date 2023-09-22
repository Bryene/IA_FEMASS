"""
versao python: 3.11.4
Lê um arquivo Excel contendo dados climáticos utilizando numpy e pandas, armazena-os em uma lista e imprime as linhas.

O PIP é uma ferramenta para gerenciamento de pacotes de software escrito em Python.

Foram usados para a instalacao a biblioteca pandas, instalada por pip install pandas.
Foram usados para a instalacao a biblioteca numpy, instalada por pip install numpy.
"""

import numpy as np
import pandas as pd
# Ler o arquivo Excel
dados_climaticos = pd.read_excel('Dados_climaticos_historicos.xlsx', sheet_name='Rio_de_Janeiro', skiprows=2)

# colunas de temperatura
temperatura_media = dados_climaticos['Temperatura média (°C)']
temperatura_minima = dados_climaticos['Temperatura mínima (°C)']
temperatura_maxima = dados_climaticos['Temperatura máxima (°C)']

# Criar um NumPy array de dimensão 12 x 3
temperaturas = np.array([temperatura_minima, temperatura_maxima, temperatura_media]).T

# Imprimir a dimensão do array
print('Dimensão do array de temperaturas:', temperaturas.shape)

# Encontrar o máximo e mínimo valor na coluna de temperatura média
minimo_temp_media = np.min(temperaturas[:, 2])
maximo_temp_media = np.max(temperaturas[:, 2])
print('Mínimo valor na coluna de Temperatura Média:', minimo_temp_media)
print('Máximo valor na coluna de Temperatura Média:', maximo_temp_media)

#argsort: classificar os índices com base na coluna de temperatura média
indices = np.argsort(temperaturas[:, 2])
print('Índices classificados com base na coluna de temperatura média:')
print(indices)


#transpose: Transpor o array
transp_array = temperaturas.T
print('\nArray sendo transposto:')
print(transp_array)


# reshape: Redimensionar o array
red_array = temperaturas.reshape(3, 12)
print('\nArray com 3x12:')
print(red_array)

# flip: Inverter o array
flip_array = np.flip(temperaturas, axis=0)
print('\nArray sendo invertido:')
print(flip_array)


# split: Dividir o array em partes
split= np.split(temperaturas, 3, axis=1)
print('\nArrays com divisao em 3 partes:')
for array in split:
    print(array)

# concatenate: Concatenar o array consigo mesmo
concatenat_array = np.concatenate((temperaturas, temperaturas), axis=1)
print('\nArray concatenado com ele mesmo:')
print(concatenat_array)

# insert: Inserir uma linha de zeros no início do array
insert_array = np.insert(temperaturas, 0, [0, 0, 0], axis=0)
print('\nArray com linha de zeros no início:')
print(insert_array)

# append:Anexa uma linha de zeros no final do array
append_array = np.append(temperaturas, [[0, 0, 0]], axis=0)
print('\nArray com linha de zeros anexada no final:')
print(append_array)

# delete: Excluir a primeira linha do array
delete_array = np.delete(temperaturas, [0], axis=0)
print('\nArray com a 1ª linha excluída:')
print(delete_array)

print('\nAnálise de dados climáticos concluída.')
