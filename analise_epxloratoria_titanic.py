import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('titanic.csv')

print(df.head())
print(df.info())
print(df.describe())
print(df['Survived'].value_counts())
sns.countplot(x='Survived', data=df)
plt.title('Sobreviventes (0 = Não, 1 = Sim)')
plt.show()

sns.countplot(x='Survived', hue='Sex', data=df)
plt.title('Sobreviventes por Gênero')
plt.show()

sns.histplot(df['Age'].dropna(), bins=30)
plt.title('Distribuição de Idades dos Passageiros')
plt.show()

sns.scatterplot(x='Age', y='Fare', hue='Survived', data=df)
plt.title('Idade vs. Tarifa dos Passageiros')
plt.show()

correlation = df.corr()
print(correlation)