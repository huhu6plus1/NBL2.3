def display_matches(sport):
    import streamlit as st
    st.subheader(f'{sport.capitalize()} 今日比赛')
    st.write('（比赛抓取模块待接入真实数据源）')