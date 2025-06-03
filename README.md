# 📊 Analyse de la corrélation entre crypto-actifs et actions technologiques (2020–2024)

---

## 🧠 Présentation

Ce projet explore les relations financières entre les cryptomonnaies (Bitcoin, Ethereum) et des actions technologiques majeures (Nvidia, Tesla, Coinbase) sur la période 2020–2024.

L’objectif est d’analyser la **corrélation entre ces actifs innovants**, d’en observer l’évolution dans le temps, et d’identifier les différences de comportement selon les contextes de marché (Bull vs Bear).

---

## 🎯 Objectifs de l’étude

- 📈 Mesurer la relation entre BTC/ETH et les actions tech
- 🔍 Identifier les périodes de corrélation/décorrélation
- 🐂🐻 Analyser les dynamiques selon les phases de marché (Bull vs Bear)
- 🧪 Réaliser des tests statistiques (test t de Student)
- 📉 Modéliser les tendances via des régressions linéaires
- 🧠 Regrouper les actifs avec du clustering non supervisé (KMeans + PCA)

---

## 🛠️ Technologies utilisées

- Python (Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, Scipy)
- yFinance pour l’extraction des données financières
- Google Colab pour l’exécution du notebook
- GitHub pour l’hébergement du projet

---

## 📁 Structure du projet

```
📦 Crypto-Tech-Correlation-Analysis
 ┣ 📁 figures/           → Graphiques générés
 ┣ 📓 notebook.ipynb      → Analyse complète sur Google Colab
 ┣ 📑 presentation.pdf    → Présentation académique finale (21 slides)
 ┣ 📑 presentation.pptx   → Version modifiable PowerPoint
 ┗ 📄 README.md           → Description du projet
```

---

## 🚀 Exécution du projet

1. **Cloner le dépôt** :
```bash
git clone https://github.com/yanis-allamigeon/Crypto-Tech-Correlation-Analysis.git
```

2. **Ouvrir le notebook sur Google Colab**  
Lien : [Notebook Colab](https://colab.research.google.com/drive/1AaeHV-F3WGE5O1hNjSKthJAQKoesqr5a)

3. **Exécuter les cellules** pour reproduire l’analyse, les tests statistiques et les visualisations.

---

## 📄 Résultats clés

- Corrélations fortes entre BTC–COIN ; modérées et variables entre BTC–NVDA et ETH–NVDA
- Corrélations plus élevées en **marché baissier** que haussier (confirmé par tests t)
- Les régressions montrent des tendances différentes selon les actifs
- Le **clustering** révèle une structure en deux univers : crypto et tech

---

## 🧭 Pour aller plus loin

- Étendre l’échantillon à d’autres cryptos (BNB, SOL…) et entreprises tech (Meta, Apple…)
- Intégrer des événements macroéconomiques (inflation, taux directeur…)
- Appliquer des modèles prédictifs plus complexes (réseaux de neurones, LSTM)

---

## 👨‍🎓 Auteur

**Yanis Allamigeon**  
Licence 1 Économie – Université de Montpellier (Parcours International)  
Mars 2025

📧 yanisallamigeon92@gmail.com

---

## 📜 Licence

Projet open-source sous licence MIT
