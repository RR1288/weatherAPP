from flask import Flask, render_template, request
from weather import get_weather_data
from activities import get_activities
import json
import logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    print("Handling request...")  # Debug print statement
    weather_data = None
    city=None
    activities=None

    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            # Get today's weather
            weather_data = get_weather_data(city)
            app.logger.debug(weather_data)
            weather_description = weather_data['weather'][0]['description']
            
            # Get activities
            activities_text = get_activities(city,weather_description)
            app.logger.debug(activities_text)
            # Parse activities
            activities = parse_activities(activities_text)

            
    return render_template('index.html', city=city, activities=activities, weather_data=weather_data)


def parse_activities(text):
    try:
        activities = json.loads(text)
        return [(a['description'], a['image_prompt']) for a in activities]
    except json.JSONDecodeError as e:
        print("Failed to parse JSON:", e)
        print("Raw text was:", text)
        return []