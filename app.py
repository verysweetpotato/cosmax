import pathlib
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="포뮬로그 FormuLog | 처방 변경 이력 관리",
    layout="wide",
)

# app.py와 같은 폴더에 있는 index.html을 읽어서 그대로 렌더링합니다.
html_path = pathlib.Path(__file__).parent / "index.html"
html_content = html_path.read_text(encoding="utf-8")

components.html(html_content, height=1800, scrolling=True)
