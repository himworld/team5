import streamlit as st

# 이미지 파일들
image_filenames = [f"images/logo_1990 ({i}).jpg" for i in range(1, 11)]

# Streamlit 앱 생성
st.title("1990년대 회사 알아보기")

# 이미지를 5개씩 2줄로 나열해서 표시
col1, col2, col3 = st.columns(3)

with col1:
    st.image(image_filenames[0])
    with st.expander(f"정보"):
        st.write("종합무역상사, 다양한 상품을 종합하여 국내 시장에 팔거나 외국과 무역하는 일을 하는 기업")

with col2:
    st.image(image_filenames[1])
    with st.expander(f"정보"):
        st.write("정유 회사, 원유를 정제하여 다양한 석유 제품을 생산하는 기업으로 시설 규모가 큼")

with col3:
    st.image(image_filenames[2])
    with st.expander(f"정보"): 
        st.write("시멘트 회사, 다양한 건축물이나 도로를 만들 때 사용하는 시멘트를 만드는 회사")

col4, col5, col6 = st.columns(3)

with col4:
    st.image(image_filenames[3])
    with st.expander(f"정보"):
        st.write("의류 회사, 옷, 신발, 잡화 등 다양한 의류 용품을 만들어 파는 경공업 회사")

with col5:
    st.image(image_filenames[4])
    with st.expander(f"정보"):
        st.write("자동차 회사, 자동차를 만드는 회사로 자동차산업 발달에 따라 눈부신 성장을 이루어냄")

with col6:
    st.image(image_filenames[5])
    with st.expander(f"정보"):
        st.write("선박을 만드는 회사, 주로 무역업에 쓰이는 상선을 제작함")

col7, col8, col9 = st.columns(3)

with col7:
    st.image(image_filenames[6])
    with st.expander(f"정보"):
        st.write("제철 회사, 철광석에서 철을 추출하여 각종 철재를 만들어 내는 회사")

with col8:
    st.image(image_filenames[7])
    with st.expander(f"정보"):
        st.write("다양한 전자제품을 만들고, 우리나라 뿐 아니라 세계에 수출함")

with col9:
    st.image(image_filenames[8])
    with st.expander(f"정보"):
        st.write("당시 시중 은행의 금리")