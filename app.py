import streamlit as st
import time

# --- 頁面設定 ---
st.set_page_config(page_title="指揮助手", page_icon="🎼")

st.title("🎼 指揮助手：拍子機與術語翻譯")

# --- 1. 音樂術語翻譯功能 ---
st.header("🔍 術語翻譯")
dict_music = {
    "Lento": "慢板 (每分鐘約 40-60 拍)，通常帶有沉重感。",
    "Adagio": "柔板 (每分鐘約 66-76 拍)，優雅緩慢。",
    "Andante": "行板 (每分鐘約 76-108 拍)，如步行般的速度。",
    "Moderato": "中板 (每分鐘約 108-120 拍)。",
    "Allegro": "快板 (每分鐘約 120-168 拍)，活潑快速。",
    "Presto": "急板 (每分鐘約 168-200 拍)。",
    "Ritardando (rit.)": "漸慢。",
    "Accelerando (accel.)": "漸快。",
    "A tempo": "回到原速。",
}

search = st.selectbox("選擇或輸入術語：", list(dict_music.keys()))
st.info(f"**解釋：** {dict_music.get(search)}")

---

# --- 2. 視覺拍子機功能 ---
st.header("🥁 視覺拍子機")
bpm = st.slider("調整 BPM (每分鐘拍數)", min_value=40, max_value=208, value=100)

if st.button("開始跳動"):
    st.write(f"正在以 {bpm} BPM 運行...")
    sleep_time = 60 / bpm
    
    # 簡單的視覺閃爍效果
    placeholder = st.empty()
    for i in range(100):  # 預設跑 100 次
        placeholder.markdown(f"<h1 style='text-align: center; color: red;'>●</h1>", unsafe_allow_html=True)
        time.sleep(sleep_time / 2)
        placeholder.markdown(f"<h1 style='text-align: center; color: gray;'>○</h1>", unsafe_allow_html=True)
        time.sleep(sleep_time / 2)
