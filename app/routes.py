from flask import Flask, render_template, request
from .weather import get_weather_data
from .activities import get_activities

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            weather_data = get_weather_data(city)
            weather_description = weather_data['current']['condition']['text']
            activities_text = get_activities(city,weather_description)

            # Parse activities
            activities = parse_activities(activities_text)
            
    return render_template('index.html', city=city, activities=activities)


def parse_activities(text):
    # Convert the text response into a list of activities and image prompts
    activities = []
    # Example parsing logic
    lines = text.split('\n')
    for line in lines:
        if line.strip():
            activity, image_prompt = line.split('|')
            activities.append((activity.strip(), image_prompt.strip()))
    return activities