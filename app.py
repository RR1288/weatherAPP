from flask import Flask, render_template, request
import requests
from config import API_KEY, BASE_URL

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            complete_url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
            response = requests.get(complete_url)
            if response.status_code == 200:
                weather_data = response.json()
            else:
                weather_data = {'error': 'City not found'}
            
    return render_template('index.html', weather_data=weather_data)
    
if __name__ == "__main__":
    app.run(debug=True)







