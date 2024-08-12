import openai
from config import OPENAI_API_KEY

def get_activities(city, weather_description):
    openai.api_key = OPENAI_API_KEY
    prompt = f"Create a table with 10 activities that can be done in {city} during {weather_description}. Add a column with a prompt for generating a relevant image for each activity."

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    
    return response.choices[0].text.strip()