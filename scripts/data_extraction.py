 # data_extraction.py

"""
Script pour extraire les données financières des actifs via yfinance.
"""

import yfinance as yf
import pandas as pd
import os

def fetch_data(tickers, start="2020-01-01", end="2024-01-01"):
    """
    Télécharge les données historiques pour plusieurs actifs.

    Args:
        tickers (list): Liste des symboles des actifs (ex: ['BTC-USD', 'TSLA']).
        start (str): Date de début (YYYY-MM-DD).
        end (str): Date de fin (YYYY-MM-DD).

    Returns:
        pandas.DataFrame: Données historiques des actifs.
    """
    data = yf.download(tickers, start=start, end=end)
    return data

if __name__ == "__main__":
    # Liste des actifs à récupérer
    assets = ["BTC-USD", "ETH-USD", "NVDA", "TSLA", "COIN"]

    # Extraction des données
    df = fetch_data(assets)

    # Vérifier que le dossier 'data/' existe, sinon le créer
    os.makedirs("../data", exist_ok=True)

    # Sauvegarde en CSV
    df.to_csv("../data/market_data.csv")

    print("Données téléchargées et enregistrées dans data/market_data.csv")

