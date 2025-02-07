import requests


#获取城市
def get_city(city):
    api_key = "60476540a0944aa2b2cfa50135bc4c24"
    url=f'https://geoapi.qweather.com/v2/city/lookup?location={city}&key={api_key}'
    response = requests.get(url)
    if response.status_code== 200:
        city_data = response.json()
        if city_data and city_data.get("location"):
            #获取location内容
            location_list = city_data.get("location")
            #获取location第一个列表【】里的内容
            city_value = location_list[0]
            #获取城市ID
            city_id = city_value.get('id')
            return  city_id
        else:
            print("未找到 'location' 部分的天气数据，请检查 API 响应。")
    else:
        print("获取城市信息失败，请检查输入的城市或网络连接。")

#获取天气
def get_weather(city):
    # 这里使用的是一个免费的天气 API，需要替换为你自己的 API 以及 API 密钥
    api_key = "60476540a0944aa2b2cfa50135bc4c24"
    # url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    url = f"https://devapi.qweather.com/v7/weather/now?location={city}&key={api_key}"

    response = requests.get(url)
    if response.status_code == 200:
        weather_data = response.json()
        # 提取主要的天气信息
        if weather_data and weather_data.get("now"):
            now = weather_data.get('now')
            if now:
                time = now.get("obsTime")
                description = now.get("text")
                temperature = now.get("temp")
                humidity = now.get("windDir")
                print(f"城市:",city_name)
                print(f"时间: {time}")
                print(f"天气状况: {description}")
                print(f"温度: {temperature}°C")
                print(f"风向: {humidity}")
        else:
            print("未找到 'now' 部分的天气数据，请检查 API 响应。")
    else:
        print("获取天气信息失败，请检查输入的城市或网络连接。")


if __name__ == "__main__":
    city_name = input("请输入你想要查询天气的城市: ")
    city_id = get_city(city_name)
    get_weather(city_id)