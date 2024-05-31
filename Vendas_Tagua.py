import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Ler a planilha
caminho_arquivo = 'abril_para_pandas.xlsx'
df = pd.read_excel(caminho_arquivo, engine='openpyxl')

# Converter a coluna de data e hora para o tipo datetime
df['Data Venda'] = pd.to_datetime(df['Data Venda'])

# Total de vendas por dia
vendas_por_dia = df.groupby(df['Data Venda'].dt.date)['Valor Recebido'].sum().reset_index()

# Total de vendas por tipo de venda
vendas_por_tipo = df.groupby('Tipo Operação')['Valor Recebido'].sum().reset_index()

# Total de vendas por forma de recebimento
vendas_por_forma = df.groupby('forma_recebimento')['Valor Recebido'].sum().reset_index()

# Total de vendas por hora para cada tipo de venda
vendas_por_hora_tipo = df.groupby([df['Data Venda'].dt.hour, 'Tipo Operação'])['Valor Recebido'].sum().reset_index()

# Título do app
st.title('Dashboard de Vendas')

# Gráfico de vendas por dia
st.subheader('Total de Vendas por Dia')
st.line_chart(data=vendas_por_dia.set_index('Data Venda'))

# Gráfico de vendas por tipo de venda
st.subheader('Total de Vendas por Tipo de Venda')
fig, ax = plt.subplots()
sns.barplot(data=vendas_por_tipo, x='Tipo Operação', y='Valor Recebido', ax=ax)
st.pyplot(fig)

# Gráfico de vendas por forma de recebimento
st.subheader('Total de Vendas por Forma de Recebimento')
fig, ax = plt.subplots()
sns.barplot(data=vendas_por_forma, x='forma_recebimento', y='Valor Recebido', ax=ax)
st.pyplot(fig)

# Gráfico de vendas por hora para cada tipo de venda
st.subheader('Total de Vendas por Hora para Cada Tipo de Venda')
fig, ax = plt.subplots()
sns.lineplot(data=vendas_por_hora_tipo, x='Data Venda', y='Valor Recebido', hue='Tipo Operação', ax=ax)
st.pyplot(fig)