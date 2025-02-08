# modules/check_levels.py
import pandas as pd

def check_fibonacci_levels(df):
    """
    Checks if the high, low, or close price is within ±3% of any Fibonacci level.
    Returns a list of stocks that qualify.
    """
    qualifying_stocks = []
    
    for index, row in df.iterrows():
        symbol = row['symbol']
        prices = [row['high'], row['low'], row['close']]
        
        for level in [4.236, 6.84, 11.08]:
            upper_level = row[f'fib_up_{level}']
            lower_level = row[f'fib_down_{level}']
            
            for price in prices:
                # Check for ±3% proximity
                if upper_level * 0.97 <= price <= upper_level * 1.03:
                    qualifying_stocks.append({
                        "symbol": symbol,
                        "level": f"Up {level}",
                        "price": price,
                        "fibonacci_level": upper_level
                    })
                if lower_level * 0.97 <= price <= lower_level * 1.03:
                    qualifying_stocks.append({
                        "symbol": symbol,
                        "level": f"Down {level}",
                        "price": price,
                        "fibonacci_level": lower_level
                    })
    
    print(f"Found {len(qualifying_stocks)} stocks near Fibonacci levels.")
    return qualifying_stocks
