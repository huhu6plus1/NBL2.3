def display_odds(sport):
    import streamlit as st
    st.subheader(f'{sport.capitalize()} 实时盘口')
    st.write('（TAB盘口抓取展示模块）')