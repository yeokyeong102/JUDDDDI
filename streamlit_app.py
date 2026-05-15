import streamlit as st

# 페이지 제목
st.title("👋 자기 소개")

# 이름과 간단한 인사
st.header("이름: 이여경")
st.write("안녕하세요! 저는 영어교육과 26학번입니다.")

# 사진 추가 (선택사항, 나중에 이미지 파일 경로를 넣으세요)
# st.image("path/to/your/photo.jpg", caption="프로필 사진", width=200)

# 자기 소개 섹션
st.subheader("자기 소개")
st.write("""
사람들과 어울리는 것을 좋아하고 여행 다니는 것을 좋아합니다.

예를 들어:
- 학력: 청주교육대학교 재학
- 경력: 학원강사 경험
- 관심사: 음악이랑 맛집
- 목표: 책 한 달에 한 권씩 읽기
""")

# 연락처 정보
st.subheader("연락처")
st.write("전화번호: 01052403900")
st.write("LinkedIn: [링크]")
st.write("GitHub: [링크]")

# 추가 섹션 (선택사항)
st.subheader("프로젝트 또는 스킬")
st.write("일처리가 빠르고 정확함")
