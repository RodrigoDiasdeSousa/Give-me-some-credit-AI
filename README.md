# Give Me Some Credit - Modelo de Previsão de Inadimplência

Este projeto tem como objetivo **prever clientes que podem se tornar inadimplentes nos próximos 2 anos**, baseado no dataset “Give Me Some Credit” do Kaggle.

Crie e ative o ambiente virtual:

python -m venv .venv
.\.venv\Scripts\activate 

Instale os pacotes:

pip install -r requirements.txt


Abra o notebook e execute as células:

jupyter notebook notebooks/notebook.ipynb]

Modelo usado: Regressão Logística

Valores ausentes preenchidos com a mediana (MonthlyIncome, NumberOfDependents)

Features escalonadas com StandardScaler

Classe alvo: SeriousDlqin2yrs (inadimplência em 2 anos)

Threshold ajustado: 0.75 (para priorizar recall da classe 1, inadimplentes)

Próximos Passos

Testar modelos mais sofisticados (RandomForest, XGBoost)

Criar features derivadas (ex: razões, combinações de dívidas, idade vs crédito)

Ajustar threshold de acordo com estratégia de negócio

