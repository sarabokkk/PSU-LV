import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Učitavanje skupa podataka
mtcars = pd.read_csv('mtcars.csv')

# 1. Barplot koji prikazuje potrošnju (mpg) automobila s 4, 6 i 8 cilindara
plt.figure(figsize=(10, 6))
sns.barplot(x='cyl', y='mpg', data=mtcars, estimator=sum, ci=None, palette="Blues_d")
plt.title('Potrošnja (MPG) automobila s 4, 6 i 8 cilindara')
plt.xlabel('Broj cilindara')
plt.ylabel('Ukupna potrošnja (sum of mpg)')
plt.show()

# 2. Boxplot koji prikazuje distribuciju težine (wt) automobila s 4, 6 i 8 cilindara
plt.figure(figsize=(10, 6))
sns.boxplot(x='cyl', y='wt', data=mtcars, palette="Set2")
plt.title('Distribucija težine (WT) automobila s 4, 6 i 8 cilindara')
plt.xlabel('Broj cilindara')
plt.ylabel('Težina (u hiljadama funti)')
plt.show()

# 3. Scatter plot koji prikazuje odnos između potrošnje i vrste mjenjača (ručni vs automatski)
plt.figure(figsize=(10, 6))
sns.boxplot(x='am', y='mpg', data=mtcars, palette="Set1")
plt.title('Poređenje potrošnje automobila sa ručnim i automatskim mjenjačem')
plt.xlabel('Vrsta mjenjača (0 = automatski, 1 = ručni)')
plt.ylabel('Potrošnja (MPG)')
plt.show()

# 4. Scatter plot koji prikazuje odnos ubrzanja (qsec) i snage (hp) za automobile s ručnim i automatskim mjenjačem
plt.figure(figsize=(10, 6))
sns.scatterplot(x='qsec', y='hp', hue='am', data=mtcars, palette="coolwarm", s=100)
plt.title('Odnos ubrzanja i snage automobila s ručnim i automatskim mjenjačem')
plt.xlabel('Ubrzanje (qsec)')
plt.ylabel('Snaga (HP)')
plt.legend(title='Vrsta mjenjača', labels=['Automatski', 'Ručni'])
plt.show()
