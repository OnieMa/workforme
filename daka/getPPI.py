import tkinter as tk
from screeninfo import get_monitors


def get_screen_ppi():
	# 获取屏幕尺寸（以英寸为单位）
	root = tk.Tk()
	screen_width = root.winfo_screenwidth()
	screen_height = root.winfo_screenheight()
	root.destroy()

	# 获取物理屏幕尺寸（以毫米为单位）
	monitor = get_monitors()[0]
	screen_width_mm = monitor.width_mm
	screen_height_mm = monitor.height_mm

	print(screen_width_mm)
	print(screen_height_mm)


	# 将毫米转换为英寸（1英寸 = 25.4毫米）
	screen_width_in = screen_width_mm / 25.4
	screen_height_in = screen_height_mm / 25.4

	# 计算屏幕的PPI
	ppi_x = screen_width / screen_width_in
	ppi_y = screen_height / screen_height_in

	return (ppi_x + ppi_y) / 2


# 获取当前屏幕的PPI
ppi = get_screen_ppi()
print(f"当前屏幕的PPI为: {ppi}")
