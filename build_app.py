"""
build_app.py — IngreTrend.html 내용을 app.py 안에 다시 녹여 넣는 생성 스크립트.

사용법:
    python build_app.py

IngreTrend.html을 수정한 뒤 이 스크립트를 실행하면, 그 내용을 그대로
app.py의 HTML_CONTENT(raw 삼중따옴표 문자열)에 담아 app.py를 다시 만듭니다.
외부 파일에 의존하지 않으므로 Streamlit Cloud 배포 시 파일 누락이 발생하지 않습니다.
"""
import pathlib

ROOT = pathlib.Path(__file__).parent
HTML_PATH = ROOT / "IngreTrend.html"
APP_PATH = ROOT / "app.py"

HEADER = '''import streamlit as st
import streamlit.components.v1 as components

# ------------------------------------------------------------
# IngreTrend — 화장품 원료별 PubMed 연구 동향 트래킹 도구
# ------------------------------------------------------------
# 원본 IngreTrend.html(순수 HTML+CSS+JS 단일 파일)의 내용을 아래
# HTML_CONTENT 문자열에 그대로 담았습니다. 외부 파일에 의존하지 않으므로
# Streamlit Cloud 배포 시 파일 누락 없이 항상 동작합니다.
#
# raw 문자열(r-string)이라 HTML 안의 백슬래시/따옴표는 이스케이프가 필요 없습니다.
# HTML을 수정할 때는 IngreTrend.html을 고친 뒤 build_app.py 로 이 파일을 다시 생성하세요.
# ------------------------------------------------------------

st.set_page_config(
    page_title="IngreTrend · 원료별 PubMed 연구 동향",
    page_icon="\U0001F4C8",
    layout="wide",
)

HTML_CONTENT = r'''

FOOTER = '''

# 화면 높이에 맞춰 충분히 크게 렌더링하고, 내부 스크롤을 허용
components.html(HTML_CONTENT, height=2400, scrolling=True)
'''

TQ = '"' * 3  # 삼중 큰따옴표


def main() -> None:
    html = HTML_PATH.read_text(encoding="utf-8")

    if TQ in html:
        raise SystemExit('IngreTrend.html에 삼중 큰따옴표(""")가 있어 raw 삼중따옴표에 담을 수 없습니다.')

    body = "\n" + html
    if not body.endswith("\n"):
        body += "\n"
    # raw string은 백슬래시로 끝날 수 없음 → 개행으로 끝나므로 안전
    if body.rstrip("\n").endswith("\\"):
        raise SystemExit("HTML이 백슬래시로 끝나 raw string 종료가 깨집니다.")

    out = HEADER + TQ + body + TQ + FOOTER
    APP_PATH.write_text(out, encoding="utf-8")

    # 문법 검증
    import py_compile
    py_compile.compile(str(APP_PATH), doraise=True)
    print(f"app.py 생성 완료 ({len(out):,} bytes) · 문법 정상")


if __name__ == "__main__":
    main()
