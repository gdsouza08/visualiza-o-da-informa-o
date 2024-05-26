## gráfico de barras
import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv('censo.csv')

x = dados['ano']
y = dados['populacao']

plt.bar(x , y, color='silver')
plt.plot(x, y, color='black', linestyle='--')

plt.xlabel('Ano')
plt.ylabel('População x 100.000.000')

plt.title('Censo da População Brasileira de 1991 até 2022')

plt.show()

## gráfico scatter
import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv('censo.csv')

x = dados['populacao']
y = dados['ano']
plt.scatter(x, y)

plt.show()

## gráfico de linhas
import pandas as pd
import matplotlib.pyplot as plt

series = pd.read_csv('censo.csv')


series.plot('ano', 'populacao')

plt.xlabel('Ano')
plt.ylabel('População x 100.000.000')

plt.title('Censo da População Brasileira de 1991 até 2022')

plt.show()