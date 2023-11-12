import streamlit as st

def main():
    if 'round_num' not in st.session_state:
        st.session_state['round_num'] = None

    st.title('1라운드(1980년대) 종료!')
    if 'user_input' not in st.session_state:
        st.session_state["user_input"]=0

    if st.session_state['round_num'] is None:
        st.write('당신의 남은 금액은?')
        user_input = st.text_input('입력하세요', value='')

        if user_input and user_input.isdigit():
            amount = int(user_input)
            st.write(f'자, 이제 다음 라운드로 가즈아~!')
            st.session_state['round_num'] = amount

            if st.button('다음', key='next'):
                # 다음 화면으로 이동하는 코드를 추가하세요
                pass

    # 다음 페이지에서 이전 페이지에서 입력한 값을 사용할 수 있습니다.
    st.write(f'이전 라운드: {st.session_state["round_num"]}')

if __name__ == '__main__':
    main()