import streamlit as st
from src.coinmarketcap_connector import CoinMarketCapConnection

# Create an instance of the connection
cmc_conn = CoinMarketCapConnection()

def main():
    st.title("CoinMarketCap Explorer")
    
    # For demonstration: Let's fetch the latest data of top 10 cryptocurrencies
    data = cmc_conn.fetch_latest_data(limit=10)
    st.write(data)

    # You can add more functionality, like searching, viewing historical data, etc.

if __name__ == '__main__':
    main()