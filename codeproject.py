import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 페이지 설정
st.set_page_config(page_title="김예준의 Streamlit 블로그", page_icon="⚾")

# 제목과 소개
st.title("⚾ 김예준의 관심 분야 블로그")
st.caption("홍익대학교 경영학과 C031048 · 2025-06-16")

st.divider()

# 1. 자기소개
st.header("1. 자기소개")
st.markdown("""
안녕하세요! 저는 홍익대학교 경영학과에 재학 중인 김예준입니다.  
저는 어릴 때부터 야구를 좋아했고, 지금도 다양한 경기를 챙겨보며 기록을 분석하는 것을 즐깁니다.
""")

st.divider()

# 2. 관심 기업 소개
st.header("2. 관심 기업: SSG 랜더스")
st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRPuUTL-kXCV-10Qw-iZpTZPWp0C_ONf5P5qQ&s", caption="SSG 랜더스 로고", width=200)
st.markdown("""
SSG 랜더스는 신세계그룹이 운영하는 KBO 리그 구단으로, 마케팅과 팬 경험 분야에서 매우 혁신적인 접근을 보여주고 있는 기업입니다.  
경영학을 전공하는 입장에서 스포츠 산업의 브랜딩 전략과 팬 기반 확장 전략에 큰 관심이 있습니다.
""")

st.divider()

# 3. 관심 주제: 야구 통계
st.header("3. 관심 주제: 야구 통계")

st.markdown("선수 A의 최근 10경기 성적 (가상의 데이터)")

# 샘플 데이터
data = pd.DataFrame({
    '경기': list(range(1, 11)),
    '타율': np.random.uniform(0.2, 0.4, 10),
    'OPS': np.random.uniform(0.7, 1.2, 10)
})
st.dataframe(data)

# 라인 차트
st.subheader("📈 타율 변화 추이")
st.line_chart(data[['타율']])

st.divider()

# 4. 코드 블록과 수식 예시
st.header("4. 코드와 수식 예시")

st.code('print("안녕하세요, SSG 랜더스!")', language='python')

st.latex(r'''
\text{OPS} = \text{출루율} + \text{장타율}
''')

st.divider()

# 5. 콜아웃(Callout)
st.header("5. 콜아웃 메시지 예시")

st.info('This is a purely informational message')
st.warning('This is a warning message')
st.error('This is an error message')
st.success('This is a success message')

st.divider()


st.write("⚾ 감사합니다!")