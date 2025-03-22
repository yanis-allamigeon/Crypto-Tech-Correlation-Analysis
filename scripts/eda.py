# eda.py

"""
Analyse exploratoire des données extraites (Crypto et actions Tech).
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Charger les données
file_path = "data/market_data.csv"
if not os.path.exists(file_path):
    raise FileNotFoundError(f"Le fichier {file_path} n'existe pas. Exécutez data_extraction.py d'abord.")

df = pd.read_csv(file_path, index_col=0, parse_dates=True)

# Affichage des premières lignes
print(df.head())

# Supprimer les colonnes inutiles
df = df["Adj Close"]

# Vérifier les valeurs manquantes
print("\nValeurs manquantes :")
print(df.isnull().sum())

# Remplir les valeurs manquantes avec une interpolation
df.interpolate(method='linear', inplace=True)

# Affichage de la corrélation
correlation_matrix = df.corr()
print("\nMatrice de corrélation :")
print(correlation_matrix)

# Affichage des prix des actifs
plt.figure(figsize=(12, 6))
df.plot(title="Évolution des prix des actifs (2020-2024)")
plt.xlabel("Date")
plt.ylabel("Prix ($)")
plt.legend(df.columns)
plt.grid()
plt.show()

# Heatmap des corrélations
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Matrice de corrélation des actifs")
plt.show()
