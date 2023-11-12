import streamlit as st


# 이미지 파일들
image_filenames = ["anal(1).jpg", "anal(2).jpg", "anal(3).jpg", "anal(4).jpg", "anal(5).jpg"]

# Streamlit 앱 생성
st.title("1990년대 경제신문")

#각 이미지를 나열해서 표시
for i, image_filename in enumerate(image_filenames):
    image_path = f"images/pic/{image_filename}"
    print(image_path)
    st.image(image_path, caption=f"기사 {i + 1}", use_column_width=True)
    