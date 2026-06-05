# Deploy Lingo Flask lên Render

## Cách nhanh nhất

1. Đẩy source code lên GitHub.
2. Vào Render Dashboard.
3. Chọn **New** -> **Blueprint**.
4. Kết nối repo này.
5. Render sẽ đọc file `render.yaml` và tự tạo Web Service.
6. Khi Render hỏi secret env, nhập các key Gemini:
   - `GEMINI_API_KEY1`
   - `GEMINI_API_KEY2`
   - `GEMINI_API_KEY3`

## Tài khoản sau khi deploy

Nếu database trên Render đang trống, app sẽ tự nạp dữ liệu học thật một lần.

- Học sinh: `hocsinh01 / 123456`
- Giáo viên: `giaovien01 / 123456`

## Cấu hình quan trọng

- Build command: `pip install -r requirements.txt`
- Start command: `python render_start.py && gunicorn app:app --workers 2 --threads 4 --timeout 120 --bind 0.0.0.0:$PORT`
- Health check: `/healthz`
- SQLite DB: `/opt/render/project/src/.render-data/users.db`
- Upload files: `/opt/render/project/src/.render-data/uploads`

## Lưu ý

Project này đang dùng SQLite và upload file local, nên `render.yaml` đã gắn persistent disk 1GB. Không đưa `.env` lên GitHub; nhập API key trong Render Environment.
