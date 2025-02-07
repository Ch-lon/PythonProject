import sys
import tkinter as tk

import requests


def cityIsNull():
    city = city_entry.get()
    if not city.strip():
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "请输入有效的城市名称。")
        return das
    else:
        return city

#获取城市id
def get_city():
    city = cityIsNull()
    api_key = "60476540a0944aa2b2cfa50135bc4c24"
    url = f'https://geoapi.qweather.com/v2/city/lookup?location={city}&key={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        city_data = response.json()
        if city_data and city_data.get("location"):
            # 获取location内容
            location_list = city_data.get("location")
            # 获取location第一个列表【】里的内容
            city_value = location_list[0]
            # 获取城市ID
            #city_name = city_value.get('name')
            city_id = city_value.get('id')
            #result_text.insert(tk.END, f'城市：{city_name}\n')
            return city_id
        else:
            result_text.insert(tk.END, "获取 location 信息失败，请检查输入的城市或网络连接。")
    else:
        result_text.insert(tk.END, "获取城市code错误，请检查查询城市模块的输入参数和认证信息。")


#查询天气
def get_weather():
    cityid = get_city()
    city = cityIsNull()
    api_key = "60476540a0944aa2b2cfa50135bc4c24"  # 请将 YOUR_API_KEY 替换为你自己的 API 密钥
    url = f"https://devapi.qweather.com/v7/weather/now?location={cityid}&key={api_key}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            weather_data = response.json()
            if weather_data and weather_data.get("now"):
                now = weather_data.get('now')
                if now:
                    time = now.get("obsTime")
                    description = now.get("text")
                    temperature = now.get("temp")
                    humidity = now.get("windDir")
                    result_text.delete(1.0, tk.END)
                    result_text.insert(tk.END, f"城市:{city}\n")
                    result_text.insert(tk.END, f"时间: {time}\n")
                    result_text.insert(tk.END, f"天气: {description}\n")
                    result_text.insert(tk.END, f"温度: {temperature}°C\n")
                    result_text.insert(tk.END, f"风向: {humidity}\n")
            else:
                result_text.insert(tk.END, "未找到 'now' 部分的天气数据，请检查 API 响应。")
        else:
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, "状态code错误，请检查获取天气模块的输入参数和认证信息。")
    except requests.RequestException:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "访问url失败，请检查网络连接和url。")


# 创建主窗口
root = tk.Tk()
root.title("天气查询")

# 创建城市输入框
city_label = tk.Label(root, text="请输入城市:")
city_label.pack()
city_entry = tk.Entry(root)
city_entry.pack()


# 创建查询按钮
query_button = tk.Button(root, text="查询", command=get_weather)
query_button.pack()

# 创建结果文本框
result_text = tk.Text(root, height=10, width=50)
result_text.pack()

# 运行主循环
root.mainloop()