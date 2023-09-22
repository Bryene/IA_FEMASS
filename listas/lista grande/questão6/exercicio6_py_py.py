
"""
lê dados climáticos de duas cidades (Macaé e Rio de Janeiro) de um arquivo Excel,
realiza cálculos estatísticos e cria um novo arquivo
O PIP é uma ferramenta para gerenciamento de pacotes de software escrito em Python.
Foram usados para a instalacao a biblioteca pandas, instalada por pip install pandas.

versao python: 3.11.4
"""

import pandas as pd # # Para manipulação de dados


# le os cada aba do arquivo e armazena em duas variaves diferente 
dadosMacae = pd.read_excel("Dados_climaticos_historicos.xlsx", sheet_name="Historico_Clima_Macae")#, skiprows=(3),nrows=7
dadosRJ = pd.read_excel("Dados_climaticos_historicos.xlsx", sheet_name="Historico_Clima_Rio_de_Janeiro")#, skiprows=(3)

display(dadosMacae)

# Declaração devariáveis que seram usadas 
somaMacaeTMedia =0
somaMacaeTMinima =0
somaMacaeTMaxima =0

somaRJTMedia =0
somaRJMinima =0
somaRJMaxima =0

VmesMaiorTempMacae =0
VmesMenorTempMacae =99

VmesMaiorTempRJ =0
VmesMenorTempRJ =99

VmesMaisChuvosoMacae = 0
VmesMaisChuvosoRJ =0
VmesMenosChuvosoMacae = 999
VmesMenosChuvosoRJ = 999

acumuloChuvaAnualMacae =0
acumuloChuvaAnualRJ =0

umidadeMacae=0
umidadeRJ=0


'''
unnamed: Colunas sem nome
'''
# Loop que percorre os meses (de 1 a 12) para calcular diversas estatísticas
for i in range(1, 13):
    # Cálculo das somas mensais de temperaturas para Macaé e Rio de Janeiro
    somaMacaeTMedia += float(dadosMacae.loc[3, f'Unnamed: {i}'])
    somaMacaeTMinima += float(dadosMacae.loc[4, f'Unnamed: {i}'])
    somaMacaeTMaxima += float(dadosMacae.loc[5, f'Unnamed: {i}'])
    
    # Imprime uma tabulação para separar os resultados de Macaé e Rio de Janeiro
    print("\t")
    
    somaRJTMedia += float(dadosRJ.loc[3, f'Unnamed: {i}'])
    somaRJMinima += float(dadosRJ.loc[4, f'Unnamed: {i}'])
    somaRJMaxima += float(dadosRJ.loc[5, f'Unnamed: {i}'])

    # Cálculo do acúmulo anual de chuva para Macaé e Rio de Janeiro
    acumuloChuvaAnualMacae += float(dadosMacae.loc[6, f'Unnamed: {i}'])
    acumuloChuvaAnualRJ += float(dadosRJ.loc[6, f'Unnamed: {i}'])

    # Cálculo da umidade para Macaé (a umidade do Rio de Janeiro é somada no final)
    umidadeMacae += float(dadosMacae.loc[7, f'Unnamed: {i}'])

    ############################ Macaé #############################################
    
    # Verifica se o mês atual em Macaé teve a maior temperatura registrada
    if VmesMaiorTempMacae < float(dadosMacae.loc[5, f'Unnamed: {i}']):
        VmesMaiorTempMacae = float(dadosMacae.loc[5, f'Unnamed: {i}'])
        mesMaiorTempMacae = dadosMacae.loc[2, f'Unnamed: {i}']

    # Verifica se o mês atual em Macaé teve a menor temperatura registrada
    if VmesMenorTempMacae > float(dadosMacae.loc[3, f'Unnamed: {i}']):
        VmesMenorTempMacae = float(dadosMacae.loc[3, f'Unnamed: {i}'])
        mesMenorTempMacae = dadosMacae.loc[2, f'Unnamed: {i}']

    # Verifica se o mês atual em Macaé teve o maior acumulado de chuva
    if VmesMaisChuvosoMacae < float(dadosMacae.loc[6, f'Unnamed: {i}']):
        VmesMaisChuvosoMacae = float(dadosMacae.loc[6, f'Unnamed: {i}'])
        mesMaisChuvosoMacae = dadosMacae.loc[2, f'Unnamed: {i}']

    # Verifica se o mês atual em Macaé teve o menor acumulado de chuva
    if VmesMenosChuvosoMacae > float(dadosMacae.loc[6, f'Unnamed: {i}']):
        VmesMenosChuvosoMacae = float(dadosMacae.loc[6, f'Unnamed: {i}'])
        mesMenosChuvosoMacae = dadosMacae.loc[2, f'Unnamed: {i}']

    ############################ Rio de Janeiro ############################################

    # Verifica se o mês atual no Rio de Janeiro teve a maior temperatura registrada
    if VmesMaiorTempRJ < float(dadosRJ.loc[5, f'Unnamed: {i}']):
        VmesMaiorTempRJ = float(dadosRJ.loc[5, f'Unnamed: {i}'])
        mesMaiorTempRJ = dadosRJ.loc[2, f'Unnamed: {i}']

    # Verifica se o mês atual no Rio de Janeiro teve a menor temperatura registrada
    if VmesMenorTempRJ > float(dadosRJ.loc[3, f'Unnamed: {i}']):
        VmesMenorTempRJ = float(dadosRJ.loc[3, f'Unnamed: {i}'])
        mesMenorTempRJ = dadosRJ.loc[2, f'Unnamed: {i}']

    # Verifica se o mês atual no Rio de Janeiro teve o maior acumulado de chuva
    if VmesMaisChuvosoRJ < float(dadosRJ.loc[6, f'Unnamed: {i}']):
        VmesMaisChuvosoRJ = float(dadosRJ.loc[6, f'Unnamed: {i}'])
        mesMaisChuvosoRJ = dadosRJ.loc[2, f'Unnamed: {i}']

    # Verifica se o mês atual no Rio de Janeiro teve o menor acumulado de chuva
    if VmesMenosChuvosoRJ > float(dadosRJ.loc[6, f'Unnamed: {i}']):
        VmesMenosChuvosoRJ = float(dadosRJ.loc[6, f'Unnamed: {i}'])
        mesMenosChuvosoRJ = dadosRJ.loc[2, f'Unnamed: {i}']

    # Adição da umidade do Rio de Janeiro (a umidade de Macaé já foi adicionada acima)
    umidadeRJ += float(dadosMacae.loc[7, f'Unnamed: {i}'])

# Cálculo das médias de temperatura para Macaé e Rio de Janeiro
mediaTMediaMacae = somaMacaeTMedia / 12
mediaTMinimaMacae = somaMacaeTMinima / 12
mediaTMaximaMacae = somaMacaeTMaxima / 12

mediaTMediaRJ = somaRJTMedia / 12
mediaTMinimaRJ = somaRJMinima / 12
mediaTMaximaRJ = somaRJMaxima / 12

# Demonstra informações estatísticas
print("Macaé")
print(f"Média de Temperatura Média: {mediaTMediaMacae}")
print(f"Média de Temperatura Mínima: {mediaTMinimaMacae}")
print(f"Média de Temperatura Máxima: {mediaTMaximaMacae}")

print("RJ")
print(f"Média de Temperatura Média: {mediaTMediaRJ}")
print(f"Média de Temperatura Mínima: {mediaTMinimaRJ}")
print(f"Média de Temperatura Máxima: {mediaTMaximaRJ}")

print("")

print("Macaé")
print("Mês de maior temperatura é:")
print(mesMaiorTempMacae)
print("Mês de menor temperatura é:")
print(mesMenorTempMacae)
print("Mês mais chuvoso:")
print(mesMaisChuvosoMacae)
print("Mês menos chuvoso:")
print(mesMenosChuvosoMacae)
print(f"Acúmulo de chuva: {acumuloChuvaAnualMacae} mm")

print("")

print("RJ")
print("Mês de maior temperatura é:")
print(mesMaiorTempRJ)
print("Mês de menor temperatura é:")
print(mesMenorTempRJ)
print("Mês mais chuvoso:")
print(mesMaisChuvosoRJ)
print("Mês menos chuvoso:")
print(mesMenosChuvosoRJ)
print(f"Acúmulo de chuva: {acumuloChuvaAnualRJ} mm")

print("")

# Compara as umidades de Macaé e Rio de Janeiro para determinar qual cidade é mais úmida
if umidadeRJ > umidadeMacae:
    quemEMaisUmido = "Rio de Janeiro é mais úmido"
else:
    quemEMaisUmido = "Macaé é mais úmido"

quemEMaisUmido


# Demonstra informações estatísticas
print("Estatísticas para Macaé:")
print(f"Média de Temperatura Média: {mediaTMediaMacae}")
print(f"Média de Temperatura Mínima: {mediaTMinimaMacae}")
print(f"Média de Temperatura Máxima: {mediaTMaximaMacae}")
print(f"Mês de maior temperatura: {mesMaiorTempMacae}")
print(f"Mês de menor temperatura: {mesMenorTempMacae}")
print(f"Mês mais chuvoso: {mesMaisChuvosoMacae}")
print(f"Mês menos chuvoso: {mesMenosChuvosoMacae}")
print(f"Acúmulo de chuva anual: {acumuloChuvaAnualMacae} mm")
print()

print("Estatísticas para Rio de Janeiro:")
print(f"Média de Temperatura Média: {mediaTMediaRJ}")
print(f"Média de Temperatura Mínima: {mediaTMinimaRJ}")
print(f"Média de Temperatura Máxima: {mediaTMaximaRJ}")
print(f"Mês de maior temperatura: {mesMaiorTempRJ}")
print(f"Mês de menor temperatura: {mesMenorTempRJ}")
print(f"Mês mais chuvoso: {mesMaisChuvosoRJ}")
print(f"Mês menos chuvoso: {mesMenosChuvosoRJ}")
print(f"Acúmulo de chuva anual: {acumuloChuvaAnualRJ} mm")
print()
print(f"Comparação de umidade: {quemEMaisUmido}\n")
#########################################################################################
# Gravação dos dados em um novo arquivo Excel para Macaé
# Define a média da temperatura média para o mês 13 na planilha de Macaé
dadosMacae.loc[3,'Unnamed: 13'] = round(mediaTMediaMacae, 2)

# Define a média da temperatura mínima para o mês 13 na planilha de Macaé
dadosMacae.loc[4,'Unnamed: 13'] = round(mediaTMinimaMacae, 2)

# Define a média da temperatura máxima para o mês 13 na planilha de Macaé
dadosMacae.loc[5,'Unnamed: 13'] = round(mediaTMaximaMacae, 2)

# Define o acúmulo anual de chuva para o mês 13 na planilha de Macaé
dadosMacae.loc[6,'Unnamed: 13'] = round(acumuloChuvaAnualMacae)

# Define o nome e valor do mês com a maior temperatura na planilha de Macaé
dadosMacae.loc[11,'Unnamed: 1'] = 'Mes maior temperatura'
dadosMacae.loc[11,'Unnamed: 2'] = mesMaiorTempMacae

# Define o nome e valor do mês com a menor temperatura na planilha de Macaé
dadosMacae.loc[11,'Unnamed: 3'] = 'Mes menor temperatura'
dadosMacae.loc[11,'Unnamed: 4'] = mesMenorTempMacae

# Define o nome e valor do mês mais chuvoso na planilha de Macaé
dadosMacae.loc[11,'Unnamed: 5'] = 'Mes mais chuvoso'
dadosMacae.loc[11,'Unnamed: 6'] = mesMaisChuvosoMacae

# Define o nome e valor do mês menos chuvoso na planilha de Macaé
dadosMacae.loc[11,'Unnamed: 7'] = 'Mes menos chuvoso'
dadosMacae.loc[11,'Unnamed: 8'] = mesMenosChuvosoMacae

# Define o nome e valor do maior acúmulo de chuva na planilha de Macaé
dadosMacae.loc[11,'Unnamed: 9'] = 'Maior acumulo de chuva(mm)'
dadosMacae.loc[11,'Unnamed: 10'] = acumuloChuvaAnualMacae

# Define qual cidade é mais úmida na planilha de Macaé
dadosMacae.loc[11,'Unnamed: 11'] = quemEMaisUmido

# Gravação dos dados em um novo arquivo Excel para Rio de Janeiro (os mesmos procedimentos que para Macaé)
dadosRJ.loc[3,'Unnamed: 13'] = round(mediaTMediaRJ, 2)
dadosRJ.loc[4,'Unnamed: 13'] = round(mediaTMinimaRJ, 2)
dadosRJ.loc[5,'Unnamed: 13'] = round(mediaTMaximaRJ, 2)
dadosRJ.loc[6,'Unnamed: 13'] = round(acumuloChuvaAnualRJ)
dadosRJ.loc[11,'Unnamed: 1'] = 'Mes maior temperatura'
dadosRJ.loc[11,'Unnamed: 2'] = mesMaiorTempRJ
dadosRJ.loc[11,'Unnamed: 3'] = 'Mes menor temperatura'
dadosRJ.loc[11,'Unnamed: 4'] = mesMenorTempRJ
dadosRJ.loc[11,'Unnamed: 5'] = 'Mes mais chuvoso'
dadosRJ.loc[11,'Unnamed: 6'] = mesMaisChuvosoRJ
dadosRJ.loc[11,'Unnamed: 7'] = 'Mes menos chuvoso'
dadosRJ.loc[11,'Unnamed: 8'] = mesMenosChuvosoRJ
dadosRJ.loc[11,'Unnamed: 9'] = 'Maior acumulo de chuva(mm)'
dadosRJ.loc[11,'Unnamed: 10'] = acumuloChuvaAnualRJ
dadosRJ.loc[11,'Unnamed: 11'] = quemEMaisUmido


# Exibe as planilhas de dados atualizadas para Macaé e Rio de Janeiro
display(dadosMacae)
display(dadosRJ)


# gravação dos dados e criação dos arquivos 
dadosMacae.to_excel('Dados_climaticos_historicos_Macae.xlsx', index=False)
dadosRJ.to_excel('Dados_climaticos_historicos_RJ.xlsx', index=False)