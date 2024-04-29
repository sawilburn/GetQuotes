import requests

# Replace 'YOUR_API_KEY' with your actual Alpha Vantage API key

API_KEY = '18P2ZFL1GQIN0S59'

# Function to fetch historical stock data
def get_stock_data(symbol, api_key):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f'Failed to fetch data. Status code: {response.status_code}')
        return None

# Example usage
if __name__ == "__main__":
    symbol = 'MSFT'  # Microsoft stock symbol
    stock_data = get_stock_data(symbol, API_KEY)
    if stock_data:
        # Process and use the retrieved data here
        print(stock_data)


