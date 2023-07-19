from flask import Flask, render_template, request
import openai
import requests
import markdown
import json

openai.api_key = "<api>"
accu_api_key = "<api>"

app = Flask(__name__)


def search_by_query(query, api_key):
    locations_search = {}
    response_search = requests.get(f"https://dataservice.accuweather.com/locations/v1/cities/autocomplete?apikey={api_key}&q={query}").json()
    for i in response_search: locations_search[f"{i['LocalizedName']}, {i['AdministrativeArea']['LocalizedName']}, {i['Country']['LocalizedName']}"] = i['Key']

    return locations_search


def get_from_loc_key(location_key, api_key):
    response = requests.get(f"https://dataservice.accuweather.com/currentconditions/v1/{location_key}?apikey={api_key}&details=true").json()

    weather_text = f"{response[0]['WeatherText']}"
    temperature = f"{response[0]['Temperature']['Metric']['Value']} Celcius"
    humidity = f"Humidty: %{response[0]['RelativeHumidity']}"
    pressure = f"Pressure: {response[0]['PressureTendency']['LocalizedText']} {response[0]['Pressure']['Metric']['Value']} mb"
    wind = f"Wind: {response[0]['Wind']['Direction']['English']} {response[0]['Wind']['Speed']['Metric']['Value']} km/h"
    location_link = response[0]['MobileLink']
    icon = response[0]['WeatherIcon']

    all_list = [weather_text, temperature, humidity, pressure, wind]
    return "\n".join(all_list), (response[0]['WeatherText'], response[0]['Temperature']['Metric']['Value'], response[0]['RelativeHumidity'], f"{response[0]['PressureTendency']['LocalizedText']} {response[0]['Pressure']['Metric']['Value']} mb", f"{response[0]['Wind']['Direction']['English']} {response[0]['Wind']['Speed']['Metric']['Value']} km/h", icon)


def getanswerfrom_openai(text):
    system_prompt = "I want you to give me a review and recommenditions about the given weather. I will provide you the weather. You answers should be in markdown language and titles font should be big. Give your answer as detailed as possible."

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": text}
        ]
    )

    # print(f"Tokens used: {str(response.usage['total_tokens'])}")

    return response["choices"][0]["message"]["content"]


@app.route('/')
def index():
    return render_template('search.html')


@app.route('/search', methods=['POST', 'GET'])
def search():
    if request.method == 'POST':
        query = request.form.get('query')
        results = search_by_query(query, accu_api_key)
    else:
        results = None

    return render_template('search.html', results=results)


@app.route('/handle_selection', methods=['POST'])
def handle_selection():
    selected_loc_key = request.form.get('location')
    location_name = request.form.get('name')

    gettingfromlockey = get_from_loc_key(selected_loc_key, accu_api_key)

    prompt = gettingfromlockey[0] + f"\nLocation: {location_name}\n\nReview and Recommendations: "

    answer = getanswerfrom_openai(prompt)

    html_format = markdown.markdown(answer)

    widget = f"""    
        <div class="weather-widget">
        <div class="weather-icon">
            <img src="https://www.accuweather.com/images/weathericons/{gettingfromlockey[1][5]}.svg" alt="Weather Icon">
            <center><p class="temperature">{gettingfromlockey[1][1]}°C</p></center>
        </div>
        <div class="weather-info">
            <p class="weather-condition">{gettingfromlockey[1][0]}</p>
            <p class="humidity"><img src="/static/images/humidity.png" width="20px" height="20px"><b> Humidity:</b> {gettingfromlockey[1][2]}%</p>
            <p class="pressure"><img src="/static/images/pressure.png" width="20px" height="20px"><b> Pressure:</b> {gettingfromlockey[1][3]}</p>
            <p class="wind"><img src="/static/images/wind.png" width="20px" height="20px"><b> Wind:</b> {gettingfromlockey[1][4]}</p>
            <p class="location"><img src="/static/images/location.jpg" width="20px" height="20px"><b> Location:</b> {location_name}</p>
        </div>
    </div>
    """

    center_lamak_icin = '\n<div class="weather-info answer-content">'

    return json.dumps({'location': prompt, 'answer_html': widget+center_lamak_icin+"<br><br><br>"+html_format+"</div>"})


if __name__ == "__main__":
    app.run(debug=False)
