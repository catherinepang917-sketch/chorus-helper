import streamlit as st
import streamlit.components.v1 as components

# --- 頁面設定 ---
st.set_page_config(page_title="指揮助手 Pro", page_icon="🎼")

st.title("🎼 指揮助手 (含音效版)")

# --- 1. 音樂術語翻譯 ---
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

st.markdown("---")

# --- 2. 聲畫同步拍子機 ---
st.header("🥁 聲畫拍子機")
bpm = st.slider("調整 BPM", min_value=40, max_value=208, value=100)

# 使用 HTML/JS 處理聲音，這能確保節拍精準且不會有網路延遲
metronome_html = f"""
<div style="text-align: center;">
    <button id="startBtn" style="padding: 15px 30px; font-size: 20px; background-color: #FF4B4B; color: white; border: none; border-radius: 10px; cursor: pointer;">
        開始 / 停止
    </button>
    <h1 id="visual" style="font-size: 100px; color: #E0E0E0;">○</h1>
</div>

<script>
    var audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    var isRunning = false;
    var intervalId = null;
    var bpm = {bpm};
    var nextTickTime = 0;

    function playSound() {{
        var oscillator = audioCtx.createOscillator();
        var gainNode = audioCtx.createGain();

        oscillator.type = 'sine';
        oscillator.frequency.setValueAtTime(880, audioCtx.currentTime); // 880Hz 高音
        
        gainNode.gain.setValueAtTime(1, audioCtx.currentTime);
        gainNode.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 0.1);

        oscillator.connect(gainNode);
        gainNode.connect(audioCtx.destination);

        oscillator.start();
        oscillator.stop(audioCtx.currentTime + 0.1);
        
        // 視覺閃爍
        const visual = document.getElementById('visual');
        visual.innerText = '●';
        visual.style.color = '#FF4B4B';
        setTimeout(() => {{
            visual.innerText = '○';
            visual.style.color = '#E0E0E0';
        }}, 100);
    }}

    document.getElementById('startBtn').onclick = function() {{
        if (audioCtx.state === 'suspended') {{
            audioCtx.resume();
        }}
        
        if (isRunning) {{
            clearInterval(intervalId);
            isRunning = false;
            this.innerText = '開始';
        }} else {{
            var step = 60000 / {bpm};
            intervalId = setInterval(playSound, step);
            isRunning = true;
            this.innerText = '停止';
        }}
    }};
</script>
"""

components.html(metronome_html, height=300)

st.caption("提示：若沒聲音，請檢查手機是否開啟靜音模式，並點擊一次『開始』觸發瀏覽器音訊。")
