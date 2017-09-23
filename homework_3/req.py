import requests

def get_weather(url):
    print(url)
    result = requests.get(url)
    if result.status_code == 200:
        return result.json()
    else:
        print("Something went wrong...")


if __name__ == "__main__":
    api_key = "871a34381b7f452a92d6f61c7e62c4df"

    data = get_weather("http://api.openweathermap.org/data/2.5/weather?id=524901&APPID={key}&units=metric".format(key=api_key))
    print(data)