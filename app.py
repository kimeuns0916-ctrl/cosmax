import pathlib
import streamlit as st
import streamlit.components.v1 as components

# ------------------------------------------------------------
# IngreTrend — 화장품 원료별 PubMed 연구 동향 트래킹 도구
# ------------------------------------------------------------
# 원본 IngreTrend.html은 순수 HTML+CSS+JS 단일 파일이며,
# PubMed E-utilities / 번역 API를 브라우저에서 직접 fetch로 호출합니다.
# (백엔드 서버가 필요 없는 구조이므로, Streamlit에서는 그대로
#  iframe에 임베드하여 실행합니다.)
# ------------------------------------------------------------

st.set_page_config(
    page_title="IngreTrend · 원료별 PubMed 연구 동향",
    page_icon="📈",
    layout="wide",
)

HTML_PATH = pathlib.Path(__file__).parent / "IngreTrend.html"

if not HTML_PATH.exists():
    st.error(
        "IngreTrend.html 파일을 찾을 수 없습니다. "
        "app.py와 같은 폴더에 IngreTrend.html이 있는지 확인해주세요."
    )
else:
    html_content = HTML_PATH.read_text(encoding="utf-8")
    # 화면 높이에 맞춰 충분히 크게 렌더링하고, 내부적으로 스크롤이 가능하도록 설정
    components.html(html_content, height=2400, scrolling=True)
