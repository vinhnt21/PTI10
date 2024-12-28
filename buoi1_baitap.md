### Bài Tập: Quản Lý Sách Trong Thư Viện

Hãy viết chương trình quản lý sách trong một thư viện với các chức năng tương tự như chương trình quản lý sinh viên ở trên.

#### Yêu cầu:

1. **Lớp Book**:

   - Thuộc tính:
     - `title` (Tên sách).
     - `author` (Tác giả).
     - `published_year` (Năm xuất bản).
     - `isbn` (Mã số ISBN).
   - Phương thức:
     - `introduce`: In thông tin sách.

2. **Lớp Library**:

   - Thuộc tính:
     - `book_list`: Danh sách các sách (một list).
   - Phương thức:
     - `add_book`: Thêm một cuốn sách vào danh sách.
     - `show_all_books`: Hiển thị toàn bộ thông tin các sách trong danh sách.

3. **Chương trình chính**:
   - Hiển thị menu cho người dùng:
     1. Thêm sách mới.
     2. Hiển thị tất cả sách.
     3. Thoát chương trình.

#### Menu mẫu:

```plaintext
1. Add book
2. Show all books
3. Exit
Your choice:
```

#### Gợi ý triển khai:

1. Khi chọn `1`, yêu cầu người dùng nhập thông tin sách: `title`, `author`, `published_year`, `isbn` và thêm sách vào thư viện.
2. Khi chọn `2`, hiển thị toàn bộ danh sách các sách, mỗi sách ngăn cách bằng một dòng kẻ (`----------`).
3. Khi chọn `3`, kết thúc chương trình.

#### Yêu cầu thêm:

- Nếu người dùng nhập lựa chọn không hợp lệ, thông báo lỗi và hiển thị lại menu.
- Dữ liệu sách nên được lưu trong danh sách (`book_list`) của thư viện.
