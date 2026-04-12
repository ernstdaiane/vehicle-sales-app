# Vehicle Sales App

Este projeto é um aplicativo web desenvolvido com Streamlit para análise de anúncios de venda de carros.

## Funcionalidades

- Exibe um cabeçalho com descrição do projeto
- Gera um histograma da coluna `odometer`
- Gera um gráfico de dispersão entre `odometer` e `price`
- Permite interação por meio de botões

## Tecnologias utilizadas

- Python
- Pandas
- Plotly Express
- Streamlit

## Estrutura do projeto

- `app.py`: aplicativo web
- `vehicles_us.csv`: conjunto de dados
- `requirements.txt`: dependências do projeto
- `notebooks/EDA.ipynb`: análise exploratória de dados
- `.streamlit/config.toml`: configuração para deploy

## Como executar localmente

```bash
streamlit run app.py
