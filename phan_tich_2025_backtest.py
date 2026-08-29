import yfinance as yf
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random
#5.4. Backtesting
stocks = ['AAPL', 'MSFT', 'NVDA']

data = yf.download(stocks,
                   start='2025-01-01',
                   end='2026-01-01')

returns = data['Close'].pct_change().dropna()
returns_2025 = returns.mean() # lợi nhuận xấp xỉ hằng ngày
cov_matrix_annual = returns.cov()*252
expected_returns = returns.mean()*252

vector_weights_20_24 = [0.2968,0.1042,0.5990]
vector_weights_25 = [0.4001,0.4998,0.1001]
expected_portfolio_return = np.dot(np.transpose(vector_weights_20_24), expected_returns)
print(f"Kết quả của max return: {expected_portfolio_return}")
print(f"vector expected returns của max return: {expected_returns}")
portfolio_volatility = np.sqrt(np.dot(np.transpose(vector_weights_20_24),np.dot(cov_matrix_annual,vector_weights_20_24)))    
print(f"kết quả của risk max return: {portfolio_volatility}")
# tính sharpe ratio
sharpe_ratio = (expected_portfolio_return - 0.01) / portfolio_volatility
print(f"Sharpe ratio max return: {sharpe_ratio}")
print(f"Độ rủi ro hằng năm của các mã cổ phiếu {returns.std()*np.sqrt(252)}")


portfolio_daily_returns = returns.dot(vector_weights_20_24)   # (249,) — chuỗi return portfolio theo ngày
cumulative_return = (1 + portfolio_daily_returns).prod() - 1
portfolio_volatility_2025 = portfolio_daily_returns.std() * np.sqrt(252)

sharpe_2025 = (cumulative_return - 0.01) / portfolio_volatility_2025
print(f"Cumulative return 2025: {cumulative_return:.2%}")
print(f"Volatility 2025: {portfolio_volatility_2025:.2%}")
print(f"Sharpe 2025: {sharpe_2025:.4f}")

portfolio_daily_returns = returns.dot(vector_weights_25)   # (249,) — chuỗi return portfolio theo ngày
cumulative_return = (1 + portfolio_daily_returns).prod() - 1
portfolio_volatility_2025 = portfolio_daily_returns.std() * np.sqrt(252)

sharpe_2025 = (cumulative_return - 0.01) / portfolio_volatility_2025
print(f"Cumulative return 2025: {cumulative_return:.2%}")
print(f"Volatility 2025: {portfolio_volatility_2025:.2%}")
print(f"Sharpe 2025: {sharpe_2025:.4f}")

weights_fixed = np.array([1/3, 1/3, 1/3]) # Trọng số cố định cho mỗi cổ phiếu
port_ret = (returns * weights_fixed).sum(axis=1) 
daily_rf = 0.01 / 252 # Lãi suất phi rủi ro hàng ngày. Giả sử lãi suất phi rủi ro hàng năm là 1%, thì lãi suất phi rủi ro hàng ngày sẽ là 0.01/252

print("=== BENCHMARK 1/3--1/3--1/3 ===")
print(f"Return (daily):      {round(port_ret.mean()*100, 4)}%")
print(f"Risk (daily):        {round(port_ret.std()*100, 4)}%")
print(f"Return (annualized): {round(port_ret.mean()*252*100, 2)}%")
print(f"Risk (annualized):   {round(port_ret.std()*np.sqrt(252)*100, 2)}%")
print(f"Sharpe Ratio:        {round((port_ret.mean()-daily_rf)/port_ret.std()*np.sqrt(252), 4)}")
