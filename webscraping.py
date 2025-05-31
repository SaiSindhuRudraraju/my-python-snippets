import requests
from bs4 import BeautifulSoup
import pandas as pd
import streamlit as st

def scrape_website(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        data = []
        for item in soup.find_all('article', class_='product_pod'):
            title = item.h3.a['title']
            price = item.find('p', class_ = 'price_color').text
            data.append({'title': title, 'price': price})
        return pd.DataFrame(data)
    else:
        print(f"Failed to retrive data from {url}")
        return None
    
def main():
    st.title("Web Scraping Example")
    url = st.text_input("Enter the URL to scrape:", "https://books.toscrape.com/")
    if st.button("Scrape"):
        df = scrape_website(url)
        if df is not None:
            st.write(df)
            st.download_button(label="Download CSV", data=df.to_csv(index=False), file_name='scraped_data.csv', mime='text/csv')
        else:
            st.error("Failed to scrape data.")

if __name__ == "__main__":
    main()