from flask import Flask, abort, request
from req import get_weather
from datetime import datetime, date
from news import all_news
from names import get_names
app = Flask(__name__)


@app.route("/weater")
def weater_page():
    api_key = "871a34381b7f452a92d6f61c7e62c4df"
    city_id=524901
    url = "http://api.openweathermap.org/data/2.5/weather?id={city}&APPID={key}&units=metric".format(city=city_id, key=api_key)
    weather = get_weather(url)
    page_data = """<p><b>Сегодня - </b> {data}</p>
    <p>в городе <b>{city}</b> <b>температура на улице</b> {temp} в градусах Цельсия</p>
    <a href="/">Вернуться на главную</a>
    """.format(data=datetime.now().strftime("%d.%m.%Y"), city=weather["name"], temp=weather['main']['temp'])

    return page_data

@app.route("/news")
def all_news_page():
    colors = ["green", "red", "blue", "magenta", "black"]
    try:
        limit = int(request.args.get('limit'))
    except:
        limit = 10

    color = request.args.get('color') if request.args.get('color') in colors else "black"
    page_data = '<h1 style="color:{color}"> News <h1>'.format(color=color)
    for news in all_news:
        page_data += news_by_id(news.get("id"))
    page_data += 'Максимум : {limit}. </br> <a href="/">Вернуться на главную</a>'.format(limit=limit)
    return page_data


@app.route("/news/<int:news_id>")
def news_by_id_page(news_id):
    news_to_show = [news for news in all_news if news["id"] == news_id]
    page_data = "Такой новости нет..."
    if len(news_to_show):
        data=news_to_show[0]
        page_data = """<h1>{title}</h1></br>        
        <i>{date}</i>
        <p>{body}</p>
        """.format(title=data.get('title'), body=data.get('text'), date=data.get('date'))
    return page_data

@app.route("/names")
def names_page():
    try:
        year = int(request.args.get('year'))
    except:
        year = 0


    api_key="c35d4b418b278a6174df2aa7b38566cb"
    names_list = get_names("http://api.data.mos.ru/v1/datasets/2009/rows?api_key={key}".format(key=api_key))
    
    table_content = """
        <tr> 
            <th>Имя</th>
            <th>Год</th>
            <th>Месяц</th>
            <th>Количество</th>
        </tr>
     """

    for name_dict in names_list:
        if year != 0 and name_dict['Cells'].get('Year') != year:
            continue
        name_data=name_dict['Cells']
        table_content += """
        <tr> 
            <td>{name}</td>
            <td>{year}</td>
            <td>{month}</td>
            <td>{number}</td>
        </tr>
        """.format(name=name_data.get('Name'), year=name_data.get('Year'), 
            month=name_data.get('Month'), number=name_data.get('NumberOfPersons'))
    table_content = '''
    <table cellspacing="2" border="1" cellpadding="5">
        {content}
    </table></br> 
    <a href="/">Вернуться на главную</a>'''.format(content=table_content)

    return table_content

@app.route('/')
def index_page():
    return '''<h2>Hi!</h2> 
    Please use <a href="../weater">weater</a>, 
    <a href="../news">news</a> and <a href="../names">names</a> pages. '''

if __name__ == "__main__":
    app.run()