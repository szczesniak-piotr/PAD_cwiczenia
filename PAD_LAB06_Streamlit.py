import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import time

st.title("Streamlit praca domowa")



page = st.selectbox('Wybierz stronę', ['Ankieta', 'Staty'])

if page == 'Ankieta':

    firstname = st.text_input('Podaj swoje imię', 'Wpisz tutaj...')
    lastname = st.text_input('Podaj swoje nazwisko', 'Wpisz tutaj...')
    if st.button("Zatwierdź"):
        result = firstname.title()
        st.success('Zatwierdzono')
else:

    data = st.file_uploader('Wgraj swój dataframe', type=['csv'])
    if data is not None:
        with st.spinner('Proszę czekać...'):
            time.sleep(3)
        st.success('Wczytano pomyślnie')
        df = pd.read_csv(data)
        st.dataframe(df.head(10))
        all_columns_names = df.columns.to_list()
        selected_columns_name = st.selectbox('Wybierz kolumnę do wyświetlenia', ['tshirt_quantity', 'pages_visited'])
        st.bar_chart(data=df, x='order_date', y=selected_columns_name)
    else:
        st.error('wczytaj inny df')
