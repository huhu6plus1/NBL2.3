
import streamlit as st
import pandas as pd
import json
import os

st.set_page_config(page_title="NBL + NZ NBL 自动推荐系统 v2.3", layout="wide")

st.title("🏀 NBL1 + NZ NBL 自动EV监听系统 v2.3")
st.markdown("🟢 自动推荐 + EV计算 + 推送 + 出场监听 + 多平台盘口抓取 + 首开球 & 罚牌推荐")

# 1. 推荐记录展示
st.subheader("📋 最近推荐记录（EV ≥ 5%）")
if os.path.exists("logs/recommendations.jsonl"):
    with open("logs/recommendations.jsonl", "r") as f:
        records = [json.loads(line) for line in f.readlines()]
    df = pd.DataFrame(records)
    if not df.empty:
        df = df.sort_values("timestamp", ascending=False)
        st.dataframe(df)
    else:
        st.info("暂无推荐记录")
else:
    st.warning("推荐记录文件不存在")

# 2. 多平台盘口抓取展示
st.subheader("📈 实时盘口抓取与多平台推荐对比")
multi_path = "data/multi_odds.json"
if os.path.exists(multi_path):
    with open(multi_path, "r") as f:
        multi_odds = json.load(f)
    if isinstance(multi_odds, list) and len(multi_odds) > 0:
        df_multi = pd.json_normalize(multi_odds)
        st.dataframe(df_multi)
    else:
        st.info("暂无多平台盘口数据")
else:
    st.warning("多平台盘口数据未抓取")

# 3. 出场名单监听状态
st.subheader("🧷 出场名单监听状态")
lineup_path = "data/lineups.json"
if os.path.exists(lineup_path):
    with open(lineup_path, "r") as f:
        lineups = json.load(f)
    df_lineup = pd.json_normalize(lineups)
    st.dataframe(df_lineup)
else:
    st.info("暂无出场名单监听数据")

# 4. 足球推荐（首开球、罚牌、角球、大小球、让分）
st.subheader("⚽ 足球推荐展示")
football_path = "data/football_recommendations.json"
if os.path.exists(football_path):
    with open(football_path, "r") as f:
        football = json.load(f)
    if isinstance(football, list) and len(football) > 0:
        df_football = pd.DataFrame(football)
        df_football = df_football[df_football["ev"] >= 5.0]
        st.dataframe(df_football)
    else:
        st.info("暂无足球推荐")
else:
    st.warning("未抓取足球推荐数据")

# 5. 上传截图分析（保留接口）
st.sidebar.header("📤 上传盘口截图分析")
st.sidebar.info("开发中：可上传截图进行自动识别与推荐分析")
