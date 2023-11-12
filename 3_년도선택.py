import streamlit as st

def main():
    st.title('껄무새 탈출 작전')

    if st.button('1980년대'):
        st.write("1980년대 페이지입니다.")

    if st.button('1990년대'):
        st.write("1990년대 페이지입니다.")

    if st.button('IMF시대'):
        st.write("IMF시대 페이지입니다.")

    if st.button('2000년대'):
        st.write("2000년대 페이지입니다.")

if __name__ == '__main__':
    main()