# data_extraction.py

"""
Script pour extraire les données financières des actifs via yfinance.
"""

import yfinance as yf

def fetch_data(ticker, start="2020-01-01", end="2024-01-01"):
    """
    Télécharge les données historiques pour un ticker donné.
    
    Args:
        ticker (str): Symbole de l'actif (ex: 'BTC-USD', 'TSLA').
        start (str): Date de début (YYYY-MM-DD).
        end (str): Date de fin (YYYY-MM-DD).
    
    Returns:
        pandas.DataFrame: Données historiques de l'actif.
    """
    return yf.download(ticker, start=start, end=end)

if __name__ == "__main__":
    # Exemple d'extraction
    df = fetch_data("BTC-USD")
    print(df.head())

