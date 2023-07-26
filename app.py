import streamlit as st
from src.coinmarketcap_connector import CoinMarketCapConnection
import polars as pl

# Create an instance of the connection
cmc_conn = CoinMarketCapConnection(connection_name="cmc_connection")

def main():
    st.title("CoinMarketCap Explorer")

    # Add a button to fetch data
    if st.button("Fetch Top 10 Cryptocurrencies"):
        # Fetch the latest data of top 10 cryptocurrencies
        data = cmc_conn.fetch_latest_data(limit=10)

        # Convert JSON data to polars DataFrame
        df = pl.DataFrame(data["data"])

        # Display the DataFrame in Streamlit
        st.write(df)

        # You can add more interactive elements below, like charts, filters, etc.
        # ...

if __name__ == '__main__':
    main()
