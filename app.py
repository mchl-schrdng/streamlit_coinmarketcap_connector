import streamlit as st
from src.coinmarketcap_connector import CoinMarketCapConnection
import polars as pl

# Create an instance of the connection
cmc_conn = CoinMarketCapConnection(connection_name="cmc_connection")

def main():
    st.title("CoinMarketCap Explorer")
    
    # Fetch the latest data of top 10 cryptocurrencies
    data = cmc_conn.fetch_latest_data(limit=10)

    # Convert JSON data to polars DataFrame
    df = pl.DataFrame(data["data"])

    # Display the DataFrame in Streamlit
    st.write(df)

    # Add any other functionality you wish, such as filtering, searching, etc.

if __name__ == '__main__':
    main()
