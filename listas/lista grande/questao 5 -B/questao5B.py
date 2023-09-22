"""
lê dados climáticos de duas cidades (Macaé e Rio de Janeiro) de um arquivo Excel,
realiza cálculos estatísticos,

O PIP é uma ferramenta para gerenciamento de pacotes de software escrito em Python.

Foram usados para a instalacao a biblioteca pandas, instalada por pip install pandas.
Foram usados para a instalacao a biblioteca matplotlib, instalada por pip install matplotlib.
Foram usados para a instalacao a biblioteca numpy, instalada por pip install numpy.

versao python: 3.11.4
"""
import pandas as pd  # Para manipulação de dados
import matplotlib.pyplot as plt  # Para criação de gráficos
import numpy as np  # Para operações numéricas

# Carregar os dados das temperaturas para Macaé e Rio de Janeiro a partir do excel
dadosM = pd.read_excel('Dados_climaticos_historicos.xlsx', sheet_name='Macae', skiprows=2)
dadosR = pd.read_excel('Dados_climaticos_historicos.xlsx', sheet_name='Rio_de_Janeiro', skiprows=2)

# Criação de um array de meses de 1 a 12
meses = np.arange(1, 13)

# Criação de um gráfico de barras agrupado
plt.figure(figsize=(12, 5))

# Definição da largura das barras
largura_barra = 0.30

# cálculo para posições das barras
posicoesR = meses + largura_barra / 2
posicoesM = meses - largura_barra / 2

# barras para o Rio de Janeiro
plt.bar(posicoesR, dadosR['Temperatura média (°C)'], largura_barra, label='Rio de Janeiro', color='blue')
# barras para Macaé
plt.bar(posicoesM, dadosM['Temperatura média (°C)'], largura_barra, label='Macaé', color='red')

# legenda do eixo X
plt.xlabel('Mês medido')
plt.xticks(meses)

# legenda do eixo Y
plt.ylabel('Temperatura em Média (°C)')

# Adicionando um título ao gráfico
plt.title('Temperaturas médias medidas entre Macaé e Rio de Janeiro')

# Adicionando uma legenda
plt.legend()

# Calculando a diferença de temperaturas mês a mês
diferenca_temperaturas = dadosR['Temperatura média (°C)'] - dadosM['Temperatura média (°C)']

# Plotando um gráfico de barras da diferença de temperaturas
plt.figure(figsize=(12, 5))
plt.bar(meses, diferenca_temperaturas, color='pink')
plt.xlabel('Mês medido')
plt.xticks(meses)
plt.ylabel('Diferença de Temperatura (°C)')
plt.title('Diferença de Temperaturas entre Macaé e Rio de Janeiro')

# Salvando o gráfico em figura
plt.savefig('temp_comparacao.png')

# Exibição dos gráficos
plt.show()



