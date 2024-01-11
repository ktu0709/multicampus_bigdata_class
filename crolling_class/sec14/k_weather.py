import xml.etree.ElementTree as ET

#1. 파일을 로드하자.
tree = ET.parse("weather.xml")
root  = tree.getroot()   # <weather>
print(root)
#2.하위 요소 추출
for city in root.findall('city'):
    city_name = city.get('name')
    temperature = city.find('temperature').text
    weather_condition = city.find('weather_condition').text
    humidity = city.find('humidity').text
    wind_speed = city.find('wind_speed').text

    #값 출력
    print("City:", city_name)
    print("Temperature:", temperature)
    print("Weather Condition:", weather_condition)
    print("Humidity:", humidity)
    print("Wind Speed:", wind_speed)
    print()
