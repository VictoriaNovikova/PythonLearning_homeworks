import requests

def get_names(url):
    
    result = requests.get(url)
    if result.status_code == 200:
        return result.json()
    else:
        print("Something went wrong...")


if __name__ == "__main__":
    api_key="c35d4b418b278a6174df2aa7b38566cb"
    data = get_names("http://api.data.mos.ru/v1/datasets/2009/rows?api_key={key}".format(key=api_key))
    print(data)