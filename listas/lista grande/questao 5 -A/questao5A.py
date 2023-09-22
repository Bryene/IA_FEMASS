"""
lê dados climáticos de duas cidades (Macaé e Rio de Janeiro) de um arquivo Excel,
realiza cálculos estatísticos,

O PIP é uma ferramenta para gerenciamento de pacotes de software escrito em Python.

Foram usados para a instalacao a biblioteca pandas, instalada por pip install pandas.
Foram usados para a instalacao a biblioteca matplotlib, instalada por pip install matplotlib.
Foram usados para a instalacao a biblioteca numpy, instalada por pip install numpy.

versao python: 3.11.4
"""
# Importar as bibliotecas necessárias
import pandas as pd  # Para manipulação de dados
import matplotlib.pyplot as plt  # Para criação de gráficos
import numpy as np  # Para operações numéricas

# Definir uma função para calcular estatísticas das temperaturas
def calcular_estatisticas(dados, cidade):
    # Calcular estatísticas para Temperatura Média
    media_temp_media = dados['Temperatura média (°C)'].mean()  # Calcular a média
    mediana_temp_media = dados['Temperatura média (°C)'].median()  # Calcular a mediana
    desvio_padrao_temp_media = dados['Temperatura média (°C)'].std()  # Calcular o desvio padrão

    # Calcular estatísticas para Temperatura Mínima
    media_temp_minima = dados['Temperatura mínima (°C)'].mean()
    mediana_temp_minima = dados['Temperatura mínima (°C)'].median()
    desvio_padrao_temp_minima = dados['Temperatura mínima (°C)'].std()

    # Calcular estatísticas para Temperatura Máxima
    media_temp_maxima = dados['Temperatura máxima (°C)'].mean()
    mediana_temp_maxima = dados['Temperatura máxima (°C)'].median()
    desvio_padrao_temp_maxima = dados['Temperatura máxima (°C)'].std()

    # Imprimir as estatísticas calculadas
    print(f"Estatísticas para {cidade}:")
    print(f"Média da Temperatura Média: {media_temp_media:.2f}°C")
    print(f"Mediana da Temperatura Média: {mediana_temp_media:.2f}°C")
    print(f"Desvio Padrão da Temperatura Média: {desvio_padrao_temp_media:.2f}°C")
    print(f"Média da Temperatura Mínima: {media_temp_minima:.2f}°C")
    print(f"Mediana da Temperatura Mínima: {mediana_temp_minima:.2f}°C")
    print(f"Desvio Padrão da Temperatura Mínima: {desvio_padrao_temp_minima:.2f}°C")
    print(f"Média da Temperatura Máxima: {media_temp_maxima:.2f}°C")
    print(f"Mediana da Temperatura Máxima: {mediana_temp_maxima:.2f}°C")
    print(f"Desvio Padrão da Temperatura Máxima: {desvio_padrao_temp_maxima:.2f}°C")
    print("\n")

# Carregar os dados das temperaturas para Macaé e Rio de Janeiro a partir do arquivo Excel
dados_macae = pd.read_excel('Dados_climaticos_historicos.xlsx', sheet_name='Macae', skiprows=2)
dados_rio = pd.read_excel('Dados_climaticos_historicos.xlsx', sheet_name='Rio_de_Janeiro', skiprows=2)

# Criar um array de meses de 1 a 12
meses = np.arange(1, 13)

# Criar gráfico para o Rio de Janeiro
plt.figure(figsize=(10, 5))
plt.plot(meses, dados_rio['Temperatura média (°C)'], marker='o', label='Rio de Janeiro - Temperatura Média', linestyle='-', linewidth=2)
plt.plot(meses, dados_rio['Temperatura mínima (°C)'], marker='o', label='Rio de Janeiro - Temperatura Mínima', linestyle='-', linewidth=2)
plt.plot(meses, dados_rio['Temperatura máxima (°C)'], marker='o', label='Rio de Janeiro - Temperatura Máxima', linestyle='--', linewidth=2)
plt.xlabel('Mês medido')
plt.ylabel('Temperatura em (°C)')
plt.title('Temperaturas medidas no Rio de Janeiro')
plt.legend()
plt.grid(True)

# Criar gráfico para Macaé
plt.figure(figsize=(10, 5))
plt.plot(meses, dados_macae['Temperatura média (°C)'], marker='o', label='Macaé - Temperatura Média', linestyle='-', linewidth=2)
plt.plot(meses, dados_macae['Temperatura mínima (°C)'], marker='o', label='Macaé - Temperatura Mínima', linestyle='-', linewidth=2)
plt.plot(meses, dados_macae['Temperatura máxima (°C)'], marker='o', label='Macaé - Temperatura Máxima', linestyle='--', linewidth=2)
plt.xlabel('Mês medido')
plt.ylabel('Temperatura em (°C)')
plt.title('Temperaturas medidas em Macaé')
plt.legend()
plt.grid(True)

# Salvar os gráficos como figuras
plt.savefig('Temp_rio.png')
plt.savefig('temp_macae.png')

# Exibir os gráficos
plt.show()

# Calcular estatísticas para as temperaturas de Macaé e Rio de Janeiro
calcular_estatisticas(dados_macae, 'Macaé')
calcular_estatisticas(dados_rio, 'Rio de Janeiro')




