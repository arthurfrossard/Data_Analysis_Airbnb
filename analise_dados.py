import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import folium
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
# 9. Qual a distribuição dos imóveis de acordo com o número mínimo de pernoites que podem ser agendado?
# 10. Qual a média e a mediana de imóveis cadastrado por host (dono do imóvel)?
# 11. Qual a data mais recente da última avaliação
# 12. Qual o valor máximo de pernoites agendadas?
# 13. Quantos nomes de donos de imóveis são únicos?
# 14. Quanto identificadores únicos existem na base de dados?
# 15. Qual é o valor do aluguel (diária) mais caro de cada região da base de dados da cidade de Nova York, apenas para os imóveis disponível para alugar?
# 16. Conseguimos saber onde estão localizados os imóveis com o valor do aluguel mais caro, na cidade de Nova York, apenas para os imóveis disponível para alugar?
# 17. Conseguimos saber onde estão localizados os imóveis pelo seu tipo, apenas para os imóveis disponível para alugar?

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
print(string_media_aluguel)

# Valor minimo dos alugueis
min_aluguel = min(precos_alugueis)
string_min_aluguel = f'O valor minimo dos alugueis na cidade de Nova Yorque é ${min_aluguel:.2f}'
print(string_min_aluguel)

# Valor maximo dos alugueis
max_aluguel = max(precos_alugueis)
string_max_aluguel = f'O valor maximo dos alugueis na cidade de Nova Yorque é ${max_aluguel:.2f}'
print(string_max_aluguel)

# 3. Quais os nomes das regiões que existem na cidade de Nova York?
# Pegar as regiôes distintas de NY
regiao = df.loc[:, 'neighbourhood_group']
regiao = pd.unique(regiao)
regiao_str = ', '.join(r for r in regiao)
string_saida_regiao = f'As regiões de Nova Yorque são: {regiao_str}.'
print(string_saida_regiao)

# 4. Quais são as categorias de imóveis que estão cadastradas dentro da base de dados da cidade de Nova York?
categ_imoveis = df.loc[:, 'room_type']
categ_imoveis = pd.unique(categ_imoveis)
categ_imoveis_str = ', '.join(ci for ci in categ_imoveis)
string_saida_categ_imoveis = f'As categorias de imóveis de Nova Yorque são: {categ_imoveis_str}.'
print(string_saida_categ_imoveis)

# 5. Quantos usuários (Hosts) únicos cadastrados existem dentro da base de dados da cidade de Nova York?
hosts = df.loc[:, 'host_id']
quant_hosts_unicos = len(pd.unique(hosts))
string_saida_hosts = f'Há em Nova Yorque {quant_hosts_unicos} usuários (Hosts) únicos.'
print(string_saida_hosts)

# 6. Como é a variação dos preços dos imóveis em NY?
desvio_padrao_alugueis = np.std(precos_alugueis)
string_desvio_padrao_alugueis = f'O valor da variação dos alugueis na cidade de Nova Yorque é ${desvio_padrao_alugueis:.2f}'
print(string_desvio_padrao_alugueis)

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
print(string_caros_baratos)

# 7. Com Histograma:

# linhas = df.loc[:, 'price'] < 1100
# preco_hist = df.loc[linhas, 'price']
# plt.hist(preco_hist, bins=11)
# plt.show()

# 8. Qual a distribuição do número de Reviews? Existem imóveis com muitos e outro com poucos reviews?
# linhas = df.loc[:, 'number_of_reviews'] < 600
# reviwes = df.loc[linhas, 'number_of_reviews']
# plt.hist(reviwes, bins=30)
# plt.show()

# 9. Qual a distribuição dos imóveis de acordo com o número mínimo de pernoites que podem ser agendado?

# linhas = df.loc[:, 'minimum_nights'] < 100
# df_plot = df.loc[linhas, 'minimum_nights']
# plt.hist( df_plot, bins=20 )
# plt.show()

# 10. Qual a média e a mediana de imóveis cadastrado por host (dono do imóvel)?

media = df.loc[:, 'calculated_host_listings_count'].mean()
median = df.loc[:, 'calculated_host_listings_count'].median()
print(f'A media de imoveis cadastrados é {media:.2f}')
print(f'A mediana de imoveis cadastrados é {median:.2f}')

# 11. Qual a data mais recente da última avaliação

avaliacoes = df.loc[:, 'last_review'].sort_values(ascending=True)
data_recente = avaliacoes.loc[317]
print(f'A data mais recente das avaliacoes é: {data_recente}')

# 12. Qual o valor máximo de pernoites agendadas?

maximo_pernoite = df.loc[:, 'minimum_nights'].max()
print(f'O valor maximo de pernoite é de {maximo_pernoite}')

# 13. Quantos nomes de donos de imóveis são únicos?

hosts = df.loc[:, 'host_id']
host_id_unicos = len(np.unique(hosts))
print(f'O numero de hosts únicos: {host_id_unicos}')

# 14. Quanto identificadores únicos existem na base de dados?

id = df.loc[:, 'id']
id_unicos = len(np.unique(id))
print(f'O número de IDs únicos: {id_unicos}')

# 15. Qual é o valor do aluguel (diária) mais caro de cada região da base de dados da cidade de Nova York, apenas para os imóveis disponível para alugar?

colunas = ['neighbourhood_group', 'price']
colunas_groupby = ['neighbourhood_group']
linhas = df.loc[:, 'availability_365'] != 0
df_agrup = df.loc[linhas, colunas].groupby(colunas_groupby)
df_plot = df_agrup.max().reset_index()
print(df_plot)
graf = px.bar(df_plot, x='neighbourhood_group', y='price')
# graf.show()

# 16. Conseguimos saber onde estão localizados os imóveis com o valor do aluguel mais caro, na cidade de Nova York, apenas para os imóveis disponível para alugar?

colunas = ['neighbourhood_group', 'price', 'latitude', 'longitude']
colunas_groupby = ['neighbourhood_group']
df_agrup = df.loc[:, colunas].groupby(colunas_groupby).max().reset_index()
mapa = folium.Figure()
map = folium.Map(location=[df_agrup['latitude'].mean(), df_agrup['longitude'].mean()], zoom_start=14, control_scale=True)

for index, location_info in df_agrup.iterrows():
    folium.Marker([location_info['latitude'], location_info['longitude']],
                  popup=location_info['neighbourhood_group']).add_to(map)
map.show_in_browser()

# 17. Conseguimos saber onde estão localizados os imóveis pelo seu tipo, apenas para os imóveis disponível para alugar?

colunas = ['neighbourhood_group', 'room_type', 'latitude', 'longitude']
df_plot = df.loc[:, colunas].sample(100)

df_plot.loc[:, 'color'] = 'NA'

linhas_private_room = df_plot.loc[:, 'room_type'] == 'Private room'
linhas_entire_apt = df_plot.loc[:, 'room_type'] == 'Entire home/apt'
linhas_shared_room = df_plot.loc[:, 'room_type'] == 'Shared room'

df_plot.loc[linhas_private_room, 'color'] = 'darkgreen'
df_plot.loc[linhas_entire_apt, 'color'] = 'darkred'
df_plot.loc[linhas_shared_room, 'color'] = 'purple'

map = folium.Map()
for index, location_info in df_plot.iterrows():
    folium.Marker([location_info['latitude'], location_info['longitude']],
                  popup=location_info[['neighbourhood_group', 'room_type']],
                  icon=folium.Icon( color=location_info['color'] )).add_to(map)
map.show_in_browser()

