import tkinter as tk
root = tk.Tk()
root.title("Thẻ Sinh Viên Số")
root.geometry("400x300")

# 1. Nhãn tiêu đề với Phông chữ và Màu sắc
nhan_truong = tk.Label(
    root, 
    text="TRƯỜNG ĐẠI HỌC HẠ LONG", 
    font=("Arial", 14, "bold"), 
    fg="black", 
    bg="#f8f9fa" # Màu xanh thương hiệu
)
nhan_truong.pack(fill="x", pady=10) # fill="x" để màu nền trải rộng hết chiều ngang

# 2. Nhãn hiển thị họ tên
nhan_ten = tk.Label(root, text="Họ tên: Lại Minh Huyền", font=("Arial", 12),bg='#f8f9fa')
nhan_ten.pack(pady=5)

# 3. Nhãn hiển thị MSSV với màu đỏ nổi bật
nhan_msv = tk.Label(root, text="MSSV: 24DH080046", font=("Arial", 12), fg="red",bg="#f8f9fa")
nhan_msv.pack(pady=5)
#4.Nhãn hiển thị khoa
nhan_khoa=tk.Label(root,text="Khoa: Công nghệ thông tin",font=("Arial", 12), fg="green",bg="#f8f9fa")
nhan_khoa.pack=(paddy=5)
# 5. Tạo nút bấm để thoát chương trình
nut_thoat = tk.Button(
    root, 
    text="Đóng ứng dụng", 
    command=root.destroy, 
    bg="#f8f9fa", # Màu đỏ cảnh báo
    fg="black",
    width=20,
    height=4
)
nut_thoat.pack(pady=20)

root.mainloop()
