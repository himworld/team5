import streamlit as st

# 이미지 파일들
image_filenames = [f"images/logo_1990 ({i}).jpg" for i in range(1, 11)]

# Streamlit 앱 생성
st.title("1990년대 회사 주식 가격")

# 이미지를 5개씩 2줄로 나열해서 표시
col1, col2, col3 = st.columns(3)

with col1:
    st.image(image_filenames[0])
    with st.expander(f"가격"):
        st.write("350000")

with col2:
    st.image(image_filenames[1])
    with st.expander(f"가격"):
        st.write("325000")

with col3:
    st.image(image_filenames[2])
    with st.expander(f"가격"): 
        st.write("75000")

col4, col5, col6 = st.columns(3)

with col4:
    st.image(image_filenames[3])
    with st.expander(f"가격"):
        st.write("50000")

with col5:
    st.image(image_filenames[4])
    with st.expander(f"가격"):
        st.write("225000")

with col6:
    st.image(image_filenames[5])
    with st.expander(f"가격"):
        st.write("37000")

col7, col8, col9 = st.columns(3)

with col7:
    st.image(image_filenames[6])
    with st.expander(f"가격"):
        st.write("60000")

with col8:
    st.image(image_filenames[7])
    with st.expander(f"가격"):
        st.write("225000")

with col9:
    st.image(image_filenames[8])
    with st.expander(f"이자"):
        st.write("15%")