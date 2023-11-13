import streamlit as st
import time

# 영상 파일 경로 리스트
video_files = ["intro.mp4", "rule.mp4"]
current_video_index = 0

# Streamlit 앱 시작
st.title("껄무새 탈출하기")

# 현재 영상 파일
current_video_file = video_files[current_video_index]

# 영상 보여주기
video_placeholder = st.empty()
video_placeholder.video(current_video_file)

# 다음 영상으로 넘어가는 버튼
button_placeholder = st.empty()
button_clicked = button_placeholder.button("다음 영상")

# 버튼 클릭 후 동적으로 업데이트
if button_clicked:
    current_video_index = (current_video_index + 1) % len(video_files)
    current_video_file = video_files[current_video_index]

    # 버튼 클릭 후 동적으로 업데이트
    video_placeholder.video(current_video_file)
    st.success("왼쪽 바에서 다음 단계 클릭. 🚀")

    # 마지막 화면인 경우 버튼 숨김
    if current_video_index == len(video_files) - 1:
        button_placeholder.empty()

# 사이드바에 버튼 생성
if st.sidebar.button("다른 페이지로 이동"):
    # 다른 Streamlit 웹 페이지의 URL
    new_page_url = "https://team5page2.streamlit.app/"

    # 페이지를 새 URL로 리다이렉트
    st.experimental_rerun()
