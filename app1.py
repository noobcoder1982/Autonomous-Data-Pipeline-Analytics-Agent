
import streamlit as st
from langchain_community.utilities import SQLDatabase

st.title("AI Data Agent - Day 2")

db = SQLDatabase.from_uri("duckdb:///threedatasets.db")

if st.button("Show Tables"):
    st.write(db.get_usable_table_names())

if st.button("Show Schema"):
    st.text(db.get_table_info())
