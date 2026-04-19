import streamlit as st
import time

# --- 頁面設定 ---
st.set_page_config(page_title="指揮助手", page_icon="🎼")

st.title("🎼 指揮助手")

# --- 1. 音樂術語翻譯功能 ---
st.header("🔍 術語翻譯")
dict_music = {
    "Lento": "慢板 (約 40-60 BPM)，通常帶有沉重感。",
    "Adagio": "柔板 (約 66-76 BPM)，優雅緩慢。",
    "Andante": "行板 (約 76-108 BPM)，如步行般的速度。",
    "Moderato": "中板 (約 108-120 BPM)。",
    "Allegro": "快板 (約 120-168 BPM)，活潑快速。",
    "Presto": "急板 (約 168-200 BPM)。",
    "Ritardando (rit.)": "漸慢。",
    "Accelerando (accel.)": "漸快。",
    "A tempo": "回到原速。",
}

search = st.selectbox("選擇或輸入術語：", list(dict_music.keys()))
st.info(f"**解釋：** {dict_music.get(search)}")

# 分隔線
st.markdown("---")

# --- 2. 視覺拍子機功能 ---
st.header("🥁 視覺拍子機")
bpm = st.slider("調整 BPM (每分鐘拍數)", min_value=40, max_value=208, value=100)

if st.button("開始 / 停止跳動"):
    st.write(f"正在以 {bpm} BPM 運行...")
    sleep_time = 60 / bpm
    
    # 視覺閃爍效果
    placeholder = st.empty()
    while True: # 持續運行
        placeholder.markdown(f"<h1 style='text-align: center; color: #FF4B4B; font-size: 100px;'>●</h1>", unsafe_allow_html=True)
        time.sleep(sleep_time / 2)
        placeholder.markdown(f"<h1 style='text-align: center; color: #E0E0E0; font-size: 100px;'>○</h1>", unsafe_allow_html=True)
        time.sleep(sleep_time / 2)
