import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 초기화
if 'funds' not in st.session_state:
    st.session_state.funds = 1000000  # 초기 자금
if 'stock_prices' not in st.session_state:
    st.session_state.stock_prices = {
        'D그룹': 350000,
        'S정유': 325000,
        'H시멘트': 75000,
        'K의류': 50000,
        'H자동차': 225000,
        'A조선': 37000,
        'P철강': 60000,
        'S전자': 225000
    }
if 'updated_prices' not in st.session_state:
    st.session_state.updated_prices = {
        'D그룹': 385000,
        'S정유': 390000,
        'H시멘트': 82000,
        'K의류': 53000,
        'H자동차': 300000,
        'A조선': 50000,
        'P철강': 72000,
        'S전자': 315000
    }

# 투자 포트폴리오 계산 함수
def calculate_portfolio(tickers, shares, initial_funds, stock_prices, updated_prices):
    shares = {ticker: int(share) for ticker, share in shares.items() if share != ''}
    savings = shares.pop('저축통장', 0)  # 저축액수가 없으면 0으로 처리

    # 저축액수와 주식 투자금액 합산
    total_investment_value = sum(stock_prices[ticker] * share for ticker, share in shares.items())
    total_funds_used = total_investment_value + savings
    
    # 초기 자금보다 투자금액이 많을 때 에러 메시지 처리
    if total_funds_used > initial_funds:
        return -1, [], "자금이 부족합니다.", 0
    
    # 주식 투자 결과 계산
    total_investment_result = sum(updated_prices[ticker] * share for ticker, share in shares.items())
    savings_interest = savings * 0.15  # 15%의 이자 계산
    total_savings = savings + savings_interest  # 저축액과 이자를 더한 총 저축액
    total_investment_result += total_savings  # 총투자결과액에 총 저축액을 더합니다.
    
    portfolio_details = []
    for ticker, share in shares.items():
        investment = stock_prices[ticker] * share
        updated_value = updated_prices[ticker] * share
        profit_loss = updated_value - investment
        portfolio_details.append({
            'Ticker': ticker,
            'Shares': share,
            'Old Price': stock_prices[ticker],
            'New Price': updated_prices[ticker],
            'Investment': investment,
            'Updated Value': updated_value,
            'Profit/Loss': profit_loss
        })
    
    # 저축 통장 항목 추가
    portfolio_details.append({
        'Ticker': '저축통장',
        'Shares': savings,
        'Old Price': 1,  # 1원 단위로 계산
        'New Price': 1.15,  # 이자가 포함된 단위 가격
        'Investment': savings,
        'Updated Value': total_savings,
        'Profit/Loss': savings_interest
    })

    final_funds = initial_funds - total_funds_used + total_investment_result
    return final_funds, portfolio_details, "", total_investment_result, total_funds_used  # total_funds_used 반환 추가

# 메인 페이지 상단 설정
st.header('내 자금')
initial_funds = st.session_state.funds
st.write(f"초기 자금: ₩{initial_funds:,.0f}")
remaining_funds = st.empty()

# 프로그레스 바
progress_bar = st.progress(100)

# 투자할 종목 선택
st.header("투자 종목 선택")
selected_tickers = st.multiselect("종목을 선택하세요", list(st.session_state.stock_prices.keys()))
shares_dict = {ticker: st.number_input(f"{ticker} 주식 수", value=0, min_value=0) for ticker in selected_tickers}
# 저축통장 입력을 위한 별도 UI 구성
savings_amount = st.number_input("저축통장 저축액수", value=0, min_value=0)
shares_dict['저축통장'] = savings_amount

# 투자 실행 버튼
submit_button = st.button("투자 실행")

# 사용자가 입력했을 때의 처리
if submit_button:
    # 입력된 값들을 모두 정수로 변환
    shares_dict = {ticker: int(shares) for ticker, shares in shares_dict.items()}
    savings_amount = int(savings_amount)
    if not selected_tickers and savings_amount <= 0:
        st.error("적어도 하나 이상의 종목을 선택하거나 저축액수를 입력해야 합니다.")
    else:
        if any(share <= 0 for share in shares_dict.values()):
            st.error("주식 수 또는 저축액수가 0보다 커야 합니다.")
        else:
            # 포트폴리오 계산
            remaining_funds_value, details, message, total_investment_result, total_funds_used = calculate_portfolio(
            selected_tickers, shares_dict, initial_funds, st.session_state.stock_prices, st.session_state.updated_prices
            )
            if message:
                st.error(message)
            else:
                # 결과 출력
                st.success(f"투자가 성공적으로 실행되었습니다. 남은 자금: ₩{remaining_funds_value:,.0f}")

                # 포트폴리오 상세 정보 출력
                st.subheader("포트폴리오 상세")
                df = pd.DataFrame(details)
                st.write(df)

                # 최종 자금 계산 업데이트
                final_funds = initial_funds - total_funds_used + total_investment_result
                st.write(f"최종 자금(투자 후 자금 + 수익): ₩{final_funds:,.0f}")

                # 프로그레스 바 업데이트
                percent_remaining = max(0.0, min(1.0, (remaining_funds_value / initial_funds)))
                progress_bar.progress(percent_remaining)
                remaining_funds.markdown(f"남은 자금: ₩{remaining_funds_value:,.0f} ({percent_remaining * 100:.2f}%)")

                # 주식 가격 변동률 계산 및 차트 표시
                price_changes = {ticker: {
                    'Old Price': st.session_state.stock_prices[ticker],
                    'New Price': st.session_state.updated_prices[ticker],
                    'Change': ((st.session_state.updated_prices[ticker] - st.session_state.stock_prices[ticker]) / st.session_state.stock_prices[ticker]) * 100
                } for ticker in selected_tickers if ticker != '저축통장'}

                # 가격 변동 차트 생성
                changes_df = pd.DataFrame(price_changes).T
                fig, ax = plt.subplots()
                changes_df['Change'].plot(kind='bar', ax=ax)
                ax.set_ylabel('Percentage Change (%)')
                ax.set_title('Stock Price Changes')
                st.pyplot(fig)


                # 선택한 항목과 선택하지 않은 항목의 주식 종목 변동을 표시하는 차트 추가
import matplotlib.pyplot as plt

def plot_stock_changes(stock_prices, updated_prices):
    # 종목별 가격 변동 및 변동률 계산
    price_changes = {ticker: updated_prices[ticker] - stock_prices[ticker] for ticker in stock_prices}
    percent_changes = {ticker: (price_changes[ticker] / stock_prices[ticker]) * 100 for ticker in stock_prices}

    # 차트를 그립니다.
    fig, ax = plt.subplots()
    tickers = list(stock_prices.keys())
    y_pos = range(len(tickers))
    changes = [price_changes[ticker] for ticker in tickers]

    ax.barh(y_pos, changes, align='center')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(tickers)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Price Change')
    ax.set_title('Stock Price Changes and Percentages')

    for i in y_pos:
        plt.text(changes[i], i, f"{changes[i]} ({percent_changes[tickers[i]]:.2f}%)", va='center')

    plt.tight_layout()
    return fig  # 차트 객체를 반환합니다.

# 스트림릿에서 차트를 그리는 부분
if submit_button:
    # 포트폴리오 계산 후 결과 표시
    # ...

    # 차트 그리기
    fig = plot_stock_changes(st.session_state.stock_prices, st.session_state.updated_prices)
    st.pyplot(fig)  # 스트림릿을 통해 차트를 표시합니다.