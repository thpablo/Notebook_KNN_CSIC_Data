import pandas as pd


data_url = './csicFinal.csv'
data = pd.read_csv(data_url)


for var in data.columns:
    print(data[var].value_counts())
    print("-----------------")

print(data.info())

# Drop de colunas contem os mesmos valores (redundantes)
redundant_columns = ['Pragma', 'Host-Header', 'Connection', 'Accept', 'Accept-Charset', 'Accept-Language', 'Cache-control']

for var in redundant_columns:
    data.drop(var, axis = 1, inplace = True)

print(data.info())


# Conversao variaveis categoricas em numericas (dummies) para
# Valores 'binarios'

conversion_class = pd.get_dummies(data['Class'])

display(conversion_class)
