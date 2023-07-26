import streamlit as st
from src.coinmarketcap_connector import CoinMarketCapConnection
import polars as pl

# Create an instance of the connection
cmc_conn = CoinMarketCapConnection(connection_name="cmc_connection")

def main():
    st.title("CoinMarketCap Explorer")
    
    # Sidebar with functionalities
    st.sidebar.header("Functions")
    
    # Fetch latest data
    if st.sidebar.button("Fetch Top 10 Cryptocurrencies"):
        data = cmc_conn.fetch_latest_data(limit=10)
        df = pl.DataFrame(data["data"])
        st.write(df)
    
    # Search for cryptocurrencies
    keyword = st.sidebar.text_input("Search Cryptocurrencies:")
    if keyword and st.sidebar.button("Search"):
        data = cmc_conn.search_cryptocurrencies(keyword)
        df = pl.DataFrame(data["data"])
        st.write(df)
    
    # Fetch historical data
    st.sidebar.subheader("Fetch Historical Data")
    crypto_id = st.sidebar.text_input("Cryptocurrency ID:")
    start_date = st.sidebar.date_input("Start Date")
    end_date = st.sidebar.date_input("End Date")
    if crypto_id and st.sidebar.button("Fetch Historical Data"):
        data = cmc_conn.fetch_historical_data(crypto_id, start_date, end_date)
        df = pl.DataFrame(data["data"])
        st.write(df)

if __name__ == '__main__':
    main()
