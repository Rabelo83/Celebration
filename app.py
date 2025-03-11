from flask import Flask, jsonify, send_from_directory
from datetime import datetime
import os

app = Flask(__name__, static_folder='static')

events = [
    {"name": "Alfredo", "type": "Cumple", "date": "2025-11-28"},
    {"name": "Mairelys", "type": "Cumple", "date": "2025-12-26"},
    {"name": "Alejandra", "type": "Cumple", "date": "2025-08-13"},
    {"name": "Adiel", "type": "Cumple", "date": "2025-02-14"},
    {"name": "Alfredo y Mairelys", "type": "Aniversario", "date": "2025-08-09"},
    {"name": "Tania", "type": "Cumple", "date": "2025-09-11"},
    {"name": "Osvaldo", "type": "Cumple", "date": "2025-05-13"},
    {"name": "Dayron", "type": "Cumple", "date": "2025-10-30"},
    {"name": "Daylen", "type": "Cumple", "date": "2025-01-14"},
    {"name": "Manuel", "type": "Cumple", "date": "2025-11-02"},
    {"name": "Alicia", "type": "Cumple", "date": "2025-06-29"},
    {"name": "Abrahan", "type": "Cumple", "date": "2025-02-15"},
    {"name": "Daniela", "type": "Cumple", "date": "2025-04-04"},
    {"name": "Emma", "type": "Cumple", "date": "2025-11-11"},
    {"name": "Aaron", "type": "Cumple", "date": "2025-08-26"},
    {"name": "Luis Manuel", "type": "Cumple", "date": "2025-09-05"},
    {"name": "Anita", "type": "Cumple", "date": "2025-05-07"},
    {"name": "Karolina", "type": "Cumple", "date": "2025-04-01"},
]

def get_time_remaining(event_date):
    now = datetime.now()
    event_dt = datetime.strptime(event_date, "%Y-%m-%d")
    time_diff = event_dt - now

    return {
        "days": time_diff.days,
        "hours": (time_diff.seconds // 3600) % 24,
        "minutes": (time_diff.seconds // 60) % 60,
        "seconds": time_diff.seconds % 60
    }

@app.route('/events', methods=['GET'])
def get_events():
    sorted_events = sorted(events, key=lambda e: datetime.strptime(e["date"], "%Y-%m-%d"))
    for event in sorted_events:
        event["countdown"] = get_time_remaining(event["date"])
    return jsonify(sorted_events)

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
