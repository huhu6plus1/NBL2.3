def display_recommendations(sport):
    import streamlit as st
    st.subheader(f'{sport.capitalize()} 微信推荐记录')
    st.write('（推荐记录模块）')