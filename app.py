from flask import Flask, render_template
import requests
from datetime import datetime
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "http://localhost:5000"}})


def get_filtered_departures(station_id = "310"):
    # Get departures
    rurl = f"https://www.mvg.de/api/bgw-pt/v3/departures?globalId=de%3A09162%3A{station_id}&limit=20&offsetInMinutes=0"
    print(station_id, rurl)
    departure_response = requests.get(
        rurl
    )
    print("DEPARTURES", departure_response)
    departures = departure_response.json()
    print(departures)
    return departures

@app.after_request
def set_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/")
def website():
    return render_template('departures.html')

@app.route('/line/<station_id>')
def line_departures(station_id):
    departures = get_filtered_departures(station_id=station_id)
    return departures

def minutes_until_filter(timestamp):
    local_tz = datetime.now().astimezone().tzinfo
    now = datetime.now().astimezone(local_tz).timestamp()
    delta = (timestamp/1000 - now) / 60
    return f"{max(0, int(round(delta)))} min"

app.jinja_env.filters['minutes_until'] = minutes_until_filter


if __name__ == '__main__':
    app.run(debug=True)
