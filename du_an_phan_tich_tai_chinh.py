import yfinance as yf
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random
#2.1 Thu thập dữ liệu
stocks = ['AAPL', 'MSFT', 'NVDA']

data = yf.download(stocks,
                   start='2020-01-01',
                   end='2025-01-01')
data.to_excel("stock_data.xlsx") 
#3. Thống kê mô tả
#3.1. Tóm tắt lợi nhuận và rủi ro
returns = data['Close'].pct_change().dropna()
mean_return = returns.mean() # lợi nhuận hằng ngày
annualized_mean_return = mean_return*252 # lợi nhuận hằng năm
daily_volatility = returns.std() # rủi ro hằng ngày
annualized_volatility = daily_volatility*np.sqrt(252) # rủi ro hằng năm
min_return = returns.min() # lợi nhuận tối thiểu
max_return = returns.max() # lợi nhuận tối đa
#3.2. Biểu đồ phân phối lợi nhuận hằng ngày
n_bins = 50
bin_edges = np.linspace(returns.min().min(), returns.max().max(), n_bins + 1)

fig, axes = plt.subplots(2, 2, figsize=(15, 4*2))

for ax, col in zip(axes.flatten(), returns.columns):
    ax.hist(returns[col], bins=bin_edges) 
    ax.set_title(col)

n_stocks = len(returns.columns)

for ax in axes.flatten()[n_stocks:]:
    ax.set_visible(False)

for ax in axes.flatten():
    ax.grid(True)
    ax.set_xlabel("Daily Return")
    ax.set_ylabel("Frequency")
plt.suptitle('Distribution of Returns')
plt.tight_layout()
plt.show()
#4. Phân tích tương quan
#Ma trận tương quan Pearson
correlation = returns.corr()
print("Hệ số tương quan giữa các cổ phiếu:")
print(round(correlation,3))
sns.heatmap(round(correlation,3), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation of Stock Returns')
plt.show()
#5. Tối ưu hóa danh mục
#5.1. Mô phỏng Monte Carlo
mean_return_annual = returns.mean() * 252
cov_matrix_annual = returns.cov() * 252
rf_annual = 0.01

num_portfolios = 10000
results = np.zeros((3, num_portfolios))
weights_record = []

for i in range(num_portfolios):
    while True:
        weights = np.random.dirichlet(np.ones(len(stocks)))
        if np.all(weights >= 0.1) and np.all(weights <= 0.6):
            break

    portfolio_return = np.dot(weights, mean_return_annual)
    portfolio_risk = np.sqrt(np.dot(weights.T, np.dot(cov_matrix_annual, weights)))
    portfolio_sharpe = (portfolio_return - rf_annual) / portfolio_risk

    results[0, i] = portfolio_return   # giờ đã annualized
    results[1, i] = portfolio_risk     # giờ đã annualized
    results[2, i] = portfolio_sharpe   # annualized, không cần nhân √252 nữa

    weights_record.append(weights)

max_sharpe_idx = np.argmax(results[2])
min_risk_idx   = np.argmin(results[1])
max_return_idx = np.argmax(results[0])

def print_portfolio(name, idx):
    print(f"\n--- {name} ---")
    print(f"Expected Return (annual): {results[0, idx]*100:.2f}%")
    print(f"Risk / Volatility (annual): {results[1, idx]*100:.2f}%")
    print(f"Sharpe Ratio: {results[2, idx]:.4f}")
    print("Weights:")
    for stock, w in zip(stocks, weights_record[idx]):
        print(f"  {stock}: {w*100:.2f}%")

print_portfolio("Max Sharpe Ratio Portfolio", max_sharpe_idx)
print_portfolio("Min Risk Portfolio", min_risk_idx)
print_portfolio("Max Return Portfolio", max_return_idx)

plt.figure(figsize=(10, 6))
 
sc = plt.scatter(results[1], results[0], c=results[2],
                  cmap='viridis', s=8, alpha=0.6)
plt.colorbar(sc, label='Sharpe Ratio')
 
plt.scatter(*[results[1, max_sharpe_idx], results[0, max_sharpe_idx]],
            color='red', s=100, zorder=5, label='Max Sharpe Ratio')

plt.scatter(*[results[1, min_risk_idx], results[0, min_risk_idx]],
            color='blue', s=100, zorder=5, label='Min Risk')

plt.scatter(*[results[1, max_return_idx], results[0, max_return_idx]],
            color='green', s=100, zorder=5, label='Max Return')

plt.xlabel('Risk (Annual Std)')
plt.ylabel('Return (Annual Mean)')
plt.title('Monte Carlo Simulation of Portfolio Risk-Return')
plt.legend()
plt.show()