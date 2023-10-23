import cv2
import numpy as np
import pyautogui
import time

def find_template(template_path, screenshot_path):
    # 加载模板图像和屏幕截图
    template = cv2.imread(template_path, 0)
    screenshot = cv2.imread(screenshot_path, 0)

    # 使用模板匹配算法进行匹配
    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # 如果找到匹配的位置
    if max_val > 0.8:
        # 提取模板图像的宽度和高度
        height, width = template.shape[:2]

        # 计算匹配位置的左上角和右下角坐标
        top_left = max_loc
        bottom_right = (top_left[0] + width, top_left[1] + height)

        # 返回中心点坐标
        center_x = (top_left[0] + bottom_right[0]) // 2
        center_y = (top_left[1] + bottom_right[1]) // 2
        return center_x, center_y

    # 如果未找到匹配的位置，返回None
    return None

def delay(seconds):
    time.sleep(seconds)
    print("延时完成！")

def click_button(template_path):
    # 获取屏幕尺寸
    screen_width, screen_height = pyautogui.size()

    # 进行屏幕截图
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")

    # 查找模板图像并获取中心点坐标
    button_pos = find_template(template_path, "screenshot.png")

    if button_pos is not None:
        # 计算点击位置的屏幕坐标
        x = int(button_pos[0] * screen_width / screenshot.width)
        y = int(button_pos[1] * screen_height / screenshot.height)

        # 使用pyautogui进行鼠标点击
        pyautogui.click(x, y)
        print("Clicked on the button!")
    else:
        print("Button not found.")

def check_result(template_path):
    button_pos = find_template(template_path, "screenshot.png")
    if button_pos is not None:
        print("Result OK!\n")
    else:
        print("Button not found.")



# for i in range(10):
#     # 获取条件1的输入
#     if condition == "条件1":
#         print("满足条件1，退出循环")
#         break
#     else:
#         print("不满足条件1，继续循环")
# print("循环结束")





# 测试代码
# template_path = r"E:\PythonProgram\pythonProject4\venv\button.png"  # 模板图像的路径
# click_button(template_path)
delay(1) # 延时2秒
result_path = r"E:\PythonProgram\pythonProject4\venv\Result2.png"  # 模板图像的路径
check_result(result_path)
