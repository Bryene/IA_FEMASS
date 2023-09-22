
"""
lê dados climáticos de Macaé de um arquivo txt,
realiza cálculos estatísticos,

O PIP é uma ferramenta para gerenciamento de pacotes de software escrito em Python.

Foram usados para a instalacao a biblioteca pandas, instalada por pip install pandas.
Foram usados para a instalacao a biblioteca matplotlib, instalada por pip install matplotlib.
Foram usados para a instalacao a biblioteca numpy, instalada por pip install numpy.

versao python: 3.11.4
"""
import pandas as pd  # Importa a biblioteca pandas para manipulação de dados
import matplotlib.pyplot as plt  # Importa a biblioteca matplotlib para criação de gráficos
import numpy as np  # Importa a biblioteca numpy para operações numéricas
import csv

# open para ler os dados do arquivo de texto
meses = []  # Inicializa uma lista para armazenar os meses
temperaturas_minimas = []  # Inicializa uma lista para armazenar as temperaturas mínimas
temperaturas_maximas = []  # Inicializa uma lista para armazenar as temperaturas máximas
temperaturas_medias = []  # Inicializa uma lista para armazenar as temperaturas médias

with open("Dados_historicos_climaticos_macae.txt", "r") as arquivo:
    linhas = arquivo.readlines()  # Lê todas as linhas do arquivo
    for linha in linhas[1:]:  # Ignora a primeira linha (cabeçalho)
        dados = linha.strip().split()  # Divide a linha em palavras
        meses.append(dados[0])  # Adiciona o mês à lista de meses
        temperaturas_minimas.append(float(dados[1]))  # Adiciona a temperatura mínima à lista
        temperaturas_maximas.append(float(dados[2]))  # Adiciona a temperatura máxima à lista
        temperaturas_medias.append(float(dados[3]))  # Adiciona a temperatura média à lista

# dicionário de dados
dados_climaticos = {}  # Inicializa um dicionário para armazenar os dados climáticos
for i in range(len(meses)):  # Itera sobre os meses e seus dados correspondentes
    dados_mes = {
        "TempMin": temperaturas_minimas[i],  # Temperatura mínima
        "TempMax": temperaturas_maximas[i],  # Temperatura máxima
        "TempMedia": temperaturas_medias[i]  # Temperatura média
    }
    dados_climaticos[meses[i]] = dados_mes  # Adiciona os dados ao dicionário usando o mês como chave

#Mostra o conteúdo do dicionário
print("Demonstrando as listas pedidas: ")
for mes, dados in dados_climaticos.items():
    print(f"{mes}: TempMin={dados['TempMin']} || TempMax={dados['TempMax']} || TempMedia={dados['TempMedia']}\n")

# temperatura média de julho
temperatura_media_julho = dados_climaticos["Julho"]["TempMedia"]  # Obtém a temperatura média de julho do dicionário
print(f"Temperatura média do mês de julho é: {temperatura_media_julho}")

# Calcula a temperatura média anual
temperatura_media_anual = np.mean(temperaturas_medias)
print(f"Temperatura média anual: {temperatura_media_anual:.2f}°C")

# 5. Plotar um gráfico de temperatura
plt.figure(figsize=(12,6))  # Configura o tamanho da figura
plt.plot(meses, temperaturas_minimas, marker='o', label='Tmin')  # Plot da temperatura mínima
plt.plot(meses, temperaturas_maximas, marker='o', label='Tmax')  # Plot da temperatura máxima
plt.plot(meses, temperaturas_medias, marker='o', label='Tmedia')  # Plot da temperatura média
plt.xlabel('Meses')  # Rótulo do eixo X
plt.ylabel('Temperatura')  # Rótulo do eixo Y
plt.title('Temperaturas Mensais')  # Título do gráfico
plt.legend()  # Adiciona a legenda ao gráfico
plt.grid(True)  # Habilita a grade no gráfico
plt.xticks(rotation=45)  # Rotação dos rótulos do eixo x para melhor legibilidade
plt.show()  # Exibe o gráfico
