import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

#  As perguntas do CEO
# 1. Qual o valor médio do aluguel na cidade de Nova York?
# 2. Qual o valor do aluguel diário mais caro da cidade de Nova York?
# 3. Quais os nomes das regiões que existem na cidade de Nova York?
# 4. Quais são as categorias de imóveis que estão cadastradas dentro da base de dados da cidade de Nova York?
# 5. Quantos usuários (Hosts) únicos cadastrados existem dentro da base de dados da cidade de Nova York?
# 6. Como é a variação dos preços dos imóveis em NY?
# 7. Existem mais imóveis baratos ou caros?
# 8. Qual a distribuição do número de Reviews? Existem imóveis com muitos e outro com poucos reviews?

# CSV dos alugueis em NY
df = pd.read_csv('AB_NYC_2019.csv')

# Configuração para exibir todas as colunas do DataFrame
pd.set_option('display.max_columns', None)

# Configuração para exibir todas as linhas do DataFrame
pd.set_option('display.max_rows', None)

# Verificar colunas do arquivo.csv
# print(df.head())

# 1. Qual o valor médio do aluguel na cidade de Nova York?
# 2. Qual o valor do aluguel diário mais caro da cidade de Nova York?
# Valores dos alugueis
precos_alugueis = df.loc[:, 'price']

# Médio dos valores dos alugueis
media_aluguel = np.mean(precos_alugueis)
string_media_aluguel = f'O valor médio dos alugueis na cidade de Nova Yorque é ${media_aluguel:.2f}'

# Valor minimo dos alugueis
min_aluguel = min(precos_alugueis)
string_min_aluguel = f'O valor minimo dos alugueis na cidade de Nova Yorque é ${min_aluguel:.2f}'

# Valor maximo dos alugueis
max_aluguel = max(precos_alugueis)
string_max_aluguel = f'O valor maximo dos alugueis na cidade de Nova Yorque é ${max_aluguel:.2f}'

# 3. Quais os nomes das regiões que existem na cidade de Nova York?
# Pegar as regiôes distintas de NY
regiao = df.loc[:, 'neighbourhood_group']
regiao = pd.unique(regiao)
regiao_str = ', '.join(r for r in regiao)
string_saida_regiao = f'As regiões de Nova Yorque são: {regiao_str}.'

# 4. Quais são as categorias de imóveis que estão cadastradas dentro da base de dados da cidade de Nova York?
categ_imoveis = df.loc[:, 'room_type']
categ_imoveis = pd.unique(categ_imoveis)
categ_imoveis_str = ', '.join(ci for ci in categ_imoveis)
string_saida_categ_imoveis = f'As categorias de imóveis de Nova Yorque são: {categ_imoveis_str}.'

# 5. Quantos usuários (Hosts) únicos cadastrados existem dentro da base de dados da cidade de Nova York?
hosts = df.loc[:, 'host_id']
quant_hosts_unicos = len(pd.unique(hosts))
string_saida_hosts = f'Há em Nova Yorque {quant_hosts_unicos} usuários (Hosts) únicos.'

# 6. Como é a variação dos preços dos imóveis em NY?
desvio_padrao_alugueis = np.std(precos_alugueis)
string_desvio_padrao_alugueis = f'O valor da variação dos alugueis na cidade de Nova Yorque é ${desvio_padrao_alugueis:.2f}'

# 7. Existem mais imóveis baratos ou caros? Histograma
def verificar_ocorrencia_acima_abaixo_media(lista):
    valores_acima_media = []
    valores_abaixo_media = []

    for valor in lista:
        if valor > np.mean(lista):
            valores_acima_media.append(valor)
        elif valor < np.mean(lista):
            valores_abaixo_media.append(valor)

    if len(valores_acima_media) > len(valores_abaixo_media):
        return 'Existem mais imóveis baratos (abaixo da média de preço) na cidade de Nova Yorque'
    elif len(valores_abaixo_media) > len(valores_acima_media):
        return 'Existem mais imóveis caros (acima da média de preço) na cidade de Nova Yorque'

string_caros_baratos = verificar_ocorrencia_acima_abaixo_media(precos_alugueis)

# 7. Com Histograma:
# linhas = df.loc[:, 'price'] < 1100
# preco_hist = df.loc[linhas, 'price']
# plt.hist(preco_hist, bins=11)
# plt.show()

# 8. Qual a distribuição do número de Reviews? Existem imóveis com muitos e outro com poucos reviews?
linhas = df.loc[:, 'number_of_reviews'] < 600
reviwes = df.loc[linhas, 'number_of_reviews']
plt.hist(reviwes, bins=30)
plt.show()