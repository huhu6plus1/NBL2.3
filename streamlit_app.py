
import streamlit as st
from modules.fetch_matches import display_matches
from modules.fetch_lineups import display_lineups
from modules.scrape_tab_odds import display_odds
from modules.ocr_analysis import upload_and_analyze_image
from modules.roi_plot import show_roi_plot
from modules.recommendation_log import display_recommendations

st.set_page_config(layout="wide", page_title="投注分析系统 v2.3")

tabs = st.tabs(["🏀 篮球", "⚽ 足球"])

with tabs[0]:
    st.header("🏀 篮球推荐系统")
    display_matches("basketball")
    display_lineups("basketball")
    display_odds("basketball")
    upload_and_analyze_image("basketball")
    display_recommendations("basketball")
    show_roi_plot("basketball")

with tabs[1]:
    st.header("⚽ 足球推荐系统")
    display_matches("football")
    display_lineups("football")
    display_odds("football")
    upload_and_analyze_image("football")
    display_recommendations("football")
    show_roi_plot("football")
