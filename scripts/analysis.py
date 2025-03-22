import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Charger les données
df = pd.read_csv("../data/market_data.csv", index_col=0, parse_dates=True)

# Calcul de la matrice de corrélation
correlation_matrix = df.corr()

# Visualisation
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Matrice de corrélation entre BTC, ETH et les actions tech")
plt.show()
