# modules/parse_bhavcopy.py
import pandas as pd

def parse_bhavcopy(file_path):
    """
    Parses the bhavcopy CSV file and calculates the Fibonacci levels for each stock.
    Returns a DataFrame with stock symbol, high, low, close, and Fibonacci levels.
    """
    df = pd.read_csv(file_path)
    
    # Extract relevant columns
    df = df[['TckrSymb', 'HghPric', 'LwPric', 'ClsPric']]
    df.columns = ['symbol', 'high', 'low', 'close']
    
    # Calculate Fibonacci levels
    levels = [4.236, 6.84, 11.08]
    for level in levels:
        df[f'fib_up_{level}'] = (df['high'] - df['low']) * level + df['low']
        df[f'fib_down_{level}'] = (df['high'] - df['low']) * level - df['high']
    
    print("Parsed bhavcopy and calculated Fibonacci levels.")
    return df
