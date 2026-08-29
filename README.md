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
2. Thống kê mô tả: Tính lợi nhuận trung bình, độ biến động (volatility) hàng ngày và theo năm, ma trận tương quan giữa các cổ phiếu, trực quan hóa phân phối lợi nhuận hàng ngày của từng cổ phiếu bằng histogram
3. Phân tích tương quan: Lập ma trận tương quan Pearson để thể hiện mối quan hệ giữa các mã cổ phiếu
4. Mô phỏng Monte Carlo: Sinh 10,000 danh mục ngẫu nhiên (trọng số ràng buộc cho mỗi cổ phiếu trong khoảng 10%–60%), tính lợi nhuận kỳ vọng, rủi ro và Sharpe Ratio cho từng danh mục
5. Xác định danh mục tối ưu: Tìm danh mục có Sharpe Ratio cao nhất, rủi ro thấp nhất, và lợi nhuận cao nhất
6. Backtesting: Sử dụng bộ trọng số cổ phiếu từ danh mục tối ưu để áp dụng lên một giai đoạn khác.
7. Lập danh mục tham chiếu: Tạo danh mục tham chiếu (trọng số bằng nhau) để đánh giá độ hiệu quả của danh mục đầu tư.
8. Kết luận
## Ghi chú
 
Risk-free rate sử dụng trong tính toán Sharpe Ratio: 1%/năm.
