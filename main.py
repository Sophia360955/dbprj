# streamlit_app.py

import streamlit as st

# Initialize connection.
conn = st.connection('mysql', type='sql')

# Perform query.
df = conn.query('SELECT * from bookings;', ttl=600)

st.write(df)