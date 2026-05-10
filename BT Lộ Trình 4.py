import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def xu_ly_du_lieu():
    # 1. Lấy dữ liệu từ ô nhập bằng phương thức .get()
    mssv = o_nhap_ma_sv.get()
    ho_ten = o_nhap_ho_ten.get()

    # 2. Kiểm tra dữ liệu rỗng
    if mssv == "" or ho_ten == "":
        messagebox.showerror("Chú ý", "Vui lòng không để trống thông tin sinh viên!")
        nhan_ket_qua.config(text="Vui lòng nhập đầy đủ thông tin!", fg="red")
        return

    # 3. Kiểm tra MSSV có phải là số hay không
    if not mssv.isdigit():
        messagebox.showerror("Lỗi", "MSSV phải là số!")
        nhan_ket_qua.config(text="MSSV không hợp lệ!", fg="red")
        return

    # 4. Lấy thời gian hiện tại
    thoi_gian = datetime.now().strftime("%H:%M:%S")

    # 5. In ra Terminal để lập trình viên kiểm tra
    print(f"[{thoi_gian}] Đã nhận: MSSV {mssv} - Tên: {ho_ten}")

    # 6. Cập nhật trực tiếp lên giao diện
    nhan_ket_qua.config(
        text=f"Thành công: Đã nhận dữ liệu của {ho_ten}",
        fg="green"
    )

    # 7. Xóa trắng ô nhập
    o_nhap_ma_sv.delete(0, tk.END)
    o_nhap_ho_ten.delete(0, tk.END)

root = tk.Tk()
root.title("Quản lý Sinh viên - UHL")
root.geometry("400x350")
root.columnconfigure(1, weight=1)

# --- PHẦN GIAO DIỆN ---
tk.Label(root, text="Mã sinh viên:").grid(row=0, column=0, padx=10, pady=10, sticky="w")

o_nhap_ma_sv = tk.Entry(root)
o_nhap_ma_sv.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

tk.Label(root, text="Họ và tên:").grid(row=1, column=0, padx=10, pady=10, sticky="w")

o_nhap_ho_ten = tk.Entry(root)
o_nhap_ho_ten.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

# --- NÚT BẤM ---
nut_xac_nhan = tk.Button(
    root,
    text="Xác nhận điểm danh",
    command=xu_ly_du_lieu
)

nut_xac_nhan.grid(
    row=2,
    column=0,
    columnspan=2,
    pady=10,
    padx=10,
    sticky="ew"
)

# --- NHÃN KẾT QUẢ ---
nhan_ket_qua = tk.Label(
    root,
    text="Hệ thống sẵn sàng",
    font=("Arial", 10, "italic")
)

nhan_ket_qua.grid(
    row=3,
    column=0,
    columnspan=2,
    pady=20
)

root.mainloop()
