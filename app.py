import random
import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="점심 메뉴 추천기", page_icon="🍱")

st.title("🍱 오늘의 점심 메뉴 추천")
st.write("버튼을 눌러 오늘 먹을 점심 메뉴를 랜덤으로 골라보세요!")

# 점심 메뉴 리스트 (원하는 메뉴를 자유롭게 추가/수정하세요)
lunch_menus = [
    "김치찌개",
    "된장찌개",
    "제육볶음",
    "돈까스",
    "순대국밥",
    "짜장면",
    "짬뽕",
    "초밥",
    "파스타",
    "햄버거",
    "비빔밥",
    "쌀국수",
    "마라탕",
    "칼국수",
    "샌드위치",
]

# 추천 버튼 클릭 시 동작
if st.button("🎲 메뉴 추천받기", use_container_width=True):
    selected_menu = random.choice(lunch_menus)
    st.balloons()  # 축하 풍선 효과
    st.success(f"오늘의 추천 점심 메뉴는 **{selected_menu}**입니다! 🎉")

# 전체 메뉴 후보 목록 접이식 표시
with st.expander("📋 현재 등록된 메뉴 후보 보기"):
    st.write(", ".join(lunch_menus))
