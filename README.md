# D-n-c-nh-n
# Tối ưu hóa danh mục đầu tư - Cổ phiếu công nghệ Mỹ

Dự án phân tích rủi ro - lợi nhuận và tối ưu hóa danh mục đầu tư bằng mô phỏng Monte Carlo, nghiên cứu trên nhóm cổ phiếu công nghệ lớn của Mỹ (AAPL, MSFT, NVDA).

Cài đặt
```python
pip install yfinance seaborn matplotlib numpy pandas
```
## Cấu trúc file
* du_an_phan_tich_tai_chinh.py: xử lý và phân tích dữ liệu giai đoạn 2020–2024
* phan_tich_tai_chinh.py: xử lý và phân tích dữ liệu năm 2025 (bao gồm backtesting)

# Quy trình phân tích

1. Thu thập dữ liệu: Lấy giá đóng cửa lịch sử của AAPL, MSFT, NVDA qua yfinance
2. Thống kê mô tả: Tính lợi nhuận trung bình, độ biến động (volatility) hàng ngày và theo năm, ma trận tương quan giữa các cổ phiếu
3. Phân phối lợi nhuận: Trực quan hóa phân phối lợi nhuận hàng ngày của từng cổ phiếu bằng histogram
4. Mô phỏng Monte Carlo: Sinh 10,000 danh mục ngẫu nhiên (trọng số mỗi cổ phiếu trong khoảng 10%–60%), tính lợi nhuận kỳ vọng, rủi ro và Sharpe Ratio cho từng danh mục
5. Xác định danh mục tối ưu: Tìm danh mục có Sharpe Ratio cao nhất, rủi ro thấp nhất, và lợi nhuận cao nhất

## Kết quả chính

** Danh mục có Sharpe Ratio cao nhất (Max Sharpe Ratio Portfolio): **

| Chỉ số | Giá trị |
|---|---|
| Lợi nhuận kỳ vọng (năm) | 57.40% |
| Rủi ro / Độ biến động (năm) | 41.11% |
| Sharpe Ratio | 1.3719 |
 
**Phân bổ trọng số tối ưu:**
- AAPL: 29.32%
- MSFT: 10.87%
- NVDA: 59.80%
## Ghi chú
 
Risk-free rate sử dụng trong tính toán Sharpe Ratio: 1%/năm.
