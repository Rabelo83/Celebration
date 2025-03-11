from flask import Flask, jsonify, send_from_directory
from datetime import datetime, timedelta
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
    {"name": "Abraham", "type": "Cumple", "date": "2025-02-15"},
    {"name": "Daniela", "type": "Cumple", "date": "2025-04-04"},
    {"name": "Emma", "type": "Cumple", "date": "2025-11-11"},
    {"name": "Aaron", "type": "Cumple", "date": "2025-08-26"},
    {"name": "Luis Manuel", "type": "Cumple", "date": "2025-09-05"},
    {"name": "Anita", "type": "Cumple", "date": "2025-05-07"},
    {"name": "Karolina", "type": "Cumple", "date": "2025-04-01"},
    {"name": "Yenier", "type": "Cumple", "date": "2025-04-11"},
    {"name": "Thiago", "type": "Cumple", "date": "2025-06-16"},
    {"name": "Karolina", "type": "Cumple", "date": "2025-10-16"},
    {"name": "Luis y Daylen", "type": "Aniversario", "date": "2025-09-01"},
    {"name": "Yenier y Anita", "type": "Aniversario", "date": "2026-02-20"},
    {"name": "Alicia y Manuel", "type": "Aniversario", "date": "2025-05-25"},
    {"name": "Abuela Aya", "type": "Cumple", "date": "2025-11-09"},
    {"name": "Denisse", "type": "Cumple", "date": "2025-07-25"},
    {"name": "Miguel", "type": "Cumple", "date": "2025-12-03"},
]

def get_time_remaining(event_date):
    now = datetime.now()
    event_dt = datetime.strptime(event_date, "%Y-%m-%d")
    if event_dt < now:
        event_dt = event_dt.replace(year=now.year + 1)  # Move past events to the next year
    time_diff = event_dt - now

    return {
        "days": time_diff.days,
        "hours": (time_diff.seconds // 3600) % 24,
        "minutes": (time_diff.seconds // 60) % 60,
        "seconds": time_diff.seconds % 60
    }

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/events', methods=['GET'])
def get_events():
    upcoming_events = []
    for event in events:
        event_date = datetime.strptime(event["date"], "%Y-%m-%d")
        if event_date < datetime.now():
            event_date = event_date.replace(year=datetime.now().year + 1)
        event["date"] = event_date.strftime("%Y-%m-%d")  # Update event date if moved
        event["countdown"] = get_time_remaining(event["date"])
        upcoming_events.append(event)
    
    sorted_events = sorted(upcoming_events, key=lambda e: datetime.strptime(e["date"], "%Y-%m-%d"))
    return jsonify(sorted_events)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
