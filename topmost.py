import time
import win32gui
import win32con
import win32api
import pywintypes

def toggle_topmost(hwnd):
    # 获取窗口当前的Z顺序状态
    style = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)

    # 判断窗口是否已经置顶
    if style & win32con.WS_EX_TOPMOST:
        # 如果窗口已经置顶，则取消置顶
        win32gui.SetWindowPos(
            hwnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0,
            win32con.SWP_NOMOVE | win32con.SWP_NOSIZE
        )
        print("已取消置顶")
    else:
        # 如果窗口没有置顶，则设置为置顶
        win32gui.SetWindowPos(
            hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0,
            win32con.SWP_NOMOVE | win32con.SWP_NOSIZE
        )
        print("已置顶")

user_input = input("按下[Enter]开始倒计时")
wait_time = 3

# 等待 3 秒
for i in range(wait_time):
    print(wait_time-i)
    time.sleep(1)

# 获取当前活动窗口的句柄
hwnd = win32gui.GetForegroundWindow()

# 获取窗口标题
window_title = win32gui.GetWindowText(hwnd)

# 输出窗口句柄和标题
if hwnd and window_title:
    print(f"窗口“{window_title}”")
    flag = True
else:
    print("未找到活跃窗口")
    flag = False

if flag:
    toggle_topmost(hwnd)

time.sleep(10)