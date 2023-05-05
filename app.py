import streamlit as st
import pandas as pd
st.title("Product Competitor Analyzer")
st.write("This app scrapes and gathers datasets on selected products into a database and performs analyses")

form = st.form(key='my-form')
name = form.text_input('Enter your Company Name')
shops = form.multiselect("Choose Shops",["Amazon", "Ebay",  "Walmart", "OnBuy"])
product_type = form.selectbox('Select Product Type', ['jacket','laptops','books', 'video games', 'watches','shoes','cups','shirts'], key=1) # lowercase
num_pages = int(form.number_input('Enter the number of pages to crawl'))

submit = form.form_submit_button('Gather Data')


if submit:
    st.write(f'Welcome {name}')
    st.write(f'You have selected data on {product_type} to be scraped from the ff shops {shops}')
 
    
    f = open("stream-inputs.txt", "w")
    f.write(str(name)+ "," +str(num_pages)+ "," + str(shops) + "," + str(product_type))
    f.close()
    
    data = pd.read_csv("amazon_"+product_type+"_products.csv")
    st.dataframe(data)
    
# view_data = st.button('View Data')  
# if view_data:
#     amazon_data = generateAmazonProductDataset(num_pages,str(product_type).lower())
#     st.dataframe(amazon_data)
    
