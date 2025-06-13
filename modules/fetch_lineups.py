def display_lineups(sport):
    import streamlit as st
    st.subheader(f'{sport.capitalize()} 出场球员名单')
    st.write('（出场球员监听模块）')