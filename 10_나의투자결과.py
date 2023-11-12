import streamlit as st


st.title("나의 결과 자산")

if 'ini_asset' not in st.session_state:
    st.session_state["ini_asset"]=0

if 'investment' not in st.session_state:
    st.session_state["investment"]=0

if 'ini_asset' not in st.session_state:
    st.session_state["ini_asset"]=0

if 'ini_asset' not in st.session_state:
    st.session_state["ini_asset"]=0

if 'ini_asset' not in st.session_state:
    st.session_state["ini_asset"]=0

st.session_state["ini_asset"] = st.number_input("초기자산",step = 1)
st.session_state["investment"] = st.number_input("투자금액")
st.session_state["rst_asset"] = st.number_input("결과자산")
ratio = st.number_input("수익률")
total = st.number_input("총자산")


st.write(total)
st.write("1라운드 종료")
if st.button("이어하기")==True:
    st.write("hello")